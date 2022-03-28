FROM python:3.8-slim

WORKDIR /app
COPY . /app

ADD values.py .
ADD text_analyser.py .
ADD main.py .

CMD ["python3", "main.py"]
