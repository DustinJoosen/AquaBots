import requests
import json


class ComponentAPIRequestHandler:

    def __init__(self):
        self.base_url = "http://10.80.17.1:5001/api"

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"

        response = requests.get(url)
        if response.status_code != 200:
            print("Could not send data")
            return None

        return json.loads(response.content)["result"]

    def send(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"

        headers = {"Content-Type": "application/json"}
        data = json.dumps(data)

        response = requests.post(url, headers=headers, data=data)
        if response.status_code != 200:
            print("Could not send data")


class ThingsboardRequestHandler:

    def __init__(self, access_code=None):
        self.base_url = "http://localhost:8080/api/v1"
        self.access_code = access_code

    def set_access_code(self, access_code: str):
        self.access_code = access_code

    def send(self, data):
        url = f"{self.base_url}/{self.access_code}/telemetry"

        headers = {"Content-Type": "application/json"}
        data = json.dumps(data)

        response = requests.post(url, headers=headers, data=data)
        if response.status_code != 200:
            print("Could not send telemetry")
