#!/bin/bash

cd docker

docker build -t jianminhuang/prometheus-heartbeat-exporter:1.0.0 .
docker push jianminhuang/prometheus-heartbeat-exporter:1.0.0