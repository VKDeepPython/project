from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Обрабатывать каждый запрос в отдельном потоке"""

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, router, *args, **kwargs) -> None:
        self.router = router
        super().__init__(*args, **kwargs)

    def do_GET(self):
        try:
            # Получение URL из запроса
            request_url = self.path
            print(f"Получен запрос на {request_url}")
    
            handler = self.router.find_handler(request_url, "GET")
            response = handler()
    
            # Отправка ответа
            print(f"Response: {response}")

            self.send_response(200)
            self.send_header('Content-type', response.header)
            self.end_headers()
            self.wfile.write(response.get_bytes_response())


        except Exception as e:
            self.send_error(500, f'Internal Server Error: {str(e)}')