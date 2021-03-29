from google.cloud import bigquery
import logging
import csv

def bq_db(records):
    project_id = 'avid-glass' 
    table_id = 'houses.features'
    client  = bigquery.Client(project = project_id)
    table = client.get_table(table_id)
    list_items = []
    for i in range(10): #Trasnfer 10 rows from mysqldb to bigquery
        processed_item = {
                    'name_id': records[i]['name_id'],
                    'id': records[i]['id'],
                    'data': records[i]['date'],
                    'price': records[i]['price'],
                    'grade': records[i]['grade'],
                    'bedrooms': records[i]['bedrooms'],
                    'bathrooms': records[i]['bathrooms'],
                    'floors': records[i]['floors'],
                    'waterfront': records[i]['waterfront'],
                    'yr_built': records[i]['yr_built'],
                    'condition_house': records[i]['condition_house']
                }
        list_items.append(processed_item)

    error = client.insert_rows(table, list_items) #if everything works, returns an empty list
    if error:
        logging.exception(f'BigQueryException: {error}')
    else:
        print('Data Transfered Successfully')
