from flask import Flask, jsonify, render_template, request
from SetInterval import SetInterval
from RequestHandlers import ThingsboardRequestHandler, ComponentAPIRequestHandler

app = Flask(__name__)

interval_threads = {}

componenthandler = ComponentAPIRequestHandler()

thingsboardhandler = ThingsboardRequestHandler()
thingsboardhandler.set_access_code("4k1q85v7h544t6d6ki17")

# True: get actual data. False: get static data.
PULL_DATA_FROM_API = not False


# Functions that actually measure things.
def measure_humidity(**kwargs):
    print(f"Measuring humidity on pin {kwargs['pin']} (access-code: {thingsboardhandler.access_code})")

    if PULL_DATA_FROM_API:
        humidity = componenthandler.get("humidity", pin=kwargs["pin"])
    else:
        humidity = 175

    thingsboardhandler.send({"humidity": humidity})


def measure_compass(**kwargs):
    print(f"Measuring compass on pin {kwargs['pin']} (access-code: {thingsboardhandler.access_code})")

    if PULL_DATA_FROM_API:
        compass = componenthandler.get("compass", pin=kwargs["pin"])
    else:
        compass = 80

    thingsboardhandler.send({"compass": compass})


def measure_sonar(**kwargs):
    print(f"Measuring sonar on pin {kwargs['pin']} (access-code: {thingsboardhandler.access_code})")

    if PULL_DATA_FROM_API:
        distance = componenthandler.get("sonar", pin=kwargs["pin"])
    else:
        distance = 45

    thingsboardhandler.send({"distance": distance})


def measure_magneto(**kwargs):
    print(f"Measuring magneto on pin {kwargs['pin']} (access-code: {thingsboardhandler.access_code})")

    if PULL_DATA_FROM_API:
        magneto = componenthandler.get("magneto", pin=kwargs["pin"])
    else:
        magneto = [0.1, 0.2, 0.3]

    thingsboardhandler.send({"magneto_x": magneto[0]})
    thingsboardhandler.send({"magneto_y": magneto[1]})
    thingsboardhandler.send({"magneto_z": magneto[2]})


def measure_gyro(**kwargs):
    print(f"Measuring gyroscope on pin {kwargs['pin']} (access-code: {thingsboardhandler.access_code})")

    if PULL_DATA_FROM_API:
        gyroscope = componenthandler.get("gyroscope", pin=kwargs["pin"])
    else:
        gyroscope = [0.4, 0.5, 0.6]

    thingsboardhandler.send({"gyro_x": gyroscope[0]})
    thingsboardhandler.send({"gyro_y": gyroscope[1]})
    thingsboardhandler.send({"gyro_z": gyroscope[2]})


def measure_accel(**kwargs):
    print(f"Measuring accelerator on pin {kwargs['pin']} (access-code: {thingsboardhandler.access_code})")

    if PULL_DATA_FROM_API:
        accelerator = componenthandler.get("accelerator", pin=kwargs["pin"])
    else:
        accelerator = [0.7, 0.8, 0.9]

    thingsboardhandler.send({"accelerator_x": accelerator[0]})
    thingsboardhandler.send({"accelerator_y": accelerator[1]})
    thingsboardhandler.send({"accelerator_z": accelerator[2]})


measuring_methods = {
    "humidity": measure_humidity,
    "sonar": measure_sonar,
    "compass": measure_compass,
    "accel": measure_accel,
    "gyro": measure_gyro,
    "magneto": measure_magneto,
}

# APIs


@app.route("/api/<sensor>/on", methods=["GET"])
def turn_sensor_on(sensor):
    interval = request.args.get('interval')
    pin = request.args.get('pin')

    data = {"message": f"Turning the {sensor} sensor on, with an interval of {interval} on pin {pin}"}
    interval_threads[sensor] = SetInterval(measuring_methods[sensor], int(interval), **{"pin": pin})

    return jsonify(data)


@app.route("/api/<sensor>/off", methods=["GET"])
def turn_sensor_off(sensor):
    data = {"message": f"Turning the {sensor} sensor off"}
    print(data["message"])

    if interval_threads[sensor]:
        interval_threads[sensor].cancel()
        interval_threads[sensor] = None

    return jsonify(data)


@app.route("/api/accesscode/<string:code>")
def set_access(code):
    print("setting thingsboard access code to " + code)
    thingsboardhandler.set_access_code(code)
    data = {"message": "Successully updated access code"}

    return jsonify(data)


@app.route("/")
def index():
    sensors = [
        {"name": "humidity", "display_name": "Humidity", "default_pin": "2A", "default_interval": 0.5},
        {"name": "compass", "display_name": "Compass", "default_pin": "UART 1", "default_interval": 0.2},
        {"name": "sonar", "display_name": "Sonar", "default_pin": "IC2 4", "default_interval": 0.5},
        {"name": "accel", "display_name": "Accelerator", "default_pin": "IC2 4", "default_interval": 2},
        {"name": "gyro", "display_name": "Gyroscope", "default_pin": "IC2 4", "default_interval": 2},
        {"name": "magneto", "display_name": "Magnetometer", "default_pin": "IC2 4", "default_interval": 2},
    ]

    return render_template("index.html", sensors=sensors)


if __name__ == "__main__":
    app.run(debug=True)
