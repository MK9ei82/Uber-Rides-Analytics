# Access The Dashboard Here:
https://lookerstudio.google.com/reporting/d7c0b966-5359-4dd0-95e0-6104e4f48af1/page/RtbuE

# Uber-Rides-Analytics on GCP
This project analyzes Uber ride data to uncover trends, peak usage times, and other insights that can help improve ride allocation and pricing strategies.

# Data Pipeline Architecture
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
Created a data pipeline in Mage AI which orchestrates extract, transform and load functions. The data is sourced from Google Cloud Storage, transformed using Python and libraries, loaded into BigQuery data warehouse. 

<img width="600" src="https://github.com/MK9ei82/Uber-Rides-Analytics/blob/main/misc/Uber_Rides_Data_Pipeline.png"/>

# Sample Queries
After the data has been loaded into BigQuery data warehouse sample queries have been run to interpret the results.

<img width="600" src="https://github.com/MK9ei82/Uber-Rides-Analytics/blob/main/misc/sample_query_execution.png"/>
<img width="300" src="https://github.com/MK9ei82/Uber-Rides-Analytics/blob/main/misc/top_10_pickup_locs.png"/>


# Looker BI Dashboard
Developed a interactive dashboard that shows key metrics and a map that shows the distribution of ride pickup locations. Various parameters such as trip distance, payment type, rate code and vendor ID can be selected to show corresponding visualizations.

<img width="600" src="https://github.com/MK9ei82/Uber-Rides-Analytics/blob/main/misc/Interactive_Dashboard.png"/>

Shows visualization for key metrics and pickup location bubbles for cash payments.

<img width="600" src="https://github.com/MK9ei82/Uber-Rides-Analytics/blob/main/misc/cash_dashboard.png"/>

Shows visualization for key metrics and pickup location bubbles for credit card payments and rate code is JFK.

<img width="600" src="https://github.com/MK9ei82/Uber-Rides-Analytics/blob/main/misc/credit_card_and_jfk.png"/>

Various Bar charts employing different metrics

<img width="600" src="https://github.com/MK9ei82/Uber-Rides-Analytics/blob/main/misc/Bar%20charts%20employing%20various%20metrics.png"/>

