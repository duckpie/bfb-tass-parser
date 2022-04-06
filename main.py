from src.config import Config, ParserConfig, ServerConfig, RedisConfig
from src.parser.tass_data import TassData
parser = ParserConfig('local')
res = parser.ulr
print(type(res))
print(res)


response_news = TassData(base_url=parser.ulr,
                         headers=parser.headers,
                         params=parser.params,
                         fields=parser.fields)

res = response_news.get_articles()
print(res)



