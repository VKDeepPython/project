from router import Router
from handler import HTTPRequestHandler, ThreadedHTTPServer


class Application:
    def __init__(self):
        self.router = Router()

    def route(self, path, method="GET"):
        if method.upper() not in self.router.methods:
            raise ValueError(
                "Invalid HTTP method. Supported methods are 'GET' and 'POST'."
            )

        def decorator(handler):
            self.router.add_route(path, handler, method.upper())
            return handler

        return decorator

    def start(self, host="127.0.0.1", port=8000):
        server_address = (host, port)
        httpd = ThreadedHTTPServer(
            server_address,
            lambda *args, **kwargs: HTTPRequestHandler(self.router, *args, **kwargs),
        )
        print(f"Server running on {host}:{port}")
        httpd.serve_forever()
