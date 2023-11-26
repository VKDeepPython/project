from abc import ABC, abstractmethod
import json


class BaseResponse(ABC):
    header = "text/plain"

    @abstractmethod
    def __init__(self, response):
        pass

    @abstractmethod
    def get_bytes_response(self):
        pass


class JSONResponse(BaseResponse):
    header = "application/json"

    def __init__(self, response):
        self.response = json.dumps(response)

    def get_bytes_response(self):
        return self.response.encode("utf-8")


class HTMLResponse(BaseResponse):
    header = "text/html"

    def __init__(self, file_path):
        with open(f"templates/{file_path}", "r", encoding="utf-8") as file:
            self.response = file.read()

    def get_bytes_response(self):
        return self.response.encode("utf-8")


class HTMLTextResponse(BaseResponse):
    header = "text/html"

    def __init__(self, response):
        self.response = response

    def get_bytes_response(self):
        return self.response.encode("utf-8")

class TextResponse(BaseResponse):
    header = "text/plain"

    def __init__(self, response):
        self.response = response

    def get_bytes_response(self):
        return self.response.encode("utf-8")
