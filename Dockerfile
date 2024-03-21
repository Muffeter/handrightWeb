FROM python:3.9-slim
WORKDIR /app/hr_back
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY . .

EXPOSE 5000
CMD [ "python", "main.py" ]
