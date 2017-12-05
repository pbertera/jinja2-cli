import os
from jinja2cli import cli

# change dir to tests directory to make relative paths possible
os.chdir(os.path.dirname(os.path.realpath(__file__)))


def test_relative_path():
    path = "./files/template.j2"

    output = cli.render(path, {"title": "Test"}, [])
    if isinstance(output, cli.binary_type):
        output = output.decode('utf-8')
    assert output == "Test"


def test_absolute_path():
    absolute_base_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(absolute_base_path, "files", "template.j2")

    output = cli.render(path, {"title": "Test"}, [])
    if isinstance(output, cli.binary_type):
        output = output.decode('utf-8')
    assert output == "Test"

def test_markdown():
    path = "./files/md_template.j2"

    output = cli.render(path, {"content": "#Test"}, [], markdown=True)
    if isinstance(output, cli.binary_type):
        output = output.decode('utf-8')
    assert output == "<h1>Test</h1>\n"
