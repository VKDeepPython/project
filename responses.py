from abc import ABC, abstractmethod
import json

class TextResponse(ABC):
    header = 'text/plain'

    @abstractmethod
    def __init__(self, response):
        pass

    @abstractmethod
    def get_bytes_response(self):
        pass

class JSONResponse(TextResponse):
    header = 'application/json'

    def __init__(self, response):
        try:
            self.response = json.dumps(json.loads(response))
        except json.JSONDecodeError as err:
            raise ValueError('invalid JSON') from err

    def get_bytes_response(self):
        response_json = json.dumps(self.response)
        return response_json.encode('utf-8')
    
class HTMLResponse(TextResponse):
    header = 'text/html'
    
    def init(self, response):
        self.response = response

class TextResponse(TextResponse):
    header = 'text/plain'
    
    def __init__(self, response):
        self.response = response