
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np

import plotly.graph_objs as go
import math

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets = ['stylesheet.css']

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
    #"paper": "#6D6767",
    "paper": "rgba(59.9%, 60.7%, 64.8%, 80%)",
    "ground": "#89EF89",
    "line": "#FFFFFF"
}

window_size = 10
COURT_SIZE = [72.5, 45]

def GetLineShapeDict(x0, x1, y0, y1, width=6):
    dict = {
            "type": "line",
            "x0": x0,
            "x1": x1,
            "y0": y0,
            "y1": y1,
            "line": {
                "color": court_colors["line"],
                "width":width
            }
    }
    return dict

def GetCircleShapeDict(x, y, r, width=3, line_color=court_colors["line"], fill_color=court_colors["ground"],fill=False):
    dict = {
        "type": "circle",
        "x0": x-r,
        "y0": y-r,
        "x1": x+r,
        "y1": y+r,
        "line": {
            "color": line_color,
            "width": width,
        }
    }
    return dict

layout = go.Layout(
    width = 800,
    height= 500,
    xaxis=dict(
        autorange=False,
        range=[-COURT_SIZE[0],COURT_SIZE[0]],
        zeroline=False,
        showline=False,
        mirror='ticks',
        showgrid=False,

        #グラフを描く幅、複数のグラフを描きたいなら 0 ~ 1の範囲で範囲を指定すればその範囲で描画してくれる
        domain=[0.1,0.9],
        showticklabels=False,
        #linecolor=court_colors["line"],
        #linewidth=6,
        #rangemode="nonnegative"

    ),
    yaxis=dict(
        autorange=False,
        range=[-COURT_SIZE[1], COURT_SIZE[1]],
        zeroline=False,
        showline=False,
        showgrid=False,
        scaleanchor="x",
        #ticks='',
        domain=[0.0,1.0],
        showticklabels=False,
        #linecolor=court_colors["line"],
        #linewidth=6
    ),
    shapes=[
        GetLineShapeDict(-COURT_SIZE[0],COURT_SIZE[0], COURT_SIZE[1], COURT_SIZE[1],  width=4),
        GetLineShapeDict(-COURT_SIZE[0],COURT_SIZE[0],-COURT_SIZE[1],-COURT_SIZE[1],  width=4),
        GetLineShapeDict(-COURT_SIZE[0],-COURT_SIZE[0],-COURT_SIZE[1], COURT_SIZE[1], width=4),
        GetLineShapeDict( COURT_SIZE[0], COURT_SIZE[0],-COURT_SIZE[1], COURT_SIZE[1], width=4),
        # センターライン
        GetLineShapeDict(0,0,-COURT_SIZE[1],COURT_SIZE[1], width=3),
        #ゴールエリア
        GetLineShapeDict( 67.0, 67.0,-9.16, 9.16, width=3),
        GetLineShapeDict(-67.0,-67.0,-9.16, 9.16, width=3),
        GetLineShapeDict( 67.0, COURT_SIZE[0], 9.16, 9.16, width=3),
        GetLineShapeDict( 67.0, COURT_SIZE[0],-9.16,-9.16, width=3),
        GetLineShapeDict(-67.0,-COURT_SIZE[0], 9.16, 9.16, width=3),
        GetLineShapeDict(-67.0,-COURT_SIZE[0],-9.16,-9.16, width=3),

        #ペナルティエリア
        GetLineShapeDict( 56.0, 56.0,-20.16, 20.16, width=3),
        GetLineShapeDict(-56.0,-56.0,-20.16, 20.16, width=3),
        GetLineShapeDict( 56.0, COURT_SIZE[0], 20.16, 20.16, width=3),
        GetLineShapeDict( 56.0, COURT_SIZE[0],-20.16,-20.16, width=3),
        GetLineShapeDict(-56.0,-COURT_SIZE[0], 20.16, 20.16, width=3),
        GetLineShapeDict(-56.0,-COURT_SIZE[0],-20.16,-20.16, width=3),

        #センターサークル
        GetCircleShapeDict( 0, 0, 9.150, fill=False),

        #ペナルティスポット
        GetCircleShapeDict(  61.5, 0, 0.5, fill=True, line_color="#000000", fill_color="#000000"),
        GetCircleShapeDict( -61.5, 0, 0.5, fill=True, line_color="#000000", fill_color="#000000")


    ],
    plot_bgcolor=court_colors["ground"],
    paper_bgcolor=court_colors["paper"]
)


data=[
    go.Scatter(
        x = [-9.15,9.15,0,0, -COURT_SIZE[0], COURT_SIZE[0]],
        y = [0,0,-9.15,9.15, -COURT_SIZE[1], COURT_SIZE[1]],
        text=['a', 'b','c','d'],
        name='Apple',
        marker=dict(color='#851e52'),
    )
    #,
    #go.Scatter(
    #    x=[1,2,3,4],
    #    y=[9,4,1,4],
    #    text=['w','x','y','z'],
    #    name='Tesla',
    #    marker=dict(color='#d3560e'),
    #),
]

app.layout = html.Div([
    dcc.Graph(
        id='basic-interactions',
        figure={
            'data': data,
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