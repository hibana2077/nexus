'''
Author: hibana2077 hibana2077@gmail.com
Date: 2024-02-02 15:25:19
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-02-04 17:24:20
FilePath: /stock/fugle.py
Description: This is a simple Python wrapper for the Fugle API.
'''
import requests

class Fugle:
    def __init__(self, token):
        """
        Initialize the Fugle class.

        Args:
            token (str): The API token for authentication.

        Attributes:
            token (str): The API token for authentication.
            headers (dict): The headers for API requests.
            base_url (str): The base URL for API requests.
        """
        self.token = token
        self.headers = {
            'Content-Type': 'application/json',
            'X-API-KEY': token
        }
        self.base_url = 'https://api.fugle.tw/marketdata/v1.0/stock/intraday/tickers?type=EQUITY&exchange=TWSE'
        self.index_url = 'https://api.fugle.tw/marketdata/v1.0/stock/intraday/tickers?type=INDEX&exchange=TWSE'

    def get_all_tickers(self):
        """
        Get all tickers from the Fugle API.

        Returns:
            list: A list of tickers in the format [{ticker: '2330', name: '台積電'}, ...]
        """
        response = requests.get(self.base_url, headers=self.headers)
        if response.status_code != 200:
            return []
        return response.json()['data']

    def get_all_index(self):
        """
        Get all index from the Fugle API.

        Returns:
            list: A list of index in the format [{ticker: 'IX0001', name: '台灣50指數'}, ...]
        """
        response = requests.get(self.index_url, headers=self.headers)
        if response.status_code != 200:
            return []
        return response.json()['data']

    def get_trade_rank(self,trade:str):
        """
        Get trade rank from the Fugle API.

        Args:
            trade (str): The trade to filter the trade rank.

        Returns:
            list: A list of trade rank data.
        """
        base_url = "https://api.fugle.tw/marketdata/v1.0/stock/snapshot/actives/TSE?trade={}".format(trade)
        response = requests.get(base_url, headers=self.headers)
        if response.status_code == 403:
            return "Your Subscription Plan does not support this API endpoint."
        elif response.status_code != 200:
            return []
        return response.json()['data']
    
    def get_index_price(self):
        """
        Get the price of the TAIEX index.

        Returns:
            float: The price of the TAIEX index.
        """
        base_url = "https://api.fugle.tw/marketdata/v1.0/stock/intraday/candles/{}"
        temp_data = {}
        map_data = {'IX0175': '特選臺灣產業龍頭存股等權重指數', 'IX0001': '發行量加權股價指數', 'IX0125': '智慧中立指數', 'IX0160': '臺灣優息存股指數'}
        query_symbol_list = map_data.keys()
        for symbol in query_symbol_list:
            response = requests.get(base_url.format(symbol), headers=self.headers)
            if response.status_code != 200:
                return []
            temp_data[map_data[symbol]] = response.json()['data']
        return temp_data