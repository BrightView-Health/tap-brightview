import requests
import json
from dotenv import load_dotenv
import os
import pprint
import singer
from singer import Transformer
from datetime import date, datetime, timezone, timedelta
from collections import defaultdict
import jaydebeapi
import jpype


pp = pprint.PrettyPrinter(indent=4, depth=3)

# This code is for production.
# args = singer.utils.parse_args(["user", "password"])
# USER = args.config['user']
# PASSWORD = args.config['password']

# The code below is for testing with Pytest.
load_dotenv()
USER = json.loads(os.getenv("brightview"))['user']
PASSWORD = json.loads(os.getenv("brightview"))['password']


client = jaydebeapi.connect(
    "com.simba.hive.jdbc.HS2Driver",
    "jdbc:hive2://bdgw.qualifacts.org:443/brightview_prod;ssl=1;transportMode=http;httpPath=gateway/default/llap",
    [USER, PASSWORD],
    "./HiveJDBC42.jar",
)

sql = client.cursor()


def query_database():
    # sql.execute("SELECT * FROM activity LIMIT 10")
    # sql.execute("SHOW CREATE TABLE activity")
    # sql.execute("DESCRIBE Formatted brightview_prod.activity")
    sql.execute("SHOW TABLES IN brightview_prod")
    query = sql.fetchall()

    return query

test = query_database()

stop = 'stop'

sql.close()
client.close()
