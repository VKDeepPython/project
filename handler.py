from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import json


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Обрабатывать каждый запрос в отдельном потоке"""


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, router, *args, **kwargs) -> None:
        self.router = router
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.handle_request("GET")

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8")
        try:
            json_data = json.loads(body)
        except json.JSONDecodeError:
            json_data = {}

        self.handle_request("POST", json_data)

    def do_PUT(self):
        self.handle_request("PUT")

    def do_PATCH(self):
        self.handle_request("PATCH")

    def do_DELETE(self):
        self.handle_request("DELETE")

    def handle_request(self, method, body={}):
        try:
            # Получение URL из запроса
            request_url = self.path
            print(
                f"Получен запрос на {request_url} от клиента {self.client_address[0]}"
            )

            handler, pattern_dict, params_dict = self.router.find_handler(
                request_url, method
            )
            response = handler(pattern_dict, params_dict, body)

            print(f"Body {body=}")
            # Отправка ответа
            print(f"Params before: {pattern_dict}, params after: {params_dict}")
            print(f"Response: {response}")

            self.send_response(200)
            self.send_header("Content-type", response.header)
            self.end_headers()
            self.wfile.write(response.get_bytes_response())

        except Exception as e:
            self.send_error(500, f"Internal Server Error {str(e)}")
