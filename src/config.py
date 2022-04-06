import yaml


class Config(object):
    def __init__(self, env: str) -> None:
        with open(f'config/config.{env}.yaml', 'r') as f:
            self._config = yaml.safe_load(f)

    def get_property(self, property_name: str) -> dict:
        return self._config[property_name]


class ServicersConfig(Config):
    def __init__(self, env: str) -> None:
        super().__init__(env)
        self._services_config = self.get_property('services')

    def get_services_property(self, property_name: str) -> dict:
        return self._services_config[property_name]


class ParserConfig(ServicersConfig):
    def __init__(self, env: str) -> None:
        super().__init__(env)
        self._parser_config = self.get_services_property('parser')

    def get_parser_property(self, property_name: str):
        return self._parser_config[property_name]

    @property
    def ulr(self) -> str:
        return self.get_parser_property('url')

    @property
    def headers(self) -> dict:
        return self.get_parser_property('headers')

    @property
    def params(self) -> dict:
        return self.get_parser_property('params')

    @property
    def fields(self) -> list:
        return self.get_parser_property('fields')


class ServerConfig(ServicersConfig):
    def __init__(self, env: str) -> None:
        super().__init__(env)
        self._server_config = self.get_services_property('server')

    def get_server_property(self, property_name: str):
        return self._server_config[property_name]

    @property
    def host(self) -> str:
        return self.get_server_property('host')

    @property
    def port(self) -> int:
        return self.get_server_property('port')


class RedisConfig(ServicersConfig):
    def __init__(self, env: str) -> None:
        super().__init__(env)
        self._redis_config = self.get_services_property('redis')

    def get_redis_property(self, property_name: str):
        return self._redis_config[property_name]

    @property
    def host(self) -> str:
        return self.get_redis_property('host')

    @property
    def port(self) -> int:
        return self.get_redis_property('port')

    @property
    def db(self) -> int:
        return self.get_redis_property('db')
