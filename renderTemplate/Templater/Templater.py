import re

from Templater.Node import Node
from Templater.create_node import create_node

VAR_TOKEN_START = '{{'
VAR_TOKEN_END = '}}'
BLOCK_TOKEN_START = '{%'
BLOCK_TOKEN_END = '%}'


class Templater:
    def __init__(self, html_path):
        self.regex = re.compile(r"(%s.*?%s|%s.*?%s)" % (
            VAR_TOKEN_START,
            VAR_TOKEN_END,
            BLOCK_TOKEN_START,
            BLOCK_TOKEN_END
        ))

        self.html_path = html_path
        self.root = Node()

    def compile(self):
        with open(self.html_path, 'r', encoding="utf-8") as file:
            html = file.read().replace('\n', ' ')

        fragments = self.regex.split(html, )

        scope_stack = [self.root]
        for fragment in fragments:
            if not fragment:
                continue

            parent_scope = scope_stack[-1]

            if fragment.startswith("{% end"):
                scope_stack.pop()
                continue

            new_node = create_node(fragment)

            parent_scope.children.append(new_node)
            if new_node.creates_scope:
                scope_stack.append(new_node)

    def render(self, context):
        return self.root.render_children(context)
