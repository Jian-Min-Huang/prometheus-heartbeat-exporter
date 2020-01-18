import atexit

import urllib3
from apscheduler.schedulers.background import BackgroundScheduler
from flask import make_response, Flask
from prometheus_client import start_http_server, Gauge

from config.server_info import server_info

gauges = {}


def job():
    for key, value in server_info().items():
        if key in gauges:
            gauge = gauges[key]

            http = urllib3.PoolManager()
            res = http.request(method="GET", url=value['url'])
            print(f"{key} -> {res.status}")

            gauge.set_function(lambda: res.status)
        else:
            gauges[key] = Gauge(key, f'status of {key}')


scheduler = BackgroundScheduler()
scheduler.add_job(func=job, trigger="interval", seconds=3)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return make_response(server_info(), 200)


if __name__ == '__main__':
    start_http_server(8000)

    app.run(host="0.0.0.0")
