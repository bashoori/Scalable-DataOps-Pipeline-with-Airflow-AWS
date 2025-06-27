import os
import logging
import boto3

def upload_file_to_s3(local_path, bucket_name, s3_key):
    """
    Uploads a local file to an S3 bucket.

    Parameters:
    - local_path: Path to the file on local disk
    - bucket_name: Target S3 bucket name
    - s3_key: Desired key (path) in the S3 bucket
    """
    logging.info(f"Uploading {local_path} to s3://{bucket_name}/{s3_key}...")

    # Initialize boto3 S3 client
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
    )

    try:
        with open(local_path, "rb") as f:
            s3.upload_fileobj(f, bucket_name, s3_key)
        logging.info("✅ Upload successful.")
    except Exception as e:
        logging.error(f"❌ Upload failed: {str(e)}")
        raise