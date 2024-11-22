import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import requests

states = [
  {
    "name": "Alabama",
    "abbreviation": "AL",
    "latitude": "32.31823140",
    "longitude": "-86.90229800",
    "timezones": ["CST (UTC-6)", "EST (UTC-5)"],
    "ianaTimezones": ["US/Central", "US/Eastern"]
  },
  {
    "name": "Alaska",
    "abbreviation": "AK",
    "latitude": "64.20084130",
    "longitude": "-149.49367330",
    "timezones": ["AKST (UTC-09)", "HST/HDT (UTC-10)"],
    "ianaTimezones": ["US/Alaska", "US/Aleutian"]
  },
  {
    "name": "Arizona",
    "abbreviation": "AZ",
    "latitude": "34.04892810",
    "longitude": "-111.09373110",
    "timezones": ["MST (UTC-07)", "MST/MDT (UTC-07)"],
    "ianaTimezones": ["US/Arizona", "US/Mountain"]
  },
  {
    "name": "Arkansas",
    "abbreviation": "AR",
    "latitude": "35.20105000",
    "longitude": "-91.83183340",
    "timezones": ["CST (UTC-6)"],
    "ianaTimezones": ["US/Central"]
  },
  {
    "name": "California",
    "abbreviation": "CA",
    "latitude": "36.77826100",
    "longitude": "-119.41793240",
    "timezones": ["PST (UTC-8)"],
    "ianaTimezones": ["US/Pacific"]
  },
  {
    "name": "Colorado",
    "abbreviation": "CO",
    "latitude": "39.55005070",
    "longitude": "-105.78206740",
    "timezones": ["MST (UTC-07)"],
    "ianaTimezones": ["US/Mountain"]
  },
  {
    "name": "Connecticut",
    "abbreviation": "CT",
    "latitude": "41.60322070",
    "longitude": "-73.08774900",
    "timezones": ["EST (UTC-5)"],
    "ianaTimezones": ["US/Eastern"]
  },
  {
    "name": "Delaware",
    "abbreviation": "DE",
    "latitude": "38.91083250",
    "longitude": "-75.52766990",
    "timezones": ["EST (UTC-5)"],
    "ianaTimezones": ["US/Eastern"]
  },
  {
    "name": "Florida",
    "abbreviation": "FL",
    "latitude": "27.66482740",
    "longitude": "-81.51575350",
    "timezones": ["EST (UTC-5)", "CST (UTC-6)"],
    "ianaTimezones": ["US/Eastern", "US/Central"]
  },
  {
    "name": "Georgia",
    "abbreviation": "GA",
    "latitude": "32.16562210",
    "longitude": "-82.90007510",
    "timezones": ["EST (UTC-5)"],
    "ianaTimezones": ["US/Eastern"]
  },
  {
    "name": "Hawaii",
    "abbreviation": "HI",
    "latitude": "19.89676620",
    "longitude": "-155.58278180",
    "timezones": ["HAST (UTC-10)"],
    "ianaTimezones": ["US/Hawaii"]
  },
  {
    "name": "Idaho",
    "abbreviation": "ID",
    "latitude": "44.06820190",
    "longitude": "-114.74204080",
    "timezones": ["MST (UTC-07)", "PST (UTC-8)"],
    "ianaTimezones": ["US/Mountain", "US/Pacific"]
  },
  {
    "name": "Illinois",
    "abbreviation": "IL",
    "latitude": "40.63312490",
    "longitude": "-89.39852830",
    "timezones": ["CST (UTC-6)"],
    "ianaTimezones": ["US/Central"]
  },
  {
    "name": "Indiana",
    "abbreviation": "IN",
    "latitude": "40.26719410",
    "longitude": "-86.13490190",
    "timezones": ["EST (UTC-5)", "CST (UTC-6)"],
    "ianaTimezones": ["US/Eastern", "US/Central"]
  },
  {
    "name": "Iowa",
    "abbreviation": "IA",
    "latitude": "41.87800250",
    "longitude": "-93.09770200",
    "timezones": ["CST (UTC-6)"],
    "ianaTimezones": ["US/Central"]
  },
  {
    "name": "Kansas",
    "abbreviation": "KS",
    "latitude": "39.01190200",
    "longitude": "-98.48424650",
    "timezones": ["CST (UTC-6)", "MST (UTC-07)"],
    "ianaTimezones": ["US/Central", "US/Mountain"]
  },
  {
    "name": "Kentucky",
    "abbreviation": "KY",
    "latitude": "37.83933320",
    "longitude": "-84.27001790",
    "timezones": ["EST (UTC-5)", "CST (UTC-6)"],
    "ianaTimezones": ["US/Eastern", "US/Central"]
  },
  {
    "name": "Louisiana",
    "abbreviation": "LA",
    "latitude": "30.98429770",
    "longitude": "-91.96233270",
    "timezones": ["CST (UTC-6)"],
    "ianaTimezones": ["US/Central"]
  },
  {
    "name": "Maine",
    "abbreviation": "ME",
    "latitude": "45.25378300",
    "longitude": "-69.44546890",
    "timezones": ["EST (UTC-5)"],
    "ianaTimezones": ["US/Eastern"]
  },
  {
    "name": "Maryland",
    "abbreviation": "MD",
    "latitude": "39.04575490",
    "longitude": "-76.64127120",
    "timezones": ["EST (UTC-5)"],
    "ianaTimezones": ["US/Eastern"]
  },
  {
    "name": "Massachusetts",
    "abbreviation": "MA",
    "latitude": "42.40721070",
    "longitude": "-71.38243740",
    "timezones": ["EST (UTC-5)"],
    "ianaTimezones": ["US/Eastern"]
  },
  {
    "name": "Michigan",
    "abbreviation": "MI",
    "latitude": "44.31484430",
    "longitude": "-85.60236430",
    "timezones": ["EST (UTC-5)", "CST (UTC-6)"],
    "ianaTimezones": ["US/Eastern", "US/Central"]
  },
  {
    "name": "Minnesota",
    "abbreviation": "MN",
    "latitude": "46.72955300",
    "longitude": "-94.68589980",
    "timezones": ["CST (UTC-6)"],
    "ianaTimezones": ["US/Central"]
  },
  {
    "name": "Mississippi",
    "abbreviation": "MS",
    "latitude": "32.35466790",
    "longitude": "-89.39852830",
    "timezones": ["CST (UTC-6)"],
    "ianaTimezones": ["US/Central"]
  },
  {
    "name": "Missouri",
    "abbreviation": "MO",
    "latitude": "37.96425290",
    "longitude": "-91.83183340",
    "timezones": ["CST (UTC-6)"],
    "ianaTimezones": ["US/Central"]
  },
  {
    "name": "Montana",
    "abbreviation": "MT",
    "latitude": "46.87968220",
    "longitude": "-110.36256580",
    "timezones": ["MST (UTC-07)"],
    "ianaTimezones": ["US/Mountain"]
  },
  {
    "name": "Nebraska",
    "abbreviation": "NE",
    "latitude": "41.49253740",
    "longitude": "-99.90181310",
    "timezones": ["CST (UTC-6)", "MST (UTC-07)"],
    "ianaTimezones": ["US/Central", "US/Mountain"]
  },
  {
    "name": "Nevada",
    "abbreviation": "NV",
    "latitude": "38.80260970",
    "longitude": "-116.41938900",
    "timezones": ["PST (UTC-8)", "MST (UTC-07)"],
    "ianaTimezones": ["US/Pacific", "US/Mountain"]
  },
  {
    "name": "New Hampshire",
    "abbreviation": "NH",
    "latitude": "43.19385160",
    "longitude": "-71.57239530",
    "timezones": ["EST (UTC-5)"],
    "ianaTimezones": ["US/Eastern"]
  },
  {
    "name": "New Jersey",
    "abbreviation": "NJ",
    "latitude": "40.05832380",
    "longitude": "-74.40566120",
    "timezones": ["EST (UTC-5)"],
    "ianaTimezones": ["US/Eastern"]
  },
  {
    "name": "New Mexico",
    "abbreviation": "NM",
    "latitude": "34.51994020",
    "longitude": "-105.87009010",
    "timezones": ["MST (UTC-07)"],
    "ianaTimezones": ["US/Mountain"]
  },
  {
    "name": "New York",
    "abbreviation": "NY",
    "latitude": "40.71277530",
    "longitude": "-74.00597280",
    "timezones": ["EST (UTC-5)"],
    "ianaTimezones": ["US/Eastern"]
  },
  {
    "name": "North Carolina",
    "abbreviation": "NC",
    "latitude": "35.75957310",
    "longitude": "-79.01929970",
    "timezones": ["EST (UTC-5)"],
    "ianaTimezones": ["US/Eastern"]
  },
  {
    "name": "North Dakota",
    "abbreviation": "ND",
    "latitude": "47.55149260",
    "longitude": "-101.00201190",
    "timezones": ["CST (UTC-6)", "MST (UTC-07)"],
    "ianaTimezones": ["US/Central", "US/Mountain"]
  },
  {
    "name": "Ohio",
    "abbreviation": "OH",
    "latitude": "40.41728710",
    "longitude": "-82.90712300",
    "timezones": ["EST (UTC-5)"],
    "ianaTimezones": ["US/Eastern"]
  },
  {
    "name": "Oklahoma",
    "abbreviation": "OK",
    "latitude": "35.46756020",
    "longitude": "-97.51642760",
    "timezones": ["CST (UTC-6)"],
    "ianaTimezones": ["US/Central"]
  },
  {
    "name": "Oregon",
    "abbreviation": "OR",
    "latitude": "43.80413340",
    "longitude": "-120.55420120",
    "timezones": ["PST (UTC-8)", "MST (UTC-07)"],
    "ianaTimezones": ["US/Pacific", "US/Mountain"]
  },
  {
    "name": "Pennsylvania",
    "abbreviation": "PA",
    "latitude": "41.20332160",
    "longitude": "-77.19452470",
    "timezones": ["EST (UTC-5)"],
    "ianaTimezones": ["US/Eastern"]
  },
  {
    "name": "Rhode Island",
    "abbreviation": "RI",
    "latitude": "41.58009450",
    "longitude": "-71.47742910",
    "timezones": ["EST (UTC-5)"],
    "ianaTimezones": ["US/Eastern"]
  },
  {
    "name": "South Carolina",
    "abbreviation": "SC",
    "latitude": "33.83608100",
    "longitude": "-81.16372450",
    "timezones": ["EST (UTC-5)"],
    "ianaTimezones": ["US/Eastern"]
  },
  {
    "name": "South Dakota",
    "abbreviation": "SD",
    "latitude": "43.96951480",
    "longitude": "-99.90181310",
    "timezones": ["CST (UTC-6)", "MST (UTC-07)"],
    "ianaTimezones": ["US/Central", "US/Mountain"]
  },
  {
    "name": "Tennessee",
    "abbreviation": "TN",
    "latitude": "35.51749130",
    "longitude": "-86.58044730",
    "timezones": ["CST (UTC-6)", "EST (UTC-5)"],
    "ianaTimezones": ["US/Central", "US/Eastern"]
  },
  {
    "name": "Texas",
    "abbreviation": "TX",
    "latitude": "31.96859880",
    "longitude": "-99.90181310",
    "timezones": ["CST (UTC-6)", "MST (UTC-07)"],
    "ianaTimezones": ["US/Central", "US/Mountain"]
  },
  {
    "name": "Utah",
    "abbreviation": "UT",
    "latitude": "39.32098010",
    "longitude": "-111.09373110",
    "timezones": ["MST (UTC-07)"],
    "ianaTimezones": ["US/Mountain"]
  },
  {
    "name": "Vermont",
    "abbreviation": "VT",
    "latitude": "44.55880280",
    "longitude": "-72.57784150",
    "timezones": ["EST (UTC-5)"],
    "ianaTimezones": ["US/Eastern"]
  },
  {
    "name": "Virginia",
    "abbreviation": "VA",
    "latitude": "37.43157340",
    "longitude": "-78.65689420",
    "timezones": ["EST (UTC-5)"],
    "ianaTimezones": ["US/Eastern"]
  },
  {
    "name": "Washington",
    "abbreviation": "WA",
    "latitude": "47.75107410",
    "longitude": "-120.74013850",
    "timezones": ["PST (UTC-8)"],
    "ianaTimezones": ["US/Pacific"]
  },
  {
    "name": "West Virginia",
    "abbreviation": "WV",
    "latitude": "38.59762620",
    "longitude": "-80.45490260",
    "timezones": ["EST (UTC-5)"],
    "ianaTimezones": ["US/Eastern"]
  },
  {
    "name": "Wisconsin",
    "abbreviation": "WI",
    "latitude": "43.78443970",
    "longitude": "-88.78786780",
    "timezones": ["CST (UTC-6)"],
    "ianaTimezones": ["US/Central"]
  },
  {
    "name": "Wyoming",
    "abbreviation": "WY",
    "latitude": "43.07596780",
    "longitude": "-107.29028390",
    "timezones": ["MST (UTC-07)"],
    "ianaTimezones": ["US/Mountain"]
  }
]

df = {}

def mount_charts_data():
    request = requests.post("http://localhost:5000/api/v1/disaster/predict", data={

    })
    data = request.json()

    aggregated = {
        "state": [],
        "declarationType": [],
        "incidentType": [],
        "Precipitation": [],
        "Cooling_Days": [],
        "Heating_Days": [],
        "AverageTemp": [],
        "Real": [],
        "Predicted": [],
        "Year": [],
        "Latitude": [],
        "Longitude": []
    }

    for value in data:
        stateData = next((state for state in states if state["abbreviation"] == value["state"]), {})
        
        aggregated["state"].append(value["state"])
        aggregated["declarationType"].append(value["declarationType"])
        aggregated["incidentType"].append(value["incidentType"])
        aggregated["Precipitation"].append(value["Precipitation"])
        aggregated["Cooling_Days"].append(value["Cooling_Days"])
        aggregated["Heating_Days"].append(value["Heating_Days"])
        aggregated["AverageTemp"].append(value["AverageTemp"])
        aggregated["Real"].append(value["incidentType"])  # Aqui Real é igual a incidentType
        aggregated["Predicted"].append(value["incidentType"])  # Mesmo para Predicted
        aggregated["Year"].append(value["year"])
        aggregated["Latitude"].append(stateData.get("latitude"))
        aggregated["Longitude"].append(stateData.get("longitude"))

    df = pd.DataFrame(aggregated)

# mount_charts_data()

# df = pd.DataFrame({
#     "state": ["TX", "FL", "CA", "NY", "TX", "FL"],
#     "declarationType": ["DR", "DR", "EM", "DR", "EM", "DR"],
#     "incidentType": ["Flood", "Hurricane", "Snowstorm", "Severe Storm", "Flood", "Hurricane"],
#     "Precipitation": [12.3, 15.2, 8.1, 10.5, 13.4, 17.8],
#     "Cooling_Days": [45, 50, 30, 35, 40, 55],
#     "Heating_Days": [10, 15, 20, 25, 5, 10],
#     "AverageTemp": [22.5, 25.6, 18.2, 20.3, 23.1, 26.4],
#     "Real": ["Flood", "Hurricane", "Snowstorm", "Severe Storm", "Flood", "Hurricane"],
#     "Predicted": ["Flood", "Hurricane", "Snowstorm", "Flood", "Severe Storm", "Hurricane"],
#     "Year": [2020, 2020, 2021, 2021, 2022, 2023],
#     "Latitude": [31.9686, 27.9944, 36.7783, 43.2994, 31.9686, 27.9944],
#     "Longitude": [-99.9018, -81.7603, -119.4179, -74.2179, -99.9018, -81.7603]
# })

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Análise de Incidentes Naturais nos EUA"),
    
    dcc.Dropdown(
        id="year-dropdown",
        options=[{"label": str(year), "value": year} for year in df["Year"].unique()],
        value=df["Year"].min(),
        placeholder="Selecione o ano"
    ),

    dcc.Graph(id="real-vs-predicted"),
    dcc.Graph(id="incident-frequency"),
    dcc.Graph(id="climate-analysis"),
    dcc.Graph(id="model-performance"),
    dcc.Graph(id="incident-map")
])

@app.callback(
    [Output("real-vs-predicted", "figure"),
     Output("incident-frequency", "figure"),
     Output("climate-analysis", "figure"),
     Output("model-performance", "figure"),
     Output("incident-map", "figure")],
    [Input("year-dropdown", "value")]
)
def update_graphs(selected_year):
    filtered_df = df[df["Year"] == selected_year]
    
    real_vs_predicted = px.bar(filtered_df, x="incidentType", barmode="group", 
                               y=["Real", "Predicted"],
                               title="Comparação: Incidentes Reais vs. Previstos")
    
    incident_frequency = px.histogram(filtered_df, x="incidentType", color="state",
                                      title="Frequência de Tipos de Incidentes por Estado")
    
    climate_analysis = px.scatter(filtered_df, x="AverageTemp", y="Precipitation", 
                                   size="Cooling_Days", color="incidentType",
                                   hover_data=["Heating_Days"],
                                   title="Temperatura Média vs. Precipitação")
    
    filtered_df["Correct"] = filtered_df["Real"] == filtered_df["Predicted"]
    model_performance = px.pie(filtered_df, names="Correct", 
                               title="Precisão do Modelo",
                               color_discrete_map={True: "green", False: "red"})
    
    incident_map = px.scatter_geo(
        filtered_df,
        lat="Latitude",
        lon="Longitude",
        color="incidentType",
        size="Precipitation",
        hover_name="state",
        hover_data={"AverageTemp": True, "Precipitation": True},
        title=f"Incidentes Naturais nos EUA ({selected_year})",
        scope="usa"
    )
    incident_map.update_layout(geo=dict(showland=True, landcolor="lightgray"))
    
    return real_vs_predicted, incident_frequency, climate_analysis, model_performance, incident_map

if __name__ == "__main__":
    app.run_server(debug=True)