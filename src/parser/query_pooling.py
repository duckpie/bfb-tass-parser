import argparse
import sys
import time

import pandas as pd
from src.parser import parse_default_tass
import yaml
from csv import writer
import redis


def connect_redis():
    return redis.Redis()

def activate_parser():
    parser = create_parser()
    agr = parser.parse_args(sys.argv[1:])
    return agr


def apply_config():
    agr = activate_parser()
    return read_yaml(agr.config)

def apply_time():
    agr = activate_parser()
    return int(agr.time)

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default='config.local.yaml')
    parser.add_argument('-t', '--time', default=600)

    return parser


def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


def read_old_data(old_data: str):
    return pd.read_csv(old_data)


def get_index_last_data(data):
    try:
        return int(data.iloc[0]['id'])
    except:
        return None


def set_last_id(db, data):
    last_id = get_index_last_data(data)
    print(f'Last id is {last_id}')
    db.set(last_id, last_id)


def get_last_id(db):
    try:
        return int(db.get('id').decode("utf-8"))
    except:
        return 14279053


def get_index_first_new_article(data, last_id):
    try:
        return data.loc[data['id'] == last_id].index[0]
    except:
        return None


def get_new_data(data, last_id):
    index = get_index_first_new_article(data, last_id)
    try:
        new_articles = data.iloc[:index]
    except:
        new_articles = data

    return new_articles


def save_new_data(new_articles, path):
    for line in range(len(new_articles.index) - 1, -1, -1):
        one_new_article = new_articles.iloc[line,].tolist()

        with open(path, 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(one_new_article)


if __name__ == '__main__':
    config = apply_config()
    db = connect_redis()


    while True:
        response_news = parse_default_tass.Response(base_url=config['WEB INTERFACE']['BASE_URL'],
                                                    headers=config['WEB INTERFACE']['HEADERS'],
                                                    params=config['WEB INTERFACE']['PARAMS'])
        data_news = response_news.get_data()

        ready_data = response_news.work_with_datsaframe(data_news, config['WEB INTERFACE']['FIELDS'])

        path_old_data = config['DATA_FILE']
        last_id = get_last_id(db)
        new_articles = get_new_data(ready_data, last_id)
        # print('NEW ARTICLE')
        # print(new_articles[['id', 'title']])

        save_new_data(new_articles, path_old_data)

        set_last_id(db, ready_data)

        time.sleep(apply_time())
