import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from utils.config import RESULT_FILE_LOC, LOAD_SIZE

class Loader:
    def __init__(self):
        pass

    def load(self, transformed_data):
        # Saving transformed data to Parquet
        table = pa.Table.from_pandas(transformed_data)
        pq.write_table(table, RESULT_FILE_LOC)
        # Converting transformed data to a pandas DataFrame
        df = pd.DataFrame(transformed_data)

        # Saving DataFrame to Parquet file in chunks where chunk_size can be adjusted 
        chunk_size = LOAD_SIZE
        num_chunks = len(df) // chunk_size + 1

        for i in range(num_chunks):
            start_index = i * chunk_size
            end_index = min((i + 1) * chunk_size, len(df))
            chunk_df = df.iloc[start_index:end_index]

            # Converting chunk to pyarrow Table
            table = pa.Table.from_pandas(chunk_df)

            # Appending chunk table to Parquet file
            # Using the 'snappy' compression for efficient storage 
            # and the 'use_dictionary' option to enable dictionary encoding, 
            # which can further reduce the file size.
            if i == 0:
                pq.write_table(table, RESULT_FILE_LOC, compression='snappy', use_dictionary=True, mode='overwrite')
            else:
                pq.write_table(table, RESULT_FILE_LOC, compression='snappy', use_dictionary=True, mode='append')
