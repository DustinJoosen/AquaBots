import requests
import json


class ThingsboardRequestHandler:
    def __init__(self):
        self.access_code = "4k1q85v7h544t6d6ki17"   # default

    def set_access_code(self, access_code: str):
        self.access_code = access_code

    def send(self, data):
        url = f"http://localhost:8080/api/v1/{self.access_code}/telemetry"

        headers = {"Content-Type": "application/json"}
        data = json.dumps(data)

        response = requests.post(url, headers=headers, data=data)
        if response.status_code != 200:
            print("Could not send telemetry")
