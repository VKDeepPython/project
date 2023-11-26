from renderTemplate.Templater.Node import Node

class ForNode(Node):
    def __init__(self, fragment=None):
        self.key = ""
        self.name = ""

        super().__init__(fragment)
        self.creates_scope = True

    def render(self, context):
        result_html = ""

        iterable_obj = context[self.name]

        for elem in iterable_obj:
            context[self.key] = elem
            result_html += self.render_children(context)

        del context[self.key]

        return result_html

    def process_fragment(self, fragment):
        # for elem in elems, fragment[0] == elem, etc
        fragment = fragment.split()
        self.key = fragment[0]
        self.name = fragment[2]
