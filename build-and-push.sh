#!/bin/bash

docker build -t jianminhuang/prometheus-heartbeat-exporter:1.0.1 .
docker push jianminhuang/prometheus-heartbeat-exporter:1.0.1