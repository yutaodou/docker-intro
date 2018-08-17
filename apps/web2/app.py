from flask import Flask
import urllib, json

app = Flask(__name__)


@app.route('/')
def hello_world():
    response = urllib.request.urlopen('http://time-server:5000')
    resp = json.loads(response.read())
    return 'Hello docker, the time now is: %s' % resp['time']

if __name__ == '__main__':
    app.run(host='0.0.0.0')
