# import time

# import torch
# import torch.nn as nn

# s = time.time()

# target = torch.tensor(89.64)
# now = torch.tensor(102.87)

# loss = nn.SmoothL1Loss()(target, now)

# e = time.time()

# print(f"Time: {e-s}, Loss: {loss}")

# import yfinance as yf

# stock = yf.Ticker('1303.TW')
# print(stock.history(period='2d').diff().Close[1])
# from info import dividend_fair_evaluation

# print(dividend_fair_evaluation(0.05, 0.9, '6136'))
# from bs4 import BeautifulSoup
# import requests

# url = 'https://news.cnyes.com/news/cat/tw_stock'
# class_ = 'tlhuwq2'
# res = requests.get(url)
# res.encoding = 'utf-8'
# soup = BeautifulSoup(res.text, 'html.parser')
# stocks = soup.find_all('a', class_=class_)
# for s in stocks:
#     print(s.text)
a_str = '00878L'
b_str = '00878'
print(a_str.isnumeric(), b_str.isnumeric())