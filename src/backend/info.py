'''
Author: hibana2077 hibana2077@gmail.com
Date: 2024-02-02 15:55:26
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-02-02 17:29:11
FilePath: /stock/info.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import requests
import bs4
import yfinance as yf
from yfinance import Ticker

def get_stock_dividends(stock:str):
    """
    Get the dividends of a stock.

    Args:
        stock (str): The stock symbol.

    Returns:
        pandas.Series: A pandas Series containing the dividends of the stock.
    """
    stock += '.TW'
    stock:Ticker = yf.Ticker(stock)
    return stock.dividends
    
def get_stock_info(stock:str):
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
    base_url = "https://tw.stock.yahoo.com/quote/{}.TW".format(stock)
    func_dict = {
        "base" : "/profile"
    }
    url = base_url + func_dict["base"]
    res = requests.get(url)
    if res.status_code != 200:
        return None
    res.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    stock_info = {}
    temp_title = soup.title.text.split(' ')[0].replace('(',' ').replace(')','')
    stock_info['stock_name'], stock_info['stock_num'] = temp_title.split(' ')
    stock_info['stock_class'] = soup.find_all('a', class_='Td(n) Px(8px) Py(3px) Fz(12px) Fw(b) Bdrs(11px) C(#188fff) Bgc($tag-bg-blue) Bgc($tag-bg-blue-hover):h')[0].text
    stock += '.TW'
    stock:Ticker = yf.Ticker(stock)
    stock_info['bookValue'] = stock.info['bookValue']
    stock_info['priceToBook'] = stock.info['priceToBook']

    return stock_info