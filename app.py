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

                if "url" in value:
                    res = http.request(method="GET", url=value["url"])

                    gauge.set_function(lambda: res.status)
                if "metric" in value:
                    res = http.request(method=value["method"], url=value["metric"])
                    body = json.loads(res.data.decode("utf-8"))
                    value = eval(value["expr"])

                    gauge.set_function(lambda: value)
            except:
                gauge.set_function(lambda: 1000000)
        else:
            gauges[key] = Gauge(key, f"status of {key}", registry=REGISTRY)


scheduler = BackgroundScheduler()
scheduler.add_job(func=job, max_instances=30, trigger="interval", seconds=3)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())

app = Flask(__name__)


@app.route("/metrics", methods=["GET"])
def metrics():
    return Response(prometheus_client.generate_latest(REGISTRY), mimetype="text/plain")


@app.route("/", methods=["GET"])
def root():
    return make_response(server_info, 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
