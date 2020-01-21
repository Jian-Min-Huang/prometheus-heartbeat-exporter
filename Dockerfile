FROM python:3-slim
MAINTAINER yfr.huang@hotmail.com

ADD . /prometheus-heartbeat-exporter
WORKDIR /prometheus-heartbeat-exporter

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","app.py"]