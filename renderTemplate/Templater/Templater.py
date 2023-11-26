class Templater:
    def __init__(self, html_path):
        self.html_path = html_path

    def compile(self):
        pass
    """
    read html and execute regex
    for every fragment
    check ENUM and create class
        - text
        - variable
        - create scope 
        - close scope
    """

    def render(self, context):
        pass
    """
    for every variable in tree 
    render variable
    """
