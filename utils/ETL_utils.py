import json
import os
import datetime

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
