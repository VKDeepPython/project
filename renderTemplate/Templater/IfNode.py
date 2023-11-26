from Templater.Node import Node


class IfNode(Node):
    def __init__(self, fragment=None):
        self.reserved_strs = ['or', 'and', 'not', 'is', 'in',
                              '(', ')', '+', '-', '/', '*', '%',
                              '==', '>', '>=', '==', '!=', '<', '<=']
        self.condition = ""

        super().__init__(fragment)
        self.creates_scope = True

    def render(self, context):
        result_html = ""

        if eval(self.condition, context):
            result_html = self.render_children(context)

        return result_html

    def process_fragment(self, fragment):
        split_fragment = fragment.split()

        for elem in split_fragment:
            elem = elem.strip()
            self.condition += f" {elem} "
