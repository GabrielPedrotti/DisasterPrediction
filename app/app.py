import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import requests

df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 20, 30, 40],
    "Year": [2020, 2021, 2022, 2023]
})

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Análise de Predição de Desastres Naturais"),

    dcc.Dropdown(
        id="year-dropdown",
        options=[{"label": str(year), "value": year} for year in df["Year"].unique()],
        value=df["Year"].min()
    ),

    dcc.Graph(id="bar-chart"),
    dcc.Graph(id="line-chart"),
    dcc.Graph(id="incidents-freq-chart"),
    dcc.Graph(id="avg-temp-chart")
])

@app.callback(
    [Output("bar-chart", "figure"),
     Output("line-chart", "figure"),
     Output("incidents-freq-chart", "figure"),
     Output("avg-temp-chart", "figure")],
    [Input("year-dropdown", "value")]
)
def update_graph(selected_year):
    filtered_df = df[df["Year"] == selected_year]
    
    precipitation_chart = px.bar(filtered_df, x="Category", y="Values", title="Precipitação ao Longo do Tempo")
    
    incidents_types_states_chart = px.line(filtered_df, x="Category", y="Values", title="Tipos de Incidentes por Estado")

    incidents_freq_states_chart = px.line(filtered_df, x="Category", y="Values", title="Frequência de Incidentes por Estado")

    avg_temp_chart = px.line(filtered_df, x="Category", y="Values", title="Temperatura Média vs. Dias de Resfriamento e Aquecimento")
    
    return precipitation_chart, incidents_types_states_chart, incidents_freq_states_chart, avg_temp_chart

def get_data():
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
    return response.json()

if __name__ == "__main__":
    app.run_server(debug=True)