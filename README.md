# Convert JSON to CSV in Python
This Python code helps convert several individual JSON files, locally, into one CSV. Additionally, this code allows the user to cherry-pick the field names from the JSON dataset.

## How to Use the Code
To run the code and get the expected output, use the following steps:

1. Compile all JSON files into one folder, locally.
    - Note: there shouldn't be any other file types or sub-folders
1. Open the Python script in your IDE.
1. Set up the following variables based on your preferences:
    - `file_path`: Enter the path to the JSON and the filename without appending `.json`
    - `key_list`: Extract data from the defined key names
    - `key_ignore`: Key names to ignore separated by a vertical bar (`|`)
