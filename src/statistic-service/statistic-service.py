import os
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def SS_hello_world():
    statement = 'Statistic service!'
    return statement

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run(debug=True, port=port, host="0.0.0.0")
