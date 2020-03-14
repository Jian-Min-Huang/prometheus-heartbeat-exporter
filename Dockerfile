FROM python:3-slim

ADD . /health-exporter
WORKDIR /health-exporter

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","app.py"]
