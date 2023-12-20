from flask import Flask, jsonify, request, abort
import json
# from Components.Sonar import distance as get_sonar_distance
# from Components.MoistureSensor import get_moisture

app = Flask(__name__)


@app.route('/api/servo', methods=['POST'])
def servo():
    angle = request.json.get("angle")
    if angle is None:
        return abort(418)

    return jsonify({"result": True})


@app.route('/api/sonar', methods=['GET'])
def sonar():
    return jsonify({"result": 42})


@app.route('/api/humidity', methods=['GET'])
def humidity():
    return jsonify({"result": 5})


if __name__ == '__main__':
    app.run(debug=True, port=5001)
