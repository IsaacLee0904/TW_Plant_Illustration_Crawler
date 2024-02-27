import json
import os
import datetime
from pandas import DataFrame
import sqlite3

def save_data_to_json(data):
    """
    Saves the extracted data to a JSON file with a filename based on the current date and time.
    
    Args:
        data (list): A list of dictionaries containing the extracted data.
    """
    # Get the path to the project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Build the path to the 'data' directory
    data_dir = os.path.join(project_root, 'data')
    
    # Ensure the 'data' directory exists
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Generate the filename based on the current date and time
    currentDT = datetime.datetime.now()
    filename = currentDT.strftime("%Y%m%d%H%M%S_") + "Plant.json"
    print('[Crawler Start]', "\n" + filename)

    # Here is the fix: Construct the full file path
    filepath = os.path.join(data_dir, filename)  # This line was missing in your original code

    # Write the data to the JSON file
    with open(filepath, 'w', encoding='utf-8') as json_file:  # Now 'filepath' is correctly defined
        for item in data:
            # Convert each item to a JSON string and write it to the file
            line = json.dumps(item, ensure_ascii=False) + "\n"
            json_file.write(line)
    
    print('[Crawler End]')

def split_col_value(df, columns):
    """
    Splits the value of specified columns at the first occurrence of ':' and keeps the part after it.
    
    Args:
        df (pd.DataFrame): The DataFrame containing the columns to be processed.
        columns (list of str): A list of column names in the DataFrame to be split and processed.
    """
    for col in columns:
        df[col] = df[col].str.split(':').str.get(1)

def reshape_df(df):
    """
    Reorganize the DataFrame based on specified column order.

    Parameters:
    - df: The input DataFrame to be reshaped.

    Returns:
    - A new DataFrame reorganized based on the specified column order.
    """
    column_order = ['chinese_name', 'scientific_name', 'museum_number', 'catalog_number',
                    'reference', 'collection_date', 'collector',
                    'latitude', 'longitude', 'country', 'administrative_region',
                    'minimum_elevation', 'image_url']
    
    for column in column_order:
        if column not in df.columns:
            raise ValueError(f"Column '{column}' is not in the DataFrame")
    
    reshaped_df = df[column_order].copy()
    
    return reshaped_df

def insert_into_db(df: DataFrame, db_path: str):
    """
    Inserts data from a DataFrame into a SQLite database.

    Parameters:
    - df: DataFrame containing the data to be inserted.
    - db_path: The path to the SQLite database file.

    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    table_name = 'specimens'
    
    df.to_sql(table_name, conn, if_exists='append', index=False)
    
    conn.commit()
    conn.close()
    
    print(f"Data inserted into '{table_name}' table successfully.")