import pyarrow as pa
import pyarrow.parquet as pq
from utils.config import RESULT_FILE_LOC

class Loader:
    def __init__(self):
        pass

    def load(self, transformed_data):
        # Saving transformed data to Parquet
        table = pa.Table.from_pandas(transformed_data)
        pq.write_table(table, RESULT_FILE_LOC)