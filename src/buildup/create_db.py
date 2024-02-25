import sqlite3
import os

# Define the path for the database
db_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'specimens.db')

# Connect to or create the SQLite database at the specified path
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Create a new table
c.execute('''
CREATE TABLE IF NOT EXISTS specimens (
    id INTEGER PRIMARY KEY,
    chinese_name TEXT, -- Chinese common name
    scientific_name TEXT, -- Scientific name
    museum_number TEXT, -- Museum number
    catalog_number TEXT, -- Catalog number
    reference TEXT, -- Reference
    collection_date TEXT, -- Collection date
    collector TEXT, -- Collector
    latitude REAL, -- Latitude
    longitude REAL, -- Longitude
    country TEXT, -- Country
    administrative_region TEXT, -- Administrative region
    minimum_elevation REAL, -- Minimum elevation
    image_url TEXT -- Image URL
)
''')

# Commit the operation of creating table
conn.commit()

# Close the connection
conn.close()
