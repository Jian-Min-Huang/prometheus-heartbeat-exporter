health-exporter
> this app is inspired by Heartbeat 💓 in Elastic Stacks, it will invoke endpoints by configuration and export 🔀 information to Prometheus.

## setup venv
```
$ pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ deactivate
```

## pip install
```
(venv) $ pip3 install -r requirements.txt
 or
(venv) $ pip3 install prometheus_client
(venv) $ pip3 install Flask
(venv) $ pip3 install urllib3
(venv) $ pip3 install APScheduler

(venv) $ pip3 freeze | tee requirements.txt
```
```
(venv) $ pip3 freeze | xargs pip3 uninstall -y
```

## ENV
```
SERVER_INFO={"root":{"url":"http://localhost:5000"},"metrics":{"url":"http://localhost:5000/metrics"}}
```

## Helm
```
$ helm install --name heartbeat ./helm
$ helm upgrade --force heartbeat ./helm
```

## DEBUG
```
add release: prometheus-operator
then can discover on prometheus but will cause service can't visit
kubectl edit prometheuses prometheus-operator-prometheus -n monitoring
>> serviceMonitorSelector: {}
```
```
if discover on prometheus but monitoring/heartbeat/0 (0/0 up)
probably your endpoint not at /metrics
```

## References
* https://www.elastic.co/cn/downloads/beats
