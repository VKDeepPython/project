from renderTemplate.Templater.Node import Node


class TextNode(Node):
    def process_fragment(self, fragment):
        self.name = fragment

    def render(self, context):
        return self.name

    def render_children(self, context, children=None):
        pass