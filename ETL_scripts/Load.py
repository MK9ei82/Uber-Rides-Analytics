from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    table_id_prefix = 'uber-ride-analytics.uber_rides_data'  # Common prefix
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'
    bq = BigQuery.with_config(ConfigFileLoader(config_path, config_profile)) # Initialize BigQuery client outside the loop

    for key, value in data.items():
        table_id = f"{table_id_prefix}.{key}"  # Construct table ID dynamically

        try:
            bq.export(  # Use the pre-initialized BigQuery client
                DataFrame(value),
                table_id,
                if_exists='replace',
            )
            print(f"Successfully exported {key} to {table_id}")
        except Exception as e:
            print(f"Error exporting {key}: {e}") #Print full error for debugging