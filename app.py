import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

### FIGURE 1

df = pd.read_csv("data/parallel_coordinates.csv")

fig = px.parallel_coordinates(df, color="Cost Penalty [%]", color_continuous_scale="Viridis")
fig.update_layout(margin={"r":0,"t":50,"l":80,"b":10}, height=600)

### Text

markdown_text = '''
### Info and Explanation


I created this [parallel coordinates plot](https://plotly.com/python-api-reference/generated/plotly.express.parallel_coordinates.html)
with Plotly and Dash, following up on a discussion on [this](https://twitter.com/fneum_/status/1308728435787866113?s=20)
Twitter thread about the article:

**Fabian Neumann, Tom Brown,
The near-optimal feasible space of a renewable power system model,
*Electric Power Systems Research*,
Volume 190,
2021,
106690,
[doi:10.1016/j.epsr.2020.106690](https://doi.org/10.1016/j.epsr.2020.106690),
[arXiv:1910.01891](https://arxiv.org/abs/1910.01891).**

This page is a work in progress! I will add new features and more detailed explanations step by step.

Copyright 2020 © [Fabian Neumann](https://www.neumann.fyi/).
This work is licensed under a [Creative Commons Attribution 4.0 International license](https://creativecommons.org/licenses/by/4.0/).
'''

### APPLICATION

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(style={'backgroundColor': "#ffffff"}, children=[
    html.H1(children='nearoptimal.systems', style={"textAlign": "center"}),

    html.Div([

            dcc.Graph(
                id="map",
                figure=fig
            ),

    ], className="row"),

    dcc.Markdown(children=markdown_text)

    

])

if __name__ == '__main__':
    server = app.run_server()