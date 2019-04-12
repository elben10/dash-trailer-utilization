import dash
import dash_core_components as dcc
import dash_html_components as html
import dashmaterialui as dmui

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=[])

app.layout = html.Div(
    [
        dmui.AppBar(
            dmui.Toolbar(dmui.Typography("DSV", variant="h2", color="inherit"))
        ),
        html.Main([dmui.Toolbar(), dmui.Grid(container=True, children=[dmui.Grid(item=True, children=[dmui.Typography('HELLO')])])]),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
