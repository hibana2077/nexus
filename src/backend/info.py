'''
Author: hibana2077 hibana2077@gmail.com
Date: 2024-02-02 15:55:26
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-02-05 22:45:33
FilePath: /stock/info.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import requests
import bs4
import pandas as pd
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
            - eps (float): The trailing earnings per share of the stock.
            - income (float): The net income to common shareholders of the stock.
            - price (float): The current price of the stock.
            - prev_day_change (float): The change in price from the previous day.
            - week_52_change_percent (float): The percentage change in price over the past 52 weeks.
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
    stock_info['name'], stock_info['code'] = temp_title.split(' ')
    stock_info['stock_class'] = soup.find_all('a', class_='Td(n) Px(8px) Py(3px) Fz(12px) Fw(b) Bdrs(11px) C(#188fff) Bgc($tag-bg-blue) Bgc($tag-bg-blue-hover):h')[0].text
    stock += '.TW'
    stock:Ticker = yf.Ticker(stock)
    stock_info['bookValue'] = stock.info['bookValue'] if 'bookValue' in stock.info else None
    stock_info['priceToBook'] = round(stock.info['priceToBook'],5) if 'priceToBook' in stock.info else None
    stock_info['eps'] = stock.info['trailingEps'] if 'trailingEps' in stock.info else None
    stock_info['income'] = stock.info['netIncomeToCommon'] if 'netIncomeToCommon' in stock.info else None
    stock_info['price'] = round(stock.history(period='1d').Close[0],2) if ('B' not in stock_info['code']) and (stock_info['stock_class'] != 'ETF') and (stock_info['stock_class'] != "受益證券")else None
    stock_info['prev_day_change'] = round(stock.history(period='2d').diff().Close[1],2) if ('B' not in stock_info['code']) and (stock_info['stock_class'] != 'ETF') and (stock_info['stock_class'] != "受益證券") else None
    stock_info['week_52_change_percent'] = round(stock.info['52WeekChange'],3) if '52WeekChange' in stock.info else None
    stock_info['revenuePerShare'] = stock.info['revenuePerShare'] if 'revenuePerShare' in stock.info else None

    return stock_info

def dividend_fair_evaluation(dividend_rate:float, safety:float, stock_num:str):
    """
    Calculates the fair price and buy price of a stock based on its dividend rate and safety factor.

    Parameters:
    - dividend_rate (float): The desired dividend rate.
    - safety (float): The safety factor to apply to the fair price.
    - stock_num (str): The stock symbol or ticker.

    Returns:
    - dict: A dictionary containing the fair price, buy price, recommendation, stock price, and basic stock information.

    Recommendation:
    - '買進': The stock price is lower than the buy price.
    - '等待': The stock price is equal to the buy price.
    - '高於建議買進價': The stock price is higher than the buy price.
    """
    stockyf:Ticker = yf.Ticker(stock_num+'.TW')
    basic_info = get_stock_info(stock_num)
    dividend = stockyf.dividends
    dividend = pd.DataFrame(dividend)
    dividend['year'] = dividend.index.year
    avg_dividend = dividend.groupby('year').mean()[-5:]['Dividends'].mean()
    stock_price = stockyf.info['previousClose']
    fair_price = avg_dividend / dividend_rate
    buy_price = fair_price * safety
    recommendation = '買進' if stock_price < buy_price else '等待' if stock_price == buy_price else '高於建議買進價'

    # round to 2 decimal
    fair_price = round(fair_price, 2)
    buy_price = round(buy_price, 2)
    return_data = {'fair_price':fair_price,
        'buy_price':buy_price,
        'recommendation':recommendation,
        'stock_price':stock_price,
        'diff': round(stock_price - fair_price,3)}
    
    if basic_info:
        for k,v in basic_info.items():return_data[k] = v

    return return_data