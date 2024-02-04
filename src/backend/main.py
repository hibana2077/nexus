'''
Author: hibana2077 hibana2077@gmail.com
Date: 2024-02-02 17:41:30
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-02-04 17:59:22
FilePath: /nexus/src/backend/main.py
Description: This is a FastAPI application that uses the Fugle API to get stock information.
'''
from fastapi import FastAPI
from fugle import Fugle
import yfinance as yf
import pandas as pd
import info

API_TOKEN = 'MTJiNTVmYzgtYThlNC00MjAyLWFlYzAtMDBhMzMzMGVhMTZiIGYwODA4MzFiLTQxNzMtNDMzOC1hZDgyLTFkYzJkZGUwNmZhOA=='

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/tickers")
async def tickers():
    """
    Get all tickers from the Fugle API.

    Returns:
        list: A list of tickers in the format [{ticker: '2330', name: '台積電'}, ...]
    """
    client = Fugle(API_TOKEN)
    return client.get_all_tickers()

@app.get("/stock/{stock}")
async def stock(stock:str):
    """
    Get stock information from Yahoo Finance.

    Args:
        stock (str): The stock symbol.

    Returns:
        dict: A dictionary containing the stock information.
            - stock_name (str): The name of the stock.
            - stock_num (str): The stock number.
            - stock_class (str): The stock class.
            - bookValue (float): The book value of the stock.
            - priceToBook (float): The price-to-book ratio of the stock.
    """
    return info.get_stock_info(stock)

@app.get("/mainpage/indexprice")
async def indexprice():
    """
    Get the price of the TAIEX index.

    Returns:
        float: The price of the TAIEX index.
    """
    client = Fugle(API_TOKEN)
    temp_data = {k:v[:180] for k,v in client.get_index_price().items()}
    return_list = list()
    for k,v in temp_data.items():
        for i in v:
            i.pop('open')
            i.pop('high')
            i.pop('low')
            i.pop('volume')
            i['group'] = k
            return_list.append(i)
    return return_list