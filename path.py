import re


class Path:
    """

    :raises: TypeError, ValueError
    """

    def __init__(self, path):
        self.path = self.eval_and_process(path)
        self.items = self.path.split("/")[:-1]

    @staticmethod
    def eval_and_process(path):
        pattern = re.compile(
            r"^(((?:\/?[\+~%\/.\w\-_\<\>]*))\??(?:[-\+=&;%@.\w_]*)#?(?:[\w]*))?$"
        )
        match_obj = re.match(pattern, path)
        if match_obj:
            group = match_obj.group(2)
            new_path = "".join([item + "/" for item in group.split("/") if item])
        else:
            raise ValueError("invalid path")

        return new_path

    def __eq__(self, other):
        if not isinstance(other, str):
            raise TypeError(f"url must be a str, got {type(other)}")

        other_path = self.eval_and_process(other)
        other_items = other_path.split("/")[:-1]

        if len(self.items) != len(other_items):
            return False
        for old_i, new_i in zip(self.items, other_items):
            if old_i.startswith("<") and old_i.endswith(">"):
                continue
            if old_i != new_i:
                return False
        return True

    def __hash__(self):
        return hash(self.path)
