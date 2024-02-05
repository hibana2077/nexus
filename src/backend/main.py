'''
Author: hibana2077 hibana2077@gmail.com
Date: 2024-02-02 17:41:30
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-02-05 23:10:00
FilePath: /nexus/src/backend/main.py
Description: This is a FastAPI application that uses the Fugle API to get stock information.
'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fugle import Fugle
from yfinance import Ticker
from bs4 import BeautifulSoup
import yfinance as yf
import pandas as pd
import info
import requests

API_TOKEN = 'MTJiNTVmYzgtYThlNC00MjAyLWFlYzAtMDBhMzMzMGVhMTZiIGYwODA4MzFiLTQxNzMtNDMzOC1hZDgyLTFkYzJkZGUwNmZhOA=='

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允許所有來源
    allow_credentials=True,
    allow_methods=["*"],  # 允許所有方法
    allow_headers=["*"],  # 允許所有標頭
)

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

@app.get('/hotstock')
async def hotstock():
    """
    Retrieves the hot stocks from Yahoo Finance.

    Returns:
        list: A list of dictionaries containing the stock code and name.
    """
    url = 'https://tw.stock.yahoo.com/rank/volume'
    class_ = 'Lh(20px) Fw(600) Fz(16px) Ell'
    class_num = 'Fz(14px) C(#979ba7) Ell'
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    stocks = soup.find_all('div', class_=class_)
    stock_num = soup.find_all('span', class_=class_num)
    return_data = []
    for s,sn in zip(stocks, stock_num):
        if sn.text.split('.')[-1] == 'TW' and sn.text.split('.')[0].isnumeric():
            return_data.append({'symbol': sn.text.split('.')[0]})
    return return_data

@app.get("/news")
async def news():
    url = 'https://news.cnyes.com/news/cat/tw_stock'
    base_url = 'https://news.cnyes.com'
    class_ = 'tlhuwq2'
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    news = soup.find_all('a', class_=class_)
    return_data = []
    for n in news:
        temp_data = {}
        temp_data['title'] = n.text
        temp_data['link'] = base_url + n['href']
        return_data.append(temp_data)
    return return_data[0:6]

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

@app.post("/profile/singlestock")
async def profile(data: dict):
    """
    need parm:
    - stock (user input) eg: 2330
    - dividend_rate (user input) eg: 0.05
    - safety (user input) eg: 0.9
    """
    print(data)
    if data['stock'] == '':
        return {'error':'stock code is empty'}
    return_data = {}

    # Get stock information from Yahoo Finance.
    yf_stock_code = data['stock']+ '.TW'
    stockyf:Ticker = yf.Ticker(yf_stock_code)

    # Get stock name
    return_data['stock_name'] = info.get_stock_info(data['stock'])['name']

    # Get book value evaulate
    return_data['bookValue'] = stockyf.info['bookValue']
    return_data['bookValue_evaulate'] = '昂貴價' if stockyf.info['priceToBook'] > 2 else '合理價' if stockyf.info['priceToBook'] >= 1 else '便宜價'

    # Get dividend evaulate
    temp_data = info.dividend_fair_evaluation(float(data['dividend_rate'])/100, float(data['safety']), data['stock'])
    return_data['fair_price'] = temp_data['fair_price']
    return_data['buy_price'] = temp_data['buy_price']
    return_data['dividend_evaulate'] = temp_data['recommendation']

    return return_data

@app.post("/findstock")
async def findstock(data: dict):
    print(data)
    cats = data['cat'] # 產業類別 list
    price = float(data['price'])
    dividend_rate = float(data['dividend'])/100
    safety = float(data['safety'])
    whitelist = []
    return_data = []
    for cat in cats:
        client = Fugle(API_TOKEN)
        data = client.get_specific_stock(cat, price)
        whitelist += data
    for stock in whitelist:# stock -> {'symbol': '2330', 'name': '台積電'}
        temp_data = info.dividend_fair_evaluation(dividend_rate, safety, stock['symbol'])
        temp_info = info.get_stock_info(stock['symbol'])
        if temp_data['recommendation'] == '買進':
            return_data.append({'code':stock['symbol'],
                                'name':stock['name'],
                                'price':temp_data['stock_price'],
                                'prev_day_change':temp_info['prev_day_change'],
                                'week_52_change_percent':round(temp_info['week_52_change_percent']*100,1),
                                'eps':temp_info['eps'],
                                'income':temp_info['revenuePerShare'],
                                'ai_recommend':'Good',
                                'buy_price':temp_data['buy_price'],
                                'fair_price':temp_data['fair_price']})
    return return_data