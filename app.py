"""
app.py
Entry point for the Grazioso Salvare rescue animal dashboard.
Run with: python app.py

Author: Avantika Banerjee
CS-340 | CS-499 Enhancement One
"""

import pandas as pd
import dash_leaflet as dl
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

from data import get_db, fetch_filtered_data, get_map_coordinates
from layout import build_layout

# Connect to the database and load the initial dataset
db = get_db()
initial_df = fetch_filtered_data(db, "Reset")

app = Dash(__name__)
app.title = "Grazioso Salvare Dashboard"
app.layout = build_layout(initial_df)


@app.callback(
    Output("datatable-id", "data"),
    Input("filter-type", "value"),
)
def update_table(filter_type):
    # Re-query the database when the rescue type filter changes
    df = fetch_filtered_data(db, filter_type)
    if df.empty:
        return []
    return df.to_dict("records")


@app.callback(
    Output("graph-id", "children"),
    Input("datatable-id", "derived_virtual_data"),
)
def update_chart(view_data):
    # Display the breeds of animals currently visible in the data table
    if not view_data:
        return [html.P("No data to display.", style={"padding": "20px", "color": "gray"})]

    dff = pd.DataFrame.from_dict(view_data)

    if "breed" not in dff.columns:
        return []

    breed_counts = dff["breed"].value_counts().reset_index()
    breed_counts.columns = ["breed", "count"]

    fig = px.pie(
        breed_counts,
        names="breed",
        values="count",
        title="Breed Distribution",
        color_discrete_sequence=px.colors.sequential.Cividis,
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")

    return [dcc.Graph(figure=fig)]


@app.callback(
    Output("datatable-id", "style_data_conditional"),
    Input("datatable-id", "selected_columns"),
)
def update_styles(selected_columns):
    # Highlight the selected column with a light blue background
    return [
        {"if": {"column_id": i}, "background_color": "#D2F3FF"}
        for i in (selected_columns or [])
    ]


@app.callback(
    Output("map-id", "children"),
    [
        Input("datatable-id", "derived_virtual_data"),
        Input("datatable-id", "derived_virtual_selected_rows"),
    ],
)
def update_map(view_data, index):
    # Update the map marker to the location of the selected animal
    default_map = [
        dl.Map(style={"width": "1000px", "height": "500px"},
               center=[30.75, -97.48], zoom=10,
               children=[dl.TileLayer(id="base-layer-id")])
    ]

    if not view_data:
        return default_map

    dff = pd.DataFrame.from_dict(view_data)

    row = 0
    if index and len(index) > 0:
        row = index[0]

    lat, lon, breed, name = get_map_coordinates(dff, row)

    return [
        dl.Map(style={"width": "1000px", "height": "500px"},
               center=[lat, lon], zoom=10,
               children=[
                   dl.TileLayer(id="base-layer-id"),
                   dl.Marker(position=[lat, lon], children=[
                       dl.Tooltip(breed),
                       dl.Popup([html.H4("Animal Name"), html.P(name)]),
                   ]),
               ])
    ]


if __name__ == "__main__":
    app.run(debug=True)
