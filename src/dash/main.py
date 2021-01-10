
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from DrawFootballCourt import *
from SetPlayer import *

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

team_colors = {
    "home": "#FF0000",
    "away": "#FFFFFF"
}

fc = FOOTBALL_COURT()
ps = PLAYER_SERVER()
ps.SetTeamFormation(HA.Home, "4231")
ps.SetTeamFormation(HA.Away, "433")

court_layout = go.Layout(
    width = 1200,
    height= 900,
    xaxis= fc.layout["xaxis"],
    yaxis= fc.layout["yaxis"],
    shapes= fc.shapes,
    plot_bgcolor=court_colors["ground"],
    paper_bgcolor=court_colors["paper"]
)


app.layout = html.Div([
    dcc.Graph(
        id='basic_formation',
        figure={
            'layout':court_layout,
            'data': data
        }
    ),
    dcc.Interval(
        id="interval_component",
        interval=1* 1000,
        n_intervals=0
    )
])
#@app.callback(
#    Output('hover-data', 'children'),
#    [Input('basic-interactions', 'hoverData')])
#def display_hover_data(hoverData):
#    return json.dumps(hoverData, indent=2)
@app.callback(
    dash.dependencies.Output("basic_formation", "figure"),
    [dash.dependencies.Input("interval_component", "n_intervals")])
def UpdateGraph(n):
    home_player = dict(
        x = ps.GetTeamPlayerXPositionArray(HA.Home),
        y = ps.GetTeamPlayerYPositionArray(HA.Home),
        text = ps.GetTeamPlayerUniNumberArray(HA.Home),
        name = "Home",
        textposition = "center",
        mode='markers+text',
        marker=dict(
            color=ps.GetTeamColor(HA.Home),
            size=30),
        type = "scatter"

    )

    away_player = dict(
        x=ps.GetTeamPlayerXPositionArray(HA.Away),
        y=ps.GetTeamPlayerYPositionArray(HA.Away),
        text=ps.GetTeamPlayerUniNumberArray(HA.Away),
        name="Away",
        #marker=dict(color='#851e52'),
        textposition = "center",
        mode='markers+text',
        marker={
            "color":"#0000FF",
            "size":30
        },
        type = "scatter"
    )

    data=[
        home_player,
        away_player
    ]



#if __name__ == '__main__':
#    app.run_server(debug=True)

if __name__ == '__main__':
    app.run_server(debug=True)