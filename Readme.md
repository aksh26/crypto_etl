# Crypto ETL Project

## Project Structure

```
crypto_etl/
|-- src/
|   |-- utils/
|   |   |-- common_config.py   # Contains database name, schema name, and result file path
|   |   |-- google_creds.json  # Google Cloud credentials 
|   |-- __init__.py
|   |-- driver.py              # Main driver script
|   |-- extract.py             # Extraction module
|   |-- transform.py           # Transformation module
|   |-- load.py                # Loading module
|-- requirements.txt
|-- Dockerfile
|-- README.md
```

## Files and Modules

### 1. `common_config.py`
This file holds common configurations such as database name, schema name, and the path for the result file.

### 2. `google_creds.json`
This file should contain the Google Cloud credentials necessary for accessing the BigQuery API. Replace this file with your own credentials.

### 3. `driver.py`
The main script that orchestrates the ETL process. It initializes the extraction, transformation, and loading modules and executes the entire pipeline.

### 4. `extract.py`
Responsible for extracting data from the BigQuery public crypto_zillqa dataset using the BigQuery API and pagination. It utilizes the configurations from `common_config.py`.

### 5. `transform.py`
Handles the transformation of the extracted data. It applies various transformations such as aggregations, summarizations, or computed metrics.

### 6. `load.py`
Manages the loading of the transformed data into a Parquet file. It uses the configurations from `common_config.py` to determine the output file path.

### 7. `requirements.txt`
Contains the necessary Python packages and versions required for the project. Use this file to install dependencies.

### 8. `Dockerfile`
The Docker configuration file to containerize the ETL pipeline. It specifies the base image and the commands needed to set up the environment.

## How to Run the Project with Docker

1. Build the Docker image:
   ```bash
   docker build -t crypto_etl .
   ```

2. Run the Docker container:
   ```bash
   docker run crypto_etl
   ```

This will execute the ETL pipeline within the Docker container, pulling data from BigQuery, performing transformations, and saving the results to a Parquet file.

Note: Ensure that you replace `google_creds.json` with your own Google Cloud credentials before running the Docker container. Additionally, customize `common_config.py` as needed for your specific database and schema details.