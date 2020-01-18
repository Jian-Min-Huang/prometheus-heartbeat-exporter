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
(venv) $ pip3 install prometheus_client
```
```
(venv) $ pip3 freeze | tee requirements.txt
(venv) $ pip3 install -r requirements.txt
```