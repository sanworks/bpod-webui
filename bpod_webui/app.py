import ipaddress
import time

from flask import Flask, render_template, request
from flask.json import jsonify

from bpod_core.bpod import RemoteBpod
from bpod_webui.util import get_example_devices, get_network_devices, get_settings_path


app = Flask(__name__)


@app.route("/")
def dashboard():
    """ Bpod Rig Dashboard: Displays status of persisted Bpod devices via ajax """
    return render_template('dashboard.html', json_route='devices')


@app.route("/devices.json")
def devices():
    """ persisted devices (JSON); used in dashboard ajax call """
    return jsonify([])


@app.route("/browse/")
def devices_browse():
    """ Browse Network: Displays the Bpod devices available on the network and
     facilitates adding them to the persisted Bpod devices via ajax """
    return render_template('devices_browse.html', json_route='network_devices')


@app.route("/browse/devices.json")
def network_devices():
    return jsonify(get_network_devices())


@app.route("/blink/", methods=["POST"])
def blink_bpod_light():
    # Get and validate address
    data = request.get_json()
    address = data.get("address", "").strip()
    if not address:
        return {"error": "No address provided. Specify an 'address' in your json like tcp://10.42.37.54:62710"}, 400
    try:
        prefix, rest = address.split("://")
        ip, port = rest.split(":")
        if prefix != "tcp":
            jsonify({"error": "Invalid protocol. Address must use tcp."}), 400
        ipaddress.ip_address(ip)
        try:
            port = int(port)
        except ValueError:
            jsonify({"error": "Invalid port. Port number is not an integer."}), 400
        if not (1 <= port <= 65535):
            jsonify({"error": "Invalid port. Port number out of range."}), 400
    except Exception:
        return jsonify({"error": "Invalid address format. Specify an 'address' in your json like tcp://10.42.37.54:62710"}), 400

    # Connect to the Bpod and blink its light a few times
    bpod = RemoteBpod(address=address)
    for _r in range(3):
        bpod._remote_call('set_status_led', False)
        time.sleep(0.3)
        bpod._remote_call('set_status_led', True)
        time.sleep(0.3)
    return jsonify({"status": "ok"})


@app.route("/settings/")
def settings():
    """ Settings: Displays the current settings with options to change them """
    return render_template('settings.html', settings_path=get_settings_path())


@app.route("/help/")
def help():
    """ Help: Displays simple instructions for using this Web UI while also including
    links to other documentation on the Bpod neuroscience ecosystem as a whole """
    return render_template('help.html')


@app.route("/example/")
def example():
    """ Example Bpod Rig Dashboard: Displays example Bpod devices via ajax """
    return render_template('dashboard.html', json_route='example_devices')


@app.route("/example/devices.json")
def example_devices():
    """ example devices (JSON); used in example dashboard ajax call """
    return jsonify(get_example_devices())
