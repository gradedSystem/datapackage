# -*- coding: utf-8 -*-

import os
import urllib.request
import requests
from config import api_key
from requests.exceptions import HTTPError

# Option 1:
data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                         '..', 'data')
source = 'http://ourairports.com/data/airports.csv'
archive = os.path.join(data_folder, 'data.csv')

# Option 2:
API_URL = "https://api.eia.gov/v2/natural-gas/pri/fut/data/"

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
                                                            'data.csv'))
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

def main():
    url_retrieve(source, data_folder)
    api_retrieve(API_URL, data_folder)

if __name__ == "__main__":
    main()
