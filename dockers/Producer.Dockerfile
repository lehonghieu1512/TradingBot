FROM python:3.7
WORKDIR /app
COPY requirements.txt requirements.txt
COPY src src/
COPY main.py main.py
RUN pip3 install -r requirements.txt