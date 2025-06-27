# 🚀 Scalable DataOps Pipeline with Airflow & AWS 

A modular data pipeline that simulates syncing MSP asset data, fully orchestrated with Apache Airflow and integrated with AWS S3.  
The project is designed to showcase production-grade skills relevant to a SaaS company.

---

## 🧠 Project Summary

This pipeline mimics a real-world SaaS use case for Managed Service Providers (MSPs). It automates the extraction of asset data, transforms it to meet quality standards, and uploads the cleaned result to Amazon S3 — ready for analytics or reporting.

---

## 🛠️ Tech Stack

- **Apache Airflow 2.9** – workflow orchestration
- **Docker Compose** – containerized local environment
- **AWS S3** – cloud storage for cleaned asset data
- **Python** – ETL scripting and logging
- **GitHub Codespaces** – cloud-based development
- *(Optional)* Redshift integration support

---

## 📦 Folder Structure
```
Scalable-DataOps-Pipeline-with-Airflow-AWS/
├── dags/                      # Airflow DAG definition
├── scripts/                   # Reusable Python modules
├── docker/                    # Docker Compose config
├── .devcontainer/             # Codespaces setup
├── .github/workflows/         # CI/CD (optional)
├── .env                       # AWS + Redshift secrets (ignored by Git)
├── .gitignore
├── README.md
├── requirements.txt
└── assets/                    # Diagrams or static images
```

---

## 🔁 DAG Overview: `msp_asset_sync_pipeline`

| Task            | Description                                                  | Output File                          |
|-----------------|--------------------------------------------------------------|--------------------------------------|
| `extract_assets`| Simulates pulling asset info (e.g., backup status, devices)  | `/opt/airflow/tmp/assets.json`       |
| `transform_assets` | Cleans and standardizes fields                             | `/opt/airflow/tmp/transformed_assets.json` |
| `upload_to_s3`  | Uploads cleaned data to AWS S3                               | `s3://<your-bucket>/assets/...`      |

---

## 📂 `.env` Configuration
```
# AWS Credentials & S3
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_REGION=us-west-2
AWS_S3_BUCKET=your-bucket-name

# Redshift (optional)
REDSHIFT_HOST=...
REDSHIFT_DB=...
REDSHIFT_USER=...
REDSHIFT_PASSWORD=...
REDSHIFT_PORT=5439
```

## 🧪 How to Run Locally
	1.	Clone the repository:
    ```
    git clone https://github.com/YOUR_USERNAME/Scalable-DataOps-Pipeline-with-Airflow-AWS.git
    cd Scalable-DataOps-Pipeline-with-Airflow-AWS
    ```
    2.	Configure .env
	•	Copy the example and add your AWS keys and bucket.

	3.	Launch with Docker
    ```
    cd docker
    docker-compose up airflow-init
    docker-compose up
    ```
    	4.	Access Airflow UI
	•	Go to: http://localhost:8080
	•	Trigger the DAG: msp_asset_sync_pipeline
    
##  📊 Architecture Diagram

Include diagram here once created (e.g., ETL → S3 → Redshift)

⸻

💡 Future Enhancements
	•	Redshift loader for BI/analytics
	•	Slack/Email alerts on failure
	•	Unit tests & CI integration
	•	API-based real data ingestion   

👩‍💻 Author

Bita Ashoori
LinkedIn | GitHub