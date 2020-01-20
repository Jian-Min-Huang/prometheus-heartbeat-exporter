import atexit
import json
import os

import prometheus_client
import urllib3
from apscheduler.schedulers.background import BackgroundScheduler
from flask import make_response, Flask, Response
from prometheus_client import Gauge, CollectorRegistry

server_info = json.loads(os.getenv("SERVER_INFO"))
REGISTRY = CollectorRegistry(auto_describe=False)
gauges = {}


def job():
    for key, value in server_info.items():
        if key in gauges:
            gauge = gauges[key]

            try:
                http = urllib3.PoolManager()
                res = http.request(method="GET", url=value['url'])
                # print(f"{key} -> {res.status}")

                gauge.set_function(lambda: res.status)
            except:
                gauge.set_function(lambda: 500.0)
        else:
            gauges[key] = Gauge(key, f'status of {key}', registry=REGISTRY)


scheduler = BackgroundScheduler()
scheduler.add_job(func=job, trigger="interval", seconds=3)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())

app = Flask(__name__)


@app.route("/metrics", methods=["GET"])
def metrics():
    return Response(prometheus_client.generate_latest(REGISTRY), mimetype="text/plain")


@app.route("/", methods=["GET"])
def root():
    return make_response(server_info, 200)


if __name__ == '__main__':
    app.run(host="0.0.0.0")