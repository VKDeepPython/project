from parse_params import parse_after_question_mark, parse_between_quotes
from path import Path
from exceptions import NotFoundError


class Router:
    methods = {"GET", "POST", "PUT", "PATCH", "DELETE"}

    def __init__(self):
        self.routes = []

    def add_route(self, path, handler, method):
        self.routes.append({"path": Path(path), "method": method, "handler": handler})

    def find_handler(self, path, method):
        for pattern in self.routes:
            if pattern["path"] == path and pattern["method"] == method:
                # pattern_dict = parse_between_quotes(path)
                pattern_dict = parse_between_quotes(pattern["path"].path, path)
                param_dict = parse_after_question_mark(path)
                return pattern["handler"], pattern_dict, param_dict

        raise NotFoundError(
            f"Route for path '{path}' with method '{method}' not found."
        )
