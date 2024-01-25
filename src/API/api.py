from flask import Flask, jsonify, request, abort
import json
from Components.Sonar import distance as get_sonar_distance
from Components.MoistureSensor import get_moisture
from Components.compass import get_compass
from Components.IMU import get_accelerometer, get_magnetometer, get_gyroscope

app = Flask(__name__)


# TODO: Make a generic endpoint that can request multiple measurements. Cause now it get's spammed.

@app.route('/api/servo', methods=['POST'])
def servo():
    angle = request.json.get("angle")
    if angle is None:
        return abort(418)

    return jsonify({"result": True})


@app.route('/api/sonar', methods=['GET'])
def sonar():
    distance = get_sonar_distance()
    return jsonify({"result": distance})


@app.route('/api/accelerator', methods=['GET'])
def accelerator():
    accel = get_accelerometer()
    return jsonify({"result": accel})

@app.route('/api/gyroscope', methods=['GET'])
def gyroscope():
    gyro = get_gyroscope()
    return jsonify({"result": gyro})

@app.route('/api/magneto', methods=['GET'])
def magneto():
    magneto = get_magnetometer()
    return jsonify({"result": magneto})


@app.route('/api/compass', methods=['GET'])
def compass():
    compass = get_compass()
    return jsonify({"result": compass})


@app.route('/api/humidity', methods=['GET'])
def humidity():
    humidity = get_moisture()
    return jsonify({"result": humidity})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
