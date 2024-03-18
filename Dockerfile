FROM python:3.9-slim as py
WORKDIR /app/hr_back
COPY . /app/hr_back
RUN pip install -r requirements.txt

FROM py
EXPOSE 5000
CMD [ "python", "main.py" ]
