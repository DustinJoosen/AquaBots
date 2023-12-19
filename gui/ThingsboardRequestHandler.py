import requests
import json


class ThingsboardRequestHandler:

    BASE_URL = "http://localhost:8080/api/v1"

    def __init__(self, access_code="4k1q85v7h544t6d6ki17"):
        self.access_code = access_code

    def set_access_code(self, access_code: str):
        self.access_code = access_code

    def send(self, data):
        url = f"{ThingsboardRequestHandler.BASE_URL}/{self.access_code}/telemetry"

        headers = {"Content-Type": "application/json"}
        data = json.dumps(data)

        response = requests.post(url, headers=headers, data=data)
        if response.status_code != 200:
            print("Could not send telemetry")
