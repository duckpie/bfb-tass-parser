import argparse
import sys

import requests
import yaml


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


if __name__ == '__main__':


    config = apply_config()


    proxies = {'http':'77.236.237.241:1256',
               'https': '178.167.66.141:55443'
               }
    session = requests.Session()
    session.proxies = proxies

    # response = session.post('https://tass.ru/userApi/getNewsFeed',
    #             headers=config['WEB INTERFACE']['HEADERS'],
    #                        timeout=3
    #             )

    response = requests.post('https://tass.ru/userApi/getNewsFeed',
                            headers=config['WEB INTERFACE']['HEADERS'],
                            timeout=3,proxies=proxies)
    print(response)
