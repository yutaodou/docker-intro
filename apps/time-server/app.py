from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def time():
    now = datetime.now()
    return jsonify({"time": now.isoformat()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
