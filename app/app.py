import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import requests
from datetime import datetime
import json


states_json = "states.json"

with open(states_json, "r", encoding="utf-8") as file:
    states = json.load(file)

def mount_charts_data(selected_year, selected_incident, selected_state):
    # TODO: the above data needs to dynamic
    teste = {
        "state": selected_state,
        "declarationType": "DR",
        "designatedArea": "Some Area",
        "fipsStateCode": 48,
        "fipsCountyCode": "001",
        "combinedFIPS": 48001,
        "year": int(selected_year),
        "Month": 8,
        "Precipitation": 12.3,
        "Cooling_Days": 45,
        "Heating_Days": 10,
        "AverageTemp": 22.5,
        "ihProgramDeclared": 1,
        "iaProgramDeclared": 0,
        "paProgramDeclared": 1,
        "hmProgramDeclared": 0,
        "incidentType": selected_incident
    }
    
    url = "http://127.0.0.1:5000/api/v1/model/predict"
    request = requests.request("POST", url, headers={'Content-Type': 'application/json'}, json=teste)
    data = request.json()

    stateData = next((state for state in states if state["abbreviation"] == teste["state"]), {})

    aggregated = {
        "state": [teste["state"]],
        "declarationType": [teste["declarationType"]],
        "Tipo de Incidente": [teste["incidentType"]],
        "Precipitação": [teste["Precipitation"]],
        "Cooling_Days": [teste["Cooling_Days"]],
        "Heating_Days": [teste["Heating_Days"]],
        "Temperatura Média": [teste["AverageTemp"]],
        "Real": [teste["incidentType"]],
        "Predicted": [teste["incidentType"]],
        "Year": [teste["year"]],
        "Latitude": [stateData.get("latitude")],  
        "Longitude": [stateData.get("longitude")],
        "Predição": [data.get("prediction")]
    }

    value = pd.DataFrame(aggregated)
    return value

current_year = datetime.now().year
years = [str(year) for year in range(current_year, current_year + 6)] 

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Análise de Incidentes Naturais nos EUA"),
    
    dcc.Dropdown(
        id="year-dropdown",
        options=[{"label": year, "value": year} for year in years],
        value=None,
        placeholder="Selecione o ano"
    ),
    
    dcc.Dropdown(
        id="incident-dropdown",
        options=[
            {"label": "Flood", "value": "Flood"},
            {"label": "Hurricane", "value": "Hurricane"},
            {"label": "Tornado", "value": "Tornado"},
            {"label": "Wildfire", "value": "Wildfire"}
        ],
        value=None,
        placeholder="Selecione o tipo de incidente"
    ),
    
    dcc.Dropdown(
        id="state-dropdown",
        options=[{"label": state["name"], "value": state["abbreviation"]} for state in states],
        value=None,
        placeholder="Selecione o estado"
    ),
    
    dcc.Graph(id="incident-map")
])

@app.callback(
    [Output("incident-map", "figure")],
    [
        Input("year-dropdown", "value"),
        Input("incident-dropdown", "value"),
        Input("state-dropdown", "value")
    ]
)
def update_graphs(selected_year, selected_incident, selected_state):
    if not all([selected_year, selected_incident, selected_state]):
        empty_fig = px.scatter_geo(
            title="Aguardando seleção de todos os campos...",
            scope="usa"
        )
        return empty_fig 

    df = mount_charts_data(selected_year, selected_incident, selected_state)

    filtered_df = df[df["Year"] == int(selected_year)] 

    incident_map = px.scatter_geo(
        filtered_df,
        lat="Latitude",
        lon="Longitude",
        color="Tipo de Incidente",
        size="Precipitação",
        hover_name="state",
        hover_data={"Predição": True, "Temperatura Média": True, "Precipitação": True},
        title=f"Incidentes Naturais nos EUA ({selected_year})",
        scope="usa"
    )
    
    incident_map.update_layout(geo=dict(showland=True, landcolor="lightgray"))
    
    return [incident_map]

if __name__ == "__main__":
    app.run_server(debug=True)