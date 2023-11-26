from renderTemplate.Templater.ForNode import ForNode
from renderTemplate.Templater.IfNode import IfNode
from renderTemplate.Templater.TextNode import TextNode
from renderTemplate.Templater.VariableNode import VariableNode

def create_node(fragment):
    if fragment.startswith('{% for'):
        fragment = fragment[6:-3]
        return ForNode(fragment)
    if fragment.startswith('{% if'):
        fragment = fragment[5:-3]
        return IfNode(fragment)
    # if fragment.startwith('{% each'):
    #     pass
    if fragment.startswith('{{'):
        fragment = fragment[3:-3]
        return VariableNode(fragment)

    return TextNode(fragment)
