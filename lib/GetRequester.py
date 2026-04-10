import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """
        Queries the endpoint and returns the raw response body (bytes).
        """
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        """
        Queries the endpoint, converts the response to JSON, and returns the data.
        """
        response = requests.get(self.url)
        return response.json()