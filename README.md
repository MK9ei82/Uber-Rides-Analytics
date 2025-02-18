# Access The Dashboard Here:
https://lookerstudio.google.com/reporting/d7c0b966-5359-4dd0-95e0-6104e4f48af1/page/RtbuE

# Uber-Rides-Analytics on GCP
This project demonstrates a scalable ETL pipeline for Uber ride data using Mage AI, Google Cloud Platform (GCP), and BigQuery. The pipeline extracts, transforms, and loads taxi trip records into BigQuery, where analytics and business intelligence insights are generated via Looker Studio.

# Data Pipeline Architecture
1️. Data Ingestion – Raw trip data from TLC Taxi Records is loaded into Google Cloud Storage (GCS).
2️. Processing & Transformation – Mage AI orchestrates data transformations using Python and Pandas.
3️. Data Warehousing – Transformed data is loaded into BigQuery for analysis.
4️. Analytics & Visualization – Looker Studio connects to BigQuery to generate real-time dashboards.

<p>
  <img width="600" src="https://github.com/MK9ei82/Uber-Rides-Analytics/blob/main/misc/Data_pipeline_architecture.png" />
</p>

# Languages and Tools used
1. Python 🐍
2. GCP (Compute Instance, Google Cloud Storage, BigQuery, Looker Studio BI)
3. Mage AI for data pipeline (https://www.mage.ai/)

# Dataset
TLC Trip Record Data
- Yellow and green taxi trip records include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts.

# Data Model
Data model was generated using Python and Graphviz library.
<p>
<img height="600" src = "https://github.com/MK9ei82/Uber-Rides-Analytics/blob/main/misc/data_model_erd_diagram_script_generated.png">
</p>

# Data Pipeline
This project follows a modular ETL pipeline architecture, where data flows through the following stages:

This project uses Mage AI to automate the Extract, Transform, Load (ETL) process. The pipeline consists of:
1. Extraction – Fetches raw trip data from Google Cloud Storage
2. Transformation – Uses Python (Pandas, NumPy) to clean and preprocess the data
3. Loading – Inserts processed data into BigQuery tables

<img width="600" src="https://github.com/MK9ei82/Uber-Rides-Analytics/blob/main/misc/Uber_Rides_Data_Pipeline.png"/>

# Sample Queries
After the data has been loaded into BigQuery data warehouse sample queries have been run to interpret the results.

<img width="600" src="https://github.com/MK9ei82/Uber-Rides-Analytics/blob/main/misc/sample_query_execution.png"/>

## Top 10 Pickup Locations

<img width="300" src="https://github.com/MK9ei82/Uber-Rides-Analytics/blob/main/misc/top_10_pickup_locs.png"/>

Insight: Identifies the busiest pickup locations, which can help optimize driver allocation.


# Looker BI Dashboard
Developed a interactive dashboard that shows key metrics and a map that shows the distribution of ride pickup locations. Various parameters such as trip distance, payment type, rate code and vendor ID can be selected to show corresponding visualizations.

The interactive dashboard enables stakeholders to:
✔ Analyze trip frequency by time of day
✔ Compare cash vs. credit card payments
✔ Identify high-demand ride locations

 Live Dashboard: https://lookerstudio.google.com/reporting/d7c0b966-5359-4dd0-95e0-6104e4f48af1/page/RtbuE
 
<img width="600" src="https://github.com/MK9ei82/Uber-Rides-Analytics/blob/main/misc/Interactive_Dashboard.png"/>

Shows visualization for key metrics and pickup location bubbles for cash payments.

<img width="600" src="https://github.com/MK9ei82/Uber-Rides-Analytics/blob/main/misc/cash_dashboard.png"/>

Shows visualization for key metrics and pickup location bubbles for credit card payments and rate code is JFK.

<img width="600" src="https://github.com/MK9ei82/Uber-Rides-Analytics/blob/main/misc/credit_card_and_jfk.png"/>

Various Bar charts employing different metrics

<img width="600" src="https://github.com/MK9ei82/Uber-Rides-Analytics/blob/main/misc/Bar%20charts%20employing%20various%20metrics.png"/>

