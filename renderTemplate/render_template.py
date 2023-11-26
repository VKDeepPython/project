from string import Template

def render_template(html_page_path: str, params: dict) -> str:
    if not isinstance(html_page_path, str):
        raise RuntimeError(f"html_page must be str, not {type(html_page_path)}")
    if not isinstance(params, dict):
        raise RuntimeError(f"params must be dict, not {type(params)}")

    with open(html_page_path) as file:
        template: Template = Template(file.read())

    static_html :str = template.substitute(**params)
    return static_html

