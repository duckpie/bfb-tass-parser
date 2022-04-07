import redis

from src.config import Config, ParserConfig, ServerConfig, RedisConfig,ServicersConfig
from src.parser.tass_data import TassData



if __name__ == '__main__':
    # конфиг читается за 1 раз

    redis_conf = RedisConfig('local')

    r = redis.Redis(
        host=redis_conf.host,
        port=redis_conf.port,
        db=redis_conf.db
    )

    parser = ParserConfig('local')



    response_news = TassData(base_url=parser.ulr,
                             headers=parser.headers,
                             params=parser.params,
                             fields=parser.fields,
                             redis=r)

    res = response_news.get_articles()
    response_news.save_articles(res)
    # print(res)



