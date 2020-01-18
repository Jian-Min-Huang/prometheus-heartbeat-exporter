# Create a metric to track time spent and requests made.
import random
import time

from prometheus_client import start_http_server, Summary

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)


if __name__ == '__main__':
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())
