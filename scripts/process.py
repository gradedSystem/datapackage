# -*- coding: utf-8 -*-

import os
import csv
from io import StringIO
import urllib.request
import requests
import pandas as pd
from config import api_key
from requests.exceptions import HTTPError

# Option 1:
data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                         '..', 'archive')
source = 'http://ourairports.com/data/airports.csv'
archive = os.path.join(data_folder, 'source.csv')

# Option 2:
API_URL = "https://api.eia.gov/v2/natural-gas/pri/fut/data/"

# Folder path of an archive
data_csv_path = os.path.join('archive', 'source.csv')

# Parameters of an API
params = {
    'api_key': api_key,
    'frequency': 'daily',
    'data[0]': 'value',
    'facets[series][]': 'RNGWHHD',
    'sort[0][column]': 'period',
    'sort[0][direction]': 'desc',
    'offset': 0,
    'length': 5000
}

def url_retrieve(url, destination):
    try:
        if not os.path.exists(destination):
            os.makedirs(destination)
        response = urllib.request.urlretrieve(url, 
                                              os.path.join(destination,
                                                            'source.csv'))
        print("Downloaded data successfully!")
    except Exception as err:
        print(f"Error occurred while downloading data: {err}")

def api_retrieve(url, destination):
    try:
        response = requests.get(url, params=params)
        content_type = response.headers.get('Content-Type')
        if 'json' in content_type:
            file_extension = 'json'
        elif 'csv' in content_type:
            file_extension = 'csv'
        else:
            file_extension = 'txt'
        data_api_filename = os.path.join(destination, 
                                         f'data_api.{file_extension}')
        with open(data_api_filename, 'wb') as file:
            file.write(response.content)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f"Other error occurred: {err}")
    else:
        print("Success!")

def clean_and_prepare(file):
    """
    1)
        Read CSV and create separate .md file for comments
    2)  
        data files have no empty rows
    3)
        Using separator as "." instead of ",".
    4)
        Replace None values with "0" and drop rows with empty cells
    5)
        Unpivot the csv table by "id" variable.
    """
    # 1) Drop the comments and create separate .md file for comments
    # Define the character used for comments (e.g., '#')
    comment_character = '#'

    # Initialize variables to store data and comments
    data_lines = []
    comment_lines = []

    # Read the data file and separate data from comments
    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith(comment_character):
                comment_lines.append(line)
            else:
                data_lines.append(line)
    
    # Write the comments to a Markdown file
    with open('comments.md', 'w') as comments_file:
        comments_file.writelines("# Removed comments: \n")
        comments_file.writelines(comment_lines)
    
    # Parse the data without comments as a CSV to create a DataFrame
    data_string = ''.join(data_lines)
    
    df = pd.read_csv(StringIO(data_string));
    
    # 2) Remove empty rows
    df = df.dropna(how='all')
    
    # 3) Use separator as "." instead of ","
    for col in df.columns:
        df[col] = df[col].replace({',': '.'}, regex=True)

    # 4) Replace None values with "0"
    df = df.fillna(0)  

    # 5) Unpivot the data
    col_df = list(df.columns.values)
    df = pd.melt(df,id_vars = col_df[0], 
                 value_vars = col_df[1:], ignore_index=False)
    
    # Save CSV into data folder
    data_folder_path = 'data/'  # Specify the path to the 'data' folder
    out_csv_path = data_folder_path + 'data.csv'
    df.to_csv(out_csv_path, index=False)
    


def main():
    url_retrieve(source, data_folder)
    api_retrieve(API_URL, data_folder)
    clean_and_prepare(data_csv_path)

if __name__ == "__main__":
    main()
