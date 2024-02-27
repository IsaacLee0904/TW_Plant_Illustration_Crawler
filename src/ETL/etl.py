import json 
import os
import sys
import pandas as pd


### import modules
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)
from utils.ETL_utils import split_col_value, reshape_df, insert_into_db

# load the data
def load_data():

    json_file_path = 'data/20240226134932_Plant.json'
    df = pd.read_json(json_file_path, lines=True)

    return df

def data_cleaning(df):

    columns_to_process = [
        'chinese_name', 'scientific_name', 'museum_number', 'catalog_number',
        'collection_date', 'collector_chinese', 'collector_Eng', 'latitude',
        'longitude', 'country', 'administrative_region', 'minimum_elevation'
    ]


    split_col_value(df, columns_to_process)
    df['collector'] = df.apply(lambda row: f"{row['collector_chinese']}({row['collector_Eng']})", axis=1)

    return df

def main():
    df = load_data()
    data_cleaning(df)
    new_df = reshape_df(df)
    insert_into_db(new_df, 'data/specimens.db')

if __name__ == "__main__":
    main()  