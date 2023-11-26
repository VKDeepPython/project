from renderTemplate.Templater.Node import Node


class VariableNode(Node):
    def render(self, context):
        return context[self.name]

    def process_fragment(self, fragment):
        fragment = fragment.strip()
        self.name = f"{fragment}"
