import singer
import json
from singer import Transformer, metadata

# The client name needs to be filled in here
from tap_brightview.client import HiveClient
from tap_brightview.streams import STREAMS

LOGGER = singer.get_logger()


def sync(config, state, catalog):
    # Any client required PARAMETERS to hit the endpoint
    client = HiveClient()

    with Transformer() as transformer:
        for stream in catalog.get_selected_streams(state):
            tap_stream_id = stream.tap_stream_id
            stream_obj = STREAMS[tap_stream_id](client, state)
            # replication_key = stream_obj.replication_key
            stream_schema = stream.schema.to_dict()
            stream_metadata = metadata.to_map(stream.metadata)

            LOGGER.info('Staring sync for stream: %s', tap_stream_id)

            state = singer.set_currently_syncing(state, tap_stream_id)
            singer.write_state(state)

            singer.write_schema(
                tap_stream_id,
                stream_schema,
                stream_obj.key_properties,
                stream.replication_key
            )

            # state.json file here
            with open('./state.json', 'w') as state_file:


                for record in stream_obj.records_sync(table_name=tap_stream_id):
                    transformed_record = transformer.transform(
                        record, stream_schema, stream_metadata)
                    LOGGER.info(f"Writing record: {transformed_record}")
                    singer.write_record(
                        tap_stream_id,
                        transformed_record,
                    )
                    singer.write_bookmark(
                        stream_obj.state,
                        stream_obj.tap_stream_id,
                        stream_obj.replication_key,
                        record['last_operation_time']
                    )
                    # singer.write_state(
                    #     {'last_operation_time': record['last_operation_time']}
                    # )
                    json.dump(state, state_file)


            # If there is a Bookmark or state based key to store
            # state = singer.clear_bookmark(
            #     state, tap_stream_id, BOOKMARK_KEY)
            # singer.write_state(state, tap_stream_id)

    state = singer.set_currently_syncing(state, None)
    # singer.write_state(state)
