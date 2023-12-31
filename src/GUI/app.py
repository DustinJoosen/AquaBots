from flask import Flask, jsonify, render_template, request
from SetInterval import SetInterval
from RequestHandlers import ThingsboardRequestHandler, ComponentAPIRequestHandler
import random

app = Flask(__name__)

interval_threads = {}

componenthandler = ComponentAPIRequestHandler()

thingsboardhandler = ThingsboardRequestHandler()
thingsboardhandler.set_access_code("4k1q85v7h544t6d6ki17")


# Functions that actually measure things.
def measure_humidity(**kwargs):
    print(f"Measuring humidity on pin {kwargs['pin']} (access-code: {thingsboardhandler.access_code})")

    humidity = componenthandler.get("humidity")
    print(f"measured humidity: {humidity}")
    thingsboardhandler.send({"humidity": humidity})


def measure_gps(**kwargs):
    print(f"Measuring GPS on pin {kwargs['pin']} (access-code: {thingsboardhandler.access_code})")
    thingsboardhandler.send({"gps": kwargs['pin']})


def measure_sonar(**kwargs):
    print(f"Measuring sonar on pin {kwargs['pin']} (access-code: {thingsboardhandler.access_code})")

    # Measure using sonar here
    distance = componenthandler.get("sonar")
    thingsboardhandler.send({"distance": distance})


# APIs
@app.route("/api/sonar/on", methods=["GET"])
def sonar_on():
    interval = request.args.get('interval')
    pin = request.args.get('pin')

    data = {"message": f"Turning the Sonar sensor on, with an interval of {interval} on pin {pin}"}

    interval_threads["sonar"] = SetInterval(measure_sonar, int(interval), **{"pin": pin})

    return jsonify(data)


@app.route("/api/sonar/off", methods=["GET"])
def sonar_off():
    data = {"message": "Turning the Sonar sensor off"}

    interval_threads["sonar"].cancel()
    interval_threads["sonar"] = None

    return jsonify(data)


@app.route("/api/gps/on", methods=["GET"])
def gps_on():
    interval = request.args.get('interval')
    pin = request.args.get('pin')

    data = {"message": f"Turning the gps sensor on, with an interval of {interval} on pin {pin}"}

    interval_threads["gps"] = SetInterval(measure_gps, int(interval), **{"pin": pin})

    return jsonify(data)


@app.route("/api/gps/off", methods=["GET"])
def gps_off():
    data = {"message": "Turning the GPS sensor off"}

    interval_threads["gps"].cancel()
    interval_threads["gps"] = None

    return jsonify(data)


@app.route("/api/humidity/on", methods=["GET"])
def humidity_on():
    interval = request.args.get('interval')
    pin = request.args.get('pin')

    data = {"message": f"Turning the humidity sensor on, with an interval of {interval} on pin {pin}"}

    interval_threads["humidity"] = SetInterval(measure_humidity, int(interval), **{"pin": pin})

    return jsonify(data)


@app.route("/api/humidity/off", methods=["GET"])
def humidity_off():
    data = {"message": f"Turning the humidity sensor off"}

    interval_threads["humidity"].cancel()
    interval_threads["humidity"] = None

    return jsonify(data)


@app.route("/api/accesscode/<string:code>")
def set_access(code):
    print("setting thingsboard access code to " + code)
    thingsboardhandler.set_access_code(code)
    data = {"message": "Successully updated access code"}

    return jsonify(data)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
