from flask import Flask, render_template
from flask.json import jsonify

from util import get_devices


app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template('dashboard.html')


@app.route("/devices/")
def devices():
    return jsonify(get_devices())


@app.route("/configure/")
def configure():
    return render_template('configure.html')


@app.route("/help/")
def help():
    return render_template('help.html')
