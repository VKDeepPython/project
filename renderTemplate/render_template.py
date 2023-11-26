from Templater.Templater import Templater

def render_template(html_page_path: str, **kwargs) -> str:
    if not isinstance(html_page_path, str):
        raise RuntimeError(f"html_page must be str, not {type(html_page_path)}")

    templater = Templater(html_page_path)

    templater.compile()

    return templater.render(kwargs)

