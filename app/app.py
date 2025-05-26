from flask import Flask
from prometheus_client import make_wsgi_app, Counter, Gauge
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

# Создаем метрики
CONNECTIONS = Gauge("stream_connections", "Active user connections")
ERRORS = Counter("stream_errors", "Total streaming errors")

@app.route("/")
def home():
    return "VideoStream Home"

@app.route("/metrics")
def metrics():
    return make_wsgi_app()

# Эмуляция метрик
CONNECTIONS.set(100)
ERRORS.inc(5)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
