import argparse
import sys
import time

import pandas as pd
import parse_default_tass
import yaml


def apply_config():
    parser = create_parser()
    agr = parser.parse_args(sys.argv[1:])
    return read_yaml(agr.config)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default='old_config.yaml')

    return parser


def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


def read_old_data(old_data: str):
    return pd.read_csv(old_data)


# пока что id не получаем
def get_last_id():
    return 14269307


def get_index_first_new_article(data, last_id):
    return data.loc[data['id'] == last_id].index[0]


def get_new_data(data, last_id):
    index = get_index_first_new_article(data, last_id)
    new_articles = data.iloc[:index]

    return new_articles


# перезаписываем файл полностью, так как при попытке дописать новые
# строки в старый файл происходит путаница в порядке строк

# исправить индексацию
def save_new_data(new_articles, path):
    data = read_old_data(path)
    all_data = pd.concat([data, new_articles], ignore_index=True)
    # all_data = data.append(new_articles)
    all_data.to_csv(path, encoding='utf-8')


if __name__ == '__main__':
    config = apply_config()

    while True:
        response_news = parse_default_tass.Response(base_url=config['WEB INTERFACE']['BASE_URL'],
                                                    headers=config['WEB INTERFACE']['HEADERS'],
                                                    params=config['WEB INTERFACE']['PARAMS'])
        data_news = response_news.get_data()

        ready_data = response_news.work_with_datsaframe(data_news, config['WEB INTERFACE']['FIELDS'])

        path_old_data = config['DATA_FILE']
        last_id = get_last_id()
        new_articles = get_new_data(ready_data, last_id)
        print('NEW ARTICLE')
        print(new_articles[['id', 'title']])

        save_new_data(new_articles, path_old_data)
        # response_news.print_results(ready_data)

        time.sleep(10)
