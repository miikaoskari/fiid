import json
from feedparser import parse
from jinja2 import Template

def create_html(content: list) -> str:
    html_template = """
    <html>
        <head><title>feeds</title></head>
        <body>
            <ol>
            {% for article in content %}
                <li>
                    <p>{{ article.title }}</p>
                    <a href="{{ article.link }}">Link</a>
                    {{ article.summary }}
                </li>
            {% endfor %}
            </ol>
        </body>
    </html>
    """
    t = Template(html_template)
    return t.render(content=content)

def get_feeds(urls: dict) -> list:
    contents = []
    for rss in urls['urls']:
        contents.extend(parse(rss).entries)

    return contents

def read_feeds_file() -> dict:
    with open("feeds.json", "r") as f:
        return json.loads(f.read())

if __name__ == "__main__":
    urls = read_feeds_file()
    contents = get_feeds(urls)

    html = create_html(contents)

    with open("output.html", "w") as f:
        f.write(html)
