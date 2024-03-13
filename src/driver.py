from extract import Extractor
from transform import Transformer
from load import Loader
from utils.config import DATABASE, SCHEMA, TABLE, LOG_FILE_LOC


import logging

logging.basicConfig(filename=LOG_FILE_LOC, level=logging.INFO)

class ETLDriver:
    def __init__(self):
        pass

    def run(self):
        try:
            logging.info("Starting ETL pipeline")

            # Extraction
            logging.info("Extracting data from BigQuery")
            extractor = Extractor(DATABASE, SCHEMA, TABLE)
            extract_data = extractor.extract()

        except Exception as e:
            logging.error(f"Error while doing extraction in ETL pipeline: {str(e)}")

        try:
            # Transformation
            logging.info("Transforming data")
            transformer = Transformer()
            transformed_data = transformer.transform(extract_data)

        except Exception as e:
            logging.error(f"Error while transforming in ETL pipeline: {str(e)}")

        try:
            # Loading
            logging.info("Loading data to Parquet")
            loader = Loader()
            loader.load(transformed_data)
            logging.info("ETL pipeline completed successfully")

        except Exception as e:
            logging.error(f"Error while loading in ETL pipeline: {str(e)}")

def main():
    """Inside Main Method"""

    # Run the ETL pipeline
    etl_driver = ETLDriver()
    etl_driver.run()

if __name__ == "__main__":
    main()
