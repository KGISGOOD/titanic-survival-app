# 基底映像檔
FROM python:3.10-slim

# 設定工作目錄
WORKDIR /app

# 複製需求檔案及應用程式
COPY app.py requirements.txt model.pkl /app/

# 安裝Python套件
RUN apt update && apt install -y build-essential python3-dev libatlas-base-dev
RUN pip install --no-cache-dir -r requirements.txt

# 暴露 Flask 端口
EXPOSE 8080

# 執行 Flask App
CMD ["python", "app.py"]