import redis
from flask import Flask

app = Flask(__name__)
redis = redis.Redis(host='redis')


@app.route("/bump")
def status():
    hits = redis.get("hits")
    if hits is None:
        hits = '0'
    hits = int(hits)
    redis.set('hits', hits + 1)

    return "OK"

@app.route("/hits")
def hits():
    hits = redis.get("hits")
    if hits is None:
        hits = '0'
    return hits


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)
