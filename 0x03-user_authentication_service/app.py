#!/usr/bin/env python3
"""
Basic flask application for User Authentication Service
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def Hello_World():
    return jsonify(message="Bienvenue")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
