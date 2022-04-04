import json
import sys
import time

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
    def __init__(self, base_url, headers, params):
        self.base_url = base_url
        self.headers = headers
        self.params = params

    def make_request(self):
        try:
            return self._make_request()
        except:
            return None

    def _make_request(self):

        proxies = {
            'http': 'http://10.10.1.10:3128',
            'https': 'http://10.10.1.10:1080',
        }

        # print(self.params)
        response = requests.post(self.base_url,
                                 headers=self.headers,
                                 # data=self.params,
                                 # proxies=proxies
                                 )
        return response

    def json_formating(self, response):
        try:
            return self._json_formating(response)
        except:
            return None

    def _json_formating(self, response):
        return json.loads(response.text.encode())

    def check_status_code(self, response):
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
        while t and (c < 5):
            response = self.make_request()
            if self.check_status_code(response):
                t = False
            c += 1
            time.sleep(c)

        return response

    def get_data(self):
        response = self.get_request_retry()
        results = self.json_formating(response)
        return results

    def work_with_datsaframe(self, results, fields):
        data = self.to_dataframe(results)
        return self.leave_required_fields_only(data, fields)

    def to_dataframe(self, results):
        data = pd.DataFrame(results['newsList'])
        return data

    def leave_required_fields_only(self, data, fields):
        return data[fields]

    def save_data(self, important_data, path):
        important_data.to_csv(path, encoding='utf-8')
        print('File saved successfully!')

    def print_results(self, important_data):
        print('News table:')
        print(important_data)


if __name__ == '__main__':
    config = apply_config()

    response_news = Response(base_url=config['WEB INTERFACE']['BASE_URL'],
                             headers=config['WEB INTERFACE']['HEADERS'],
                             params=config['WEB INTERFACE']['PARAMS'])
    data_news = response_news.get_data()

    ready_data = response_news.work_with_datsaframe(data_news, config['WEB INTERFACE']['FIELDS'])

    response_news.print_results(ready_data)

    response_news.save_data(ready_data, config['DATA_FILE'])
