# remake query_pooling


class TassParser():
    def __init__(self, url: str, time_limit: int, records: int):
        self.url = url
        self.time_limit = time_limit
        self.records = records

    async def get_data(self) -> tuple[list[TassData], error]:
        pass

    def save_data(data: list[TassData]) -> error:
        pass

    def notify(new_ids: list[int]) -> error:
        pass



    def get_list_of_new_ids(self):
        # возвращаем приватную переменную, которую запоминаем при сохранении новых статей
        pass


    def download_new_articles(self):
        self.get_articles(self)

        get_new_articles()

        save_new_articles()
        ids = get_list_of_new_ids()
        return ids