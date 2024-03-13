from google.cloud import bigquery
import os
import pandas as pd

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "utils/google_creds.json"


class Extractor:
    
    def __init__(self, database, schema, table):
        self._client = bigquery.Client()
        self._database = database
        self._schema = schema
        self._table = table

    def extract(self):

        extractquery = f"""
        SELECT *
        FROM `{self._database}.{self._schema}.{self._table}`
        LIMIT 1000
        """
        result = self._client.query(extractquery).to_dataframe()
        return result