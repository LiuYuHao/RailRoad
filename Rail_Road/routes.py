from flask import Flask, render_template, request
from . import app

@app.route("/")
def index():
    return render_template("index.html")
