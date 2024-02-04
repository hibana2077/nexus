'''
Author: hibana2077 hibana2077@gmail.com
Date: 2024-02-02 15:25:19
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-02-02 15:42:33
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