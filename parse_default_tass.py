import json
import sys

import pandas as pd
import requests
import yaml

import argparse

def apply_config():
    parser = create_parser()
    agr = parser.parse_args(sys.argv[1:])
    return read_yaml(agr.config)

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default='config.yaml')

    return parser

def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


class Response():
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        # self.params = params



    def make_a_request(self):
        try:
            return self._make_a_request()
        except:
            return None

    def _make_a_request(self):
        # response = requests.get(self.base_url, headers=self.headers,params=self.params)
        response = requests.get(self.base_url, headers=self.headers)
        return response

    def json_formating(self,response):
        try:
            return self._json_formating(response)
        except:
            return None

    def _json_formating(self,response):
        return json.loads(response.text.encode())


    def check_status_code(self,response):
        if response.status_code == 200:
            print('Done')
            return True

        else:
            print(response)
            print('ERROR: API call failed.')
            return False

    def get_request_retry(self):
        t = True
        c = 0
        while t and (c<10):
            response = self.make_a_request()
            if self.check_status_code(response):
                t = False
            c+=1

        return response

    def get_data(self):
        response = self.get_request_retry()
        results = self.json_formating(response)
        return results

    def work_with_datsaframe(self,results,fields):
        data = self.to_dataframe(results)
        return self.leave_the_required_fields_only(data,fields)

    def to_dataframe(self,results):
        data = pd.DataFrame(results['newsList'])
        return data

    def leave_the_required_fields_only(self,data,fields):
        return data[fields]

    def save_data(self,important_data):
        important_data.to_csv('tass_titles.csv', encoding='utf-8')
        print('File saved successfully!')

    def print_results(self,important_data):
        print('News table:')
        print(important_data)




if __name__ == '__main__':

    config = apply_config()

    response_news = Response(base_url=config['WEB INTERFACE']['BASE_URL'],
                             headers=config['WEB INTERFACE']['HEADERS'])
    data_news = response_news.get_data()

    ready_data = response_news.work_with_datsaframe(data_news,config['WEB INTERFACE']['FIELDS'])

    # response_news.print_results(ready_data)

    response_news.save_data(ready_data)
