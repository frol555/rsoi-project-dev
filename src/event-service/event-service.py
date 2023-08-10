import os
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def ES_hello_world():
    statement = 'Event service!'
    return statement

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8020))
    app.run(debug=True, port=port, host="0.0.0.0")
