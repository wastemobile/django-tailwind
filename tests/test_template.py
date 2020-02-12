from django.template.loader import render_to_string


def test_base_html(with_theme_app, settings):
    template_output = render_to_string("base.html")
    assert '<link rel="stylesheet" href="/static/css/styles.min.css">' in template_output, "Template contains styles.min.css"
