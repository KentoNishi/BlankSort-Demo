#!flask/bin/python
from flask import Flask, request, jsonify
import json

app = Flask(__name__, static_url_path="")


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/api", methods=["POST"])
def returnPost():
    data = request.get_json()["params"]
    return jsonify({"response": data["text"]})


if __name__ == "__main__":
    app.run()
