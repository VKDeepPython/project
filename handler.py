from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Обрабатывать каждый запрос в отдельном потоке"""


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, router, *args, **kwargs) -> None:
        self.router = router
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.handle_request("GET")

    def do_POST(self):
        self.handle_request("POST")

    def do_PUT(self):
        self.handle_request("PUT")

    def do_PATCH(self):
        self.handle_request("PATCH")

    def do_DELETE(self):
        self.handle_request("DELETE")

    def handle_request(self, method):
        try:
            # Получение URL из запроса
            request_url = self.path
            print(f"Получен запрос на {request_url}")

            handler = self.router.find_handler(request_url, method)
            response = handler()

            # Отправка ответа
            print(f"Response: {response}")

            self.send_response(200)
            self.send_header("Content-type", response.header)
            self.end_headers()
            self.wfile.write(response.get_bytes_response())

        except Exception as e:
            self.send_error(500, f"Internal Server Error {str(e)}")
