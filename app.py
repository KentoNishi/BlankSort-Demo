#!flask/bin/python
from flask import Flask, request, jsonify
import json
import os
import blanksort

app = Flask(__name__, static_url_path="")


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/api", methods=["POST"])
def returnPost():
    data = request.get_json()["params"]
    return jsonify({"keywords": algo.rank(data["text"])})


@app.route("/articles", methods=["GET"])
def getArticles():
    with open(
        "C:\\Users\\kento\\Documents\\GitHub\\BlankSort-Demo\\articles.json"
    ) as json_file:
        data = json.load(json_file)
        return jsonify(data)


if __name__ == "__main__":
    algo = blanksort.BlankSort(
        "C:\\Users\\kento\\Documents\\GitHub\\BlankSort-Prototypes\\binaries\\data"
    )
    app.run(host="0.0.0.0")
