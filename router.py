from exceptions import NotFoundError


class Router:
    methods = {"GET", "POST", "PUT", "PATCH", "DELETE"}

    def __init__(self):
        self.routes = {}

    def add_route(self, path, handler, method):
        if path not in self.routes:
            self.routes[path] = {}
        self.routes[path][method] = handler

    def find_handler(self, path, method):
        if path in self.routes and method in self.routes[path]:
            return self.routes[path][method]
        raise NotFoundError(
            f"Route for path '{path}' with method '{method}' not found."
        )
