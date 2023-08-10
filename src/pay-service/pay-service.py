import os
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def PS_hello_world():
    statement = 'Pay service!'
    return statement

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8040))
    app.run(debug=True, port=port, host="0.0.0.0")
