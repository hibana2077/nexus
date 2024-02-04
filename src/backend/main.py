'''
Author: hibana2077 hibana2077@gmail.com
Date: 2024-02-02 17:41:30
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-02-04 12:51:10
FilePath: /nexus/src/backend/main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}