from scr.config import Config, ParserConfig, ServerConfig, RedisConfig

parser = RedisConfig('local')
res = parser.port
print(type(res))
print(res)
