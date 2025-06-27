from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import logging
import os

# Default configuration for all tasks in the DAG
default_args = {
    'owner': 'Bita',                     # Name shown in the Airflow UI
    'retries': 2,                            # Retry failed tasks up to 2 times
    'retry_delay': timedelta(minutes=5),     # Wait time between retries
    'start_date': datetime(2024, 1, 1),      # When to start scheduling
}

# Task 1: Extract simulated MSP asset data and save locally
def extract_assets():
    logging.info("📥 Extracting mock MSP asset data...")
    
    # Sample records to simulate API call response
    sample_data = [
        {"client_id": 1, "device": "Server01", "backup_status": "Healthy"},
        {"client_id": 2, "device": "Laptop22", "backup_status": "Failed"}
    ]

    # Ensure directory exists for temporary storage
    os.makedirs('/opt/airflow/tmp', exist_ok=True)

    # Save the mock data to a JSON file
    with open('/opt/airflow/tmp/assets.json', 'w') as f:
        import json
        json.dump(sample_data, f)

    logging.info("✅ Asset data saved to assets.json.")

# Task 2: Transform the asset data (e.g., standardize format)
def transform_assets():
    logging.info("🔄 Transforming asset data...")

    import json

    # Read data from the previous task
    with open('/opt/airflow/tmp/assets.json', 'r') as f:
        data = json.load(f)

    # Standardize device names and backup status
    transformed = [
        {
            "client_id": item["client_id"],
            "device": item["device"].upper(),
            "status": "OK" if item["backup_status"] == "Healthy" else "ALERT"
        } for item in data
    ]

    # Save transformed data
    with open('/opt/airflow/tmp/transformed_assets.json', 'w') as f:
        json.dump(transformed, f)

    logging.info("✅ Transformation complete. Saved to transformed_assets.json.")

# Task 3: Upload the transformed data to AWS S3 using helper function
def upload_to_s3():
    from scripts.upload_to_s3 import upload_file_to_s3

    logging.info("🚀 Starting upload to S3...")
    bucket = os.environ.get("AWS_S3_BUCKET")  # Set in .env
    local_path = '/opt/airflow/tmp/transformed_assets.json'
    s3_key = 'assets/transformed_assets.json'

    upload_file_to_s3(local_path, bucket, s3_key)

# Define and instantiate the DAG
with DAG(
    dag_id='msp_asset_sync_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    description='Simulates syncing MSP asset data to AWS S3',
    tags=['scalepad', 'msp', 'aws', 'airflow']
) as dag:

    # Define each task
    extract_task = PythonOperator(
        task_id='extract_assets',
        python_callable=extract_assets
    )

    transform_task = PythonOperator(
        task_id='transform_assets',
        python_callable=transform_assets
    )

    upload_task = PythonOperator(
        task_id='upload_to_s3',
        python_callable=upload_to_s3
    )

    # Task execution order
    extract_task >> transform_task >> upload_task