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
        try:
            # Получение URL из запроса
            request_url = self.path
            print(f"Получен запрос на {request_url}")
    
            handler = self.router.find_handler(request_url, "GET")
            response = handler()
            # header = 'text/html'
            header = 'application/json'
    
            # Отправка ответа
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            response_json = json.dumps(response)
            self.wfile.write(response_json.encode('utf-8'))

        except Exception as e:
            self.send_error(500, f'Internal Server Error: {str(e)}')