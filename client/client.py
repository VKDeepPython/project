import http.client
from http.client import HTTPConnection
from http import HTTPStatus
import logging


logging.basicConfig(level=logging.DEBUG)


class Client:
    def __init__(self):
        self.connection = None

    def set_connection(self, host, port=None):
        self.connection = HTTPConnection(host, port)
        self.__check_connection()

    def __check_connection(self):
        self.connection.request("GET", "/")
        response = self.connection.getresponse()
        response.read()
        if response.status == 200:
            logging.debug("Connected successfully")
        else:
            logging.warning(f"Status: {response.status}, reason: {response.reason}")

    def request(self, method: str, url: str, body=None, headers: dict = {}) -> None:
        self.connection.request(method, url, body, headers)
        logging.debug(f"Request sent: {method}, {url}")

    def get_response(self) -> http.client.HTTPResponse:
        return self.connection.getresponse()
