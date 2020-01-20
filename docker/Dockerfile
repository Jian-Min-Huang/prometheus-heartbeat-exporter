FROM python:3-slim

ADD .. /prometheus-heartbeat-exporter
WORKDIR /prometheus-heartbeat-exporter

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","./prometheus-heartbeat-exporter/app.py"]