import os
import json

def main():
    input_paths = os.environ.get('INPUT_PATHS')
    print ("input_paths: ", input_paths)
    output_folder = os.environ.get('OUTPUT_FOLDER')
    print ("output_folder: ", output_folder)
    if input_paths:
        with open(input_paths, 'r') as file:
            input_paths_json = file.read()
            if input_paths_json:
                data = json.loads(input_paths_json)
                if data:
                    filtered_data = []
                    for url, item in data.items():  # Iterate over keys and values
                        year_start = item.get('year_start', None)
                        year_end = item.get('year_end', None)
                        if year_start is not None and year_end is not None:
                            # Convert year strings to integers for comparison
                            year_start = int(year_start)
                            year_end = int(year_end)
                            if year_start > 2010 and year_end < 2030:
                                filtered_data.append({url: item})  # Append the whole item
                    with open(f"{output_folder}/filtered_data.json", 'w') as file:
                        json.dump(filtered_data, file)  # Use json.dump to write the list of dicts
                else:
                    print("Error: Input paths list is empty.")
            else:
                print("Error: INPUT_PATHS environment variable is not set or empty.")

if __name__ == "__main__":
    main()
