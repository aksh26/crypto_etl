import os

DATABASE = os.environ.get("DATABASE","bigquery-public-data")
SCHEMA = os.environ.get("SCHEMA","crypto_zilliqa")
TABLE = os.environ.get("TABLE","transactions")
RESULT_FILE_LOC = os.environ.get("RESULT_FILE_LOC","output_files/result.parquet")
LOG_FILE_LOC = os.environ.get("LOG_FILE_LOC","output_files/etl_pipeline.log")
READ_SIZE = os.environ.get("READ_SIZE",10000)
LOAD_SIZE = os.environ.get("LOAD_SIZE",10000)
