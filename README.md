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
```
(venv) $ pip3 freeze | xargs pip3 uninstall -y
```

### ENV
```
{"root":{"url":"http://localhost:5000"},"server2":{"metrics":"http://localhost:5000/metrics"}}
```