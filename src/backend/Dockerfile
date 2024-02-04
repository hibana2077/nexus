# 使用 Python 3.11 的 Alpine Linux 版本作為基本映像
FROM python:3.11-alpine

# 設置工作目錄
WORKDIR /app

# 複製 requirements.txt 文件到工作目錄
COPY requirements.txt .

# 安裝 pip3
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

# 更新 pip
RUN pip3 install --upgrade pip

# 安裝 Python 依賴
RUN pip install --no-cache-dir -r requirements.txt

# 複製所有其他文件到工作目錄
COPY . .

# 對外開放 8000 端口
EXPOSE 8000

# 執行 FastAPI 應用
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]