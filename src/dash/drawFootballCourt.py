
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np

import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

court_size = {
    "width": 150,
    "height": 90
}

court_colors = {
    "paper": "#6D6767",
    "ground": "#89EF89",
    "line": "#FFFFFF"
}

window_size = 10

layout = go.Layout(
    width =window_size * court_size["width"],
    height=window_size * court_size["height"],
    xaxis=dict(
        autorange=False,
        range=[-72.5,72.5],
        zeroline=False,
        showline=True,
        mirror='ticks',
        domain=[0, 1.0],
        showgrid=False,
        ticks='',
        showticklabels=False,
        linecolor=court_colors["line"],
        linewidth=6

    ),
    yaxis=dict(
        autorange=False,
        range=[-45, 45],
        zeroline=False,
        showline=True,
        mirror='ticks',
        domain=[0, 1.0],
        showgrid=False,
        ticks='',
        showticklabels=False,
        linecolor=court_colors["line"],
        linewidth=6
    ),
    plot_bgcolor=court_colors["ground"],
    paper_bgcolor=court_colors["paper"]
)

app.layout = html.Div([
    dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'x': [1, 2, 3, 4],
                    'y': [4, 1, 3, 5],
                    'text': ['a', 'b', 'c', 'd'],
                    'customdata': ['c.a', 'c.b', 'c.c', 'c.d'],
                    'name': 'Trace 1',
                    'mode': 'markers',
                    'marker': {'size': 12}
                },
                {
                    'x': [1, 2, 3, 4],
                    'y': [9, 4, 1, 4],
                    'text': ['w', 'x', 'y', 'z'],
                    'customdata': ['c.w', 'c.x', 'c.y', 'c.z'],
                    'name': 'Trace 2',
                    'mode': 'markers',
                    'marker': {'size': 12}
                }
            ],
            'layout':layout
        }
    )
])

#@app.callback(
#    Output('hover-data', 'children'),
#    [Input('basic-interactions', 'hoverData')])
#def display_hover_data(hoverData):
#    return json.dumps(hoverData, indent=2)

if __name__ == '__main__':
    app.run_server(debug=True)