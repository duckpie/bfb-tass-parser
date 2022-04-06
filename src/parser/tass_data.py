import json
import time
from typing import Optional

import pandas as pd
import requests
from requests import Response


class TassData():
    def __init__(self, base_url: str, headers: dict, params: dict, fields: list, proxies: str = None, ) -> None:
        self._base_url = base_url
        self._headers = headers
        self._params = params
        self._fields = fields
        self._proxies = proxies

    def get_articles(self) -> pd.DataFrame:
        response = self.make_requests()
        data = self.transform_response_to_data(response)
        return data

    def make_requests(self) -> Optional[Response]:
        c = 0
        while (c < 5):
            response = self._make_single_request()
            if self._check_status_code(response):
                return response
            c += 1
            time.sleep(c)
        return None

    def _make_single_request(self) -> Optional[Response]:
        try:
            data = json.dumps(self._params)

            response = requests.post(self._base_url,
                                     headers=self._headers,
                                     data=data,
                                     timeout=3,
                                     proxies=self._proxies
                                     )
            return response
        except:
            return None

    def _check_status_code(self, response: Response) -> bool:
        if response.status_code == 200:
            print('Done')
            return True

        else:
            print(response)
            return False

    def transform_response_to_data(self, response: Response) -> pd.DataFrame:
        data_dict = self._formating_json(response)
        df = self._transform_to_dataframe(data_dict)
        clean_data = self._leave_required_fields_only(df)
        return clean_data

    def _formating_json(self, response: Response) -> Optional[dict]:
        try:
            data_dict = json.loads(response.text.encode())
            return data_dict
        except:
            return None

    def _transform_to_dataframe(self, data_dict: dict) -> pd.DataFrame:
        NAME_TAG = 'newsList'
        data = pd.DataFrame(data_dict[NAME_TAG])
        return data

    def _leave_required_fields_only(self, data: pd.DataFrame) -> pd.DataFrame:
        return data[self._fields]

    # нет метода сохранения
    def save_articles(self) -> bool:
        pass

    def get_url(self) -> str:
        return self._base_url

    def get_params(self) -> dict:
        return self._params

    def get_fields(self) -> list:
        return self._fields

    def get_headers(self) -> dict:
        return self._headers
