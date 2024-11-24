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

def convert_celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32

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
        id="month-dropdown",
        options=[{"label": month, "value": month} for month in range(1, 13)],
        value=None,
        placeholder="Selecione o mês"
    ),

    dcc.Dropdown(
        id="state-dropdown",
        options=[{"label": state["name"], "value": state["abbreviation"]} for state in states],
        value=None,
        placeholder="Selecione o estado"
    ),

    dcc.Input(
        id="precipitation",
        type="number",
        placeholder="Precipitação (mm)"
    ),

    dcc.Input(
        id="cooling_days",
        type="number",
        placeholder="Dias frios"
    ),

    dcc.Input(
        id="heating_days",
        type="number",
        placeholder="Dias quentes"
    ),

    dcc.Input(
        id="average_temp",
        type="number",
        placeholder="Temperatura média (°C)"
    ),

    html.Button("Gerar Análise Preditiva", id="submit-button", n_clicks=0),
    
    dcc.Graph(id="incident-map")
])

@app.callback(
    [Output("incident-map", "figure")],
    [
        Input("submit-button", "n_clicks")
    ],
    [
        Input("year-dropdown", "value"),
        Input("month-dropdown", "value"),
        Input("state-dropdown", "value"),
        Input("precipitation", "value"),
        Input("cooling_days", "value"),
        Input("heating_days", "value"),
        Input("average_temp", "value")
    ]
)
def update_graphs(n_clicks, selected_year, selected_month, selected_state, precipitation, cooling_days, heating_days, average_temp):
    if n_clicks == 0 or not all([selected_year, selected_month, selected_state, precipitation, cooling_days, heating_days, average_temp]):
        empty_fig = px.scatter_geo(
            title="Mapa dos Estados Unidos:",
            scope="usa"
        )
        return [empty_fig]

    df = mount_charts_data(selected_year, selected_month, selected_state, precipitation, cooling_days, heating_days, average_temp)

    filtered_df = df[df["Year"] == int(selected_year)] 

    incident_map = px.scatter_geo(
        filtered_df,
        lat="Latitude",
        lon="Longitude",
        color="Predição",
        size="Precipitação",
        hover_name="state",
        hover_data={"Predição": True, "Temperatura Média": True, "Precipitação": True},
        title=f"Incidentes Naturais nos EUA ({selected_year})",
        scope="usa"
    )
    
    incident_map.update_layout(geo=dict(showland=True, landcolor="lightgray"))
    
    n_clicks = 0

    return [incident_map]

if __name__ == "__main__":
    app.run_server(debug=True)