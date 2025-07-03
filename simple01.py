from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    contents = Div(
        A('Link', hx_get='/page', hx_target="closest Main"),
    )
    return Main('Home', contents)

@rt("/page")
def get():
    contents = Div(
        A('Home', hx_get='/', hx_target="closest Main"),
    )
    return Main('Page', contents)

serve()