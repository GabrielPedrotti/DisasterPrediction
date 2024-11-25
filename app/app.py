# app.py
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State
import plotly.express as px
import pandas as pd
import requests
from datetime import datetime
import json

states_json = "states.json"

with open(states_json, "r", encoding="utf-8") as file:
    states = json.load(file)

def convert_celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32

def get_db_data():
    url = "http://127.0.0.1:5000/api/v1/disaster/all"
    request = requests.request("GET", url)
    data = request.json()
    return data

def mount_charts_data(selected_year, selected_month, selected_state, precipitation, cooling_days, heating_days, average_temp):
    state_data = next((state for state in states if state["abbreviation"] == selected_state), {})

    data_to_predict = {
        "state": selected_state,
        "declarationType": "DR",
        "designatedArea": state_data.get("designatedArea"),
        "fipsStateCode": state_data.get("fipsStateCode"),
        "fipsCountyCode": state_data.get("fipsCountyCode"),
        "combinedFIPS": state_data.get("combinedFIPS"),
        "year": int(selected_year),
        "Month": int(selected_month),
        "Precipitation": precipitation,
        "Cooling_Days": cooling_days,
        "Heating_Days": heating_days,
        "AverageTemp": convert_celsius_to_fahrenheit(temp=average_temp),
        "ihProgramDeclared": 1,
        "iaProgramDeclared": 0,
        "paProgramDeclared": 1,
        "hmProgramDeclared": 0,
    }
    
    url = "http://127.0.0.1:5000/api/v1/model/predict"
    request = requests.request("POST", url, headers={'Content-Type': 'application/json'}, json=data_to_predict)
    data = request.json()

    aggregated = {
        "state": [data_to_predict["state"]],
        "declarationType": [data_to_predict["declarationType"]],
        "Precipitação": [data_to_predict["Precipitation"]],
        "Cooling_Days": [data_to_predict["Cooling_Days"]],
        "Heating_Days": [data_to_predict["Heating_Days"]],
        "Temperatura Média": [average_temp],
        "Year": [data_to_predict["year"]],
        "Latitude": [state_data.get("latitude")],  
        "Longitude": [state_data.get("longitude")],
        "Predição": [data.get("prediction")]
    }

    value = pd.DataFrame(aggregated)
    return value

current_year = datetime.now().year
years = [str(year) for year in range(current_year, current_year + 6)]

db_data = get_db_data()
df_db = pd.DataFrame(db_data)

df_db['Month'] = df_db['Month'].astype(int)
df_db['year'] = df_db['year'].astype(int)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Análise de Incidentes Naturais nos EUA", className='text-center text-primary mb-4'), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            dbc.Label("Ano"),
                            dcc.Dropdown(
                                id="year-dropdown",
                                options=[{"label": year, "value": year} for year in years],
                                value=None,
                                placeholder="Selecione o ano"
                            )
                        ], width=6),
                        dbc.Col([
                            dbc.Label("Mês"),
                            dcc.Dropdown(
                                id="month-dropdown",
                                options=[{"label": month, "value": month} for month in range(1, 13)],
                                value=None,
                                placeholder="Selecione o mês"
                            )
                        ], width=6),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Label("Estado"),
                            dcc.Dropdown(
                                id="state-dropdown",
                                options=[{"label": state["name"], "value": state["abbreviation"]} for state in states],
                                value=None,
                                placeholder="Selecione o estado"
                            )
                        ], width=12),
                    ], className='mt-3'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Label("Precipitação (mm)"),
                            dbc.Input(
                                id="precipitation",
                                type="number",
                                placeholder="Ex: 50.5"
                            )
                        ], width=6),
                        dbc.Col([
                            dbc.Label("Temperatura Média (°C)"),
                            dbc.Input(
                                id="average_temp",
                                type="number",
                                placeholder="Ex: 22.5"
                            )
                        ], width=6),
                    ], className='mt-3'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Label("Dias Quentes"),
                            dbc.Input(
                                id="heating_days",
                                type="number",
                                placeholder="Ex: 10"
                            )
                        ], width=6),
                        dbc.Col([
                            dbc.Label("Dias Frios"),
                            dbc.Input(
                                id="cooling_days",
                                type="number",
                                placeholder="Ex: 15"
                            )
                        ], width=6),
                    ], className='mt-3'),
                    dbc.Button("Gerar Análise Preditiva", id="submit-button", color="primary", className='mt-4 w-100'),
                ])
            ], className='h-100')
        ], width=12, lg=4, className='h-100'),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id="incident-map")
                ])
            ], className='h-100')
        ], width=12, lg=8, className='h-100')
    ], className='align-items-stretch'),
    dbc.Row([
        dbc.Col(html.H3("Algumas curiosidades do dataset", className='text-center text-primary mt-4 mb-2'), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id="incidents-per-month")
                ])
            ])
        ], width=12, lg=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id="incident-type-distribution")
                ])
            ])
        ], width=12, lg=6),
    ], className='mt-4')
], fluid=True)

@app.callback(
    Output("incident-map", "figure"),
    Output("incidents-per-month", "figure"),
    Output("incident-type-distribution", "figure"),
    Input("submit-button", "n_clicks"),
    State("year-dropdown", "value"),
    State("month-dropdown", "value"),
    State("state-dropdown", "value"),
    State("precipitation", "value"),
    State("cooling_days", "value"),
    State("heating_days", "value"),
    State("average_temp", "value")
)
def update_graphs(n_clicks, selected_year, selected_month, selected_state, precipitation, cooling_days, heating_days, average_temp):
    if n_clicks is None or not all([selected_year, selected_month, selected_state, precipitation, cooling_days, heating_days, average_temp]):
        empty_fig = px.scatter_geo(
            title="Aguardando clique no botão...",
            scope="usa",
            height=386
        )
    else:
        df = mount_charts_data(selected_year, selected_month, selected_state, precipitation, cooling_days, heating_days, average_temp)
        filtered_df = df[df["Year"] == int(selected_year)] 

        empty_fig = px.scatter_geo(
            filtered_df,
            lat="Latitude",
            lon="Longitude",
            color="Predição",
            size="Precipitação",
            hover_name="state",
            hover_data={"Predição": True, "Temperatura Média": True, "Precipitação": True},
            title=f"Predição de Incidentes Naturais nos EUA ({selected_year})",
            scope="usa",
            height=386
        )
        empty_fig.update_layout(geo=dict(showland=True, landcolor="lightgray"))

    incidents_per_month = df_db.groupby('Month').size().reset_index(name='Count')
    bar_fig = px.bar(
        incidents_per_month,
        x='Month',
        y='Count',
        title='Número de Incidentes por Mês',
        labels={'Month': 'Mês', 'Count': 'Número de Incidentes'}
    )

    incident_type_distribution = df_db['incidentType'].value_counts().reset_index(name='count')
    incident_type_distribution.rename(columns={'index': 'incidentType'}, inplace=True)

    pie_fig = px.pie(
        incident_type_distribution,
        values='count',
        names='incidentType',
        title='Distribuição de Tipos de Incidentes',
        labels={'incidentType': 'Tipo de Incidente', 'count': 'Número de Incidentes'}
    )

    return empty_fig, bar_fig, pie_fig

if __name__ == "__main__":
    app.run_server(debug=True)
