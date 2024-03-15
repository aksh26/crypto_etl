# This function fetches data in batches of page_size rows 
# and keeps track of the page_token 
# to fetch the next page of data. 
# We can also adjust the page_size parameter as per our dataset size and system resources available.

from google.cloud import bigquery
import os
import pandas as pd
from utils.config import READ_SIZE

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "utils/google_creds.json"


class Extractor:
    
    def __init__(self, database, schema, table):
        self._client = bigquery.Client()
        self._database = database
        self._schema = schema
        self._table = table
        self._page_size = READ_SIZE
        
    def extract(self):

        
        extractquery = f"""
        SELECT *
        FROM `{self._database}.{self._schema}.{self._table}`
        LIMIT 1000
        """
        result = self._client.query(extractquery).to_dataframe()
        page_token = 0
        result = []
        while True:
        # Fetching data with pagination using page size and token in offset to limit number of rows 
            query_job = self._client.query(
                """
                SELECT *
                FROM FROM `{self._database}.{self._schema}.{self._table}`
                ORDER BY id
                LIMIT @page_size
                OFFSET @page_size * @page_number
                """,
                job_config=bigquery.QueryJobConfig(
                    query_parameters=[
                        bigquery.ScalarQueryParameter("page_size", "INT64", self._page_size),
                        bigquery.ScalarQueryParameter("page_number", "INT64", page_token)
                    ]
                )
            )

            # Fetching results on basis of parameter
            query_result = query_job.result()

            # Appending fetched rows to the result list
            result.extend(query_result)

            # Updating page token to get next set of records
            page_token = query_job.next_page_token

            # Break loop if next page token not found
            if not page_token:
                break

        return result
