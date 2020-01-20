# prometheus-heartbeat-exporter
prometheus heartbeat exporter

### setup venv
```
$ pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ deactivate
```

### pip install
```
(venv) $ pip3 install -r requirements.txt
```
```
(venv) $ pip3 install prometheus_client
(venv) $ pip3 install Flask
(venv) $ pip3 install urllib3
(venv) $ pip3 install APScheduler
```
```
(venv) $ pip3 freeze | tee requirements.txt
```

### ENV
```
{"server1":{"url": "http://localhost:8000"},"server2":{"url": "http://localhost:8001"}}
```