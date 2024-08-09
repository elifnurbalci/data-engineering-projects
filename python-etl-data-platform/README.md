# The Data Engineering Project

## Objective

This project aims to create a robust data platform that extracts, transforms, and loads (ETL) data from a source into an AWS-hosted data lake and warehouse. The solution should be reliable, resilient, and ideally managed through code.

By the end of this project, you should have achieved the following:
- Developed Python applications that interact with AWS and database infrastructure, and manipulate data as required.
- Remodeled data into a data warehouse hosted on AWS.
- Demonstrated effective monitoring and performance measurement of your project.
- Deployed parts of the project using scripting or automation.

Your solution should showcase your expertise in Python, SQL, database modelling, AWS, operational practices, and Agile methodologies.

## Minimum Viable Product (MVP)

The goal is to develop a data platform that extracts data from an operational database (and potentially other sources), archives it in a data lake, and remodels it into an OLAP data warehouse.

### Key Deliverables

1. **S3 Buckets:**
   - Two S3 buckets:
     - **Ingested Data Bucket**: For raw, unaltered data.
     - **Processed Data Bucket**: For data stored in Parquet format after transformation.
   - Data in these buckets should be immutable—once written, data should not be amended or overwritten.

2. **Python Ingestion Application:**
   - Automatically ingests all tables from the `totesys` database.
   - Saves data in the "ingestion" S3 bucket in a suitable format.
   - Operates on a schedule, logs progress to CloudWatch, and triggers email alerts on failures.
   - Adheres to good security practices.

3. **Python Transformation Application:**
   - Remodels data into a predefined schema for the data warehouse.
   - Stores transformed data in the "processed" S3 bucket in Parquet format.
   - Triggers automatically upon completion of data ingestion, and is monitored and logged adequately.

4. **Python Data Loading Application:**
   - Loads data from S3 into the data warehouse at defined intervals.
   - Includes comprehensive logging and monitoring.

5. **Quicksight Dashboard:**
   - Displays useful data from the warehouse.
   - SQL queries for data retrieval will be provided, and assistance with dashboard construction will be available.

### Data Requirements

- **Primary Source:** `totesys` database (a simulated commercial application backend).
- **Data Source ERD:** [ERD for totesys](https://dbdiagram.io/d/6332fecf7b3d2034ffcaaa92).
- **Data Warehouse ERDs:** 
  - [Sales Schema](https://dbdiagram.io/d/637a423fc9abfc611173f637)
  - [Purchases Schema](https://dbdiagram.io/d/637b3e8bc9abfc61117419ee)
  - [Payments Schema](https://dbdiagram.io/d/637b41a5c9abfc6111741ae8)
- **Tables to be Ingested:**
  - counterparty, currency, department, design, staff, sales_order, address, payment, purchase_order, payment_type, transaction

## Technical Details

### Required Components

1. **Job Scheduler:** Use AWS EventBridge to schedule ingestion jobs.
2. **S3 Buckets:** One for raw data and another for processed data.
3. **Ingestion Application:** Python-based, preferably using AWS Lambda for event-driven processing.
4. **Transformation Application:** Python-based, triggered by S3 events or on a schedule.
5. **Data Loading Application:** Updates the data warehouse from S3 at intervals.
6. **Automation:** Deployment should be automated using Infrastructure-as-Code (IaC) and CI/CD practices. Terraform is recommended.

## Contact

For any queries or further information, please reach out:

- **Email:** [elfnurbalci@gmail.com](mailto:elfnurbalci@gmail.com) ![Email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)
- **GitHub:** [elifnurbalci](https://github.com/elifnurbalci) ![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)