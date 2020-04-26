import jinja2
import base64
from io import BytesIO


TEMPLATE_FILE = 'template.html'


def render_template(**kwargs):
    loader = jinja2.FileSystemLoader(searchpath='./')
    env = jinja2.Environment(loader=loader)
    template = env.get_template(TEMPLATE_FILE)
    html = template.render(**kwargs)

    return html
