from abc import ABC, abstractmethod
import json

class BaseResponse(ABC):
    header = 'text/plain'

    @abstractmethod
    def __init__(self, response):
        pass

    @abstractmethod
    def get_bytes_response(self):
        pass

class JSONResponse(BaseResponse):
    header = 'application/json'

    def __init__(self, response) -> None:
        self.response = response

    def get_bytes_response(self):
        response_json = json.dumps(self.response)
        return response_json.encode('utf-8')