import os
from flask import Flask, request, Response

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

URL_AUTH = 'http://auth:8010'
URL_EVENT = 'http://event:8020'
URL_INFO = 'http://info:8030'
URL_PAY = 'http://pay:8040'
URL_STATISTIC = 'http://statistic:8050'

@app.route('/', methods=['GET'])
def GWS_hello_world():
    statement = 'Gateway service!'
    return statement

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, port=port, host="0.0.0.0")
