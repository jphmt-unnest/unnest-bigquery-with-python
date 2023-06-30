from google.cloud import bigquery
    
def create_table(project_id, schema_name, table_name):
    bq_client = bigquery.Client(project=project_id)
    
    # schema (dataset) creation
    # Ref : https://cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client#google_cloud_bigquery_client_Client_create_dataset
    dataset_ref=f"{project_id}.{schema_name}"
    dataset = bigquery.Dataset(dataset_ref=dataset_ref)
    bq_client.create_dataset(dataset=dataset)
    
    # table creation
    # Ref : https://cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.table.Table
    table_id = f"{project_id}.{schema_name}.{table_name}"
    schema_table = [
        bigquery.SchemaField("full_name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
    ]
    table_obj = bigquery.Table(table_ref=table_id, schema=schema_table)
    table = bq_client.create_table(table_obj)
    print(
        "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
    )
    
def main():
    PROJECT_ID="random-unnest"
    SCHEMA_NAME="training_jimmy"
    TABLE_NAME="table_from_python"
    create_table(project_id=PROJECT_ID, schema_name=SCHEMA_NAME, table_name=TABLE_NAME)
    

if __name__ == "__main__":
    main()