import tap_brightview.helpers as helper


def test_create_table_list():
    tables = helper.create_table_list("db_tables.txt")

    assert isinstance(tables, list)
    assert len(tables) > 0
    assert isinstance(tables[0], str)


def test_sql_to_json():
    response = [
        (
            1001,
            "HTS-BHS",
            "HTS-BH Supervision",
            "2018-06-01 00:00:00",
            "2020-03-09 00:00:00",
            "S",
            None,
            "N",
            "N",
            "Y",
            "N",
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            1000,
            1,
            "2005-02-14 10:48:32",
            38042,
            "2020-03-09 12:11:40",
            "T",
            None,
            None,
            None,
            1,
            None,
            None,
            None,
            None,
            "N",
            "N",
            None,
            None,
            None,
            "MH",
            "N",
            None,
            None,
            "N",
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            "ins",
            "2020-11-09 21:44:16",
            "2020-11-11 00:01:27.165000",
        ),
        (
            1005,
            "IC",
            "Individual Counseling",
            "2010-01-01 00:00:00",
            "2015-01-02 00:00:00",
            "C",
            None,
            "Y",
            "Y",
            "N",
            "N",
            None,
            None,
            15,
            "Minutes",
            None,
            None,
            None,
            1000,
            1,
            "2010-11-24 09:43:56",
            14884,
            "2016-01-26 12:28:42",
            "N",
            None,
            None,
            None,
            1,
            None,
            None,
            None,
            None,
            "N",
            "N",
            None,
            None,
            None,
            "MH",
            "P",
            None,
            None,
            "N",
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            "ins",
            "2020-11-09 21:44:16",
            "2020-11-11 00:01:27.165000",
        ),
        (
            1007,
            "OIC",
            "ODADAS Individual Counseling",
            "2010-01-01 00:00:00",
            "2015-01-02 00:00:00",
            "C",
            None,
            "Y",
            "N",
            "N",
            "N",
            None,
            None,
            15,
            "Minutes",
            None,
            None,
            None,
            1000,
            1,
            "2010-12-03 08:19:37",
            14884,
            "2016-01-26 13:02:35",
            "N",
            None,
            None,
            None,
            1,
            None,
            None,
            None,
            None,
            "N",
            "N",
            None,
            None,
            None,
            "MH",
            "P",
            None,
            None,
            "N",
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            "ins",
            "2020-11-09 21:44:16",
            "2020-11-11 00:01:27.165000",
        ),
    ]

    json_schema = helper.open_json_schema("activity")
    json_response = helper.create_json_response(json_schema, response)

    assert isinstance(json_response, dict)
    # assert json_response[0] != json_response[1]
    # assert len(json_response) > 1
    # assert isinstance(json_response[0], dict)
