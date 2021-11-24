# -*- coding: utf-8 -*-
"""
Convert JSON to CSV

@author: Ethan O'Sullivan <ethan.osullivan@anheuser-busch.com>
"""

import os, json, ijson, pandas, csv
from flatten_json import flatten

# Enter the path to the JSON and the filename without appending '.json'
file_path = r'C:\Path\To\JSON Folder'
# Extract data from the defined key names
key_list = ['created', 'data', 'emails', 'isRegistered', 'isVerified', 'regSource', 'profile']
# Key names to ignore separated by a vertical bar '|'
key_ignore = 'parent_key|key_list.child_key1|key_list.child_key2'

# Calculate file size in GB
file_size_gb = round(os.stat(file_path + '.json').st_size / 1024 ** 3, 2)

def convert_to_csv(key_list, key_ignore, json_data):
    json_data = [{key:data[key] for key in key_list} for data in json_data]
    # Flatten and convert to a data frame
    json_data_flattened = (flatten(d, '.') for d in json_data)
    df = pandas.DataFrame(json_data_flattened)
    # Drop unwanted columns
    df.drop(df.filter(regex=key_ignore).columns, axis=1, inplace=True)
    # Export to CSV in the same directory with the original file name
    df.to_csv(file_path + '.csv', sep=',', encoding='utf-8', index=None, header=True)

if file_size_gb < 1:
    print("JSON file is less than 1GB. Performing method #1.")
    json_data = json.load(open(file_path + '.json', 'r', encoding='utf-8', errors='ignore'))
    convert_to_csv(key_list, key_ignore, json_data)
else:
    print(f"JSON file is {file_size_gb}GB. Performing method #2.")
    """
    with open(file_path + '.json', 'rb') as json_file:
        json_data = ijson.items(json_file, 'item')
        convert_to_csv(key_list, key_ignore, json_data)
    """

"""
from copy import deepcopy
import json, pandas

def cross_join(left, right):
    new_rows = []
    for left_row in left:
        for right_row in right:
            temp_row = deepcopy(left_row)
            for key, value in right_row.items():
                temp_row[key] = value
            new_rows.append(deepcopy(temp_row))
    return new_rows

def flatten_list(data):
    for elem in data:
        if isinstance(elem, list):
            yield from flatten_list(elem)
        else:
            yield elem

def json_to_dataframe(data_in):
    def flatten_json(data, prev_heading=''):
        if isinstance(data, dict):
            rows = [{}]
            for key, value in data.items():
                rows = cross_join(rows, flatten_json(value, prev_heading + '.' + key))
        elif isinstance(data, list):
            rows = []
            for i in range(len(data)):
                [rows.append(elem) for elem in flatten_list(flatten_json(data[i], prev_heading))]
        else:
            rows = [{prev_heading[1:]: data}]
        return rows

    return pandas.DataFrame(flatten_json(data_in))

if __name__ == '__main__':
    file_path = r'C:\Users\Y931039\OneDrive - Anheuser-Busch InBev\My Documents\Data Sources\Gigya\gigya'
    json_data = json.load(open(file_path + '.json', 'r', encoding='utf-8', errors='ignore'))
    df = json_to_dataframe(json_data)
    df.drop(df.filter(regex='identities|userInfo').columns, axis=1, inplace=True)
    df.to_csv(file_path + '.csv', sep=',', encoding='utf-8', index=None, header=True)
  """
