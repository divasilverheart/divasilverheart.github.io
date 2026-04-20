"""
layout.py
Dash layout for the Grazioso Salvare rescue animal dashboard.

Author: Avantika Banerjee
CS-340 | CS-499 Enhancement One
"""

import base64
import os
from dash import dcc, html, dash_table


def _encode_logo(image_path):
    # Returns base64-encoded logo string, or None if the file is missing.
    if not os.path.isfile(image_path):
        print(f"Warning: logo file not found at '{image_path}'. Skipping logo.")
        return None
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def build_layout(df, logo_path="Grazioso Salvare Logo.png"):
    """Build and return the full dashboard layout."""
    encoded_logo = _encode_logo(logo_path)

    logo_element = html.Div()
    if encoded_logo:
        logo_element = html.Center(
            html.A(
                href="https://www.snhu.edu",
                target="_blank",
                children=[
                    html.Img(
                        src=f"data:image/png;base64,{encoded_logo}",
                        style={"height": "150px"},
                    )
                ],
            )
        )

    return html.Div([
        html.Center(html.B(html.H1("CS-340 Dashboard"))),
        logo_element,
        html.P(
            "Avantika Banerjee | CS-340 | SNHU",
            style={"textAlign": "right", "paddingRight": "30px",
                   "color": "gray", "fontSize": "0.9rem"},
        ),
        html.Hr(),

        # Filter controls
        html.Div(
            style={"padding": "15px 30px", "backgroundColor": "#f8f9fa"},
            children=[
                html.H4("Filter by Rescue Type", style={"color": "#2c3e50"}),
                dcc.RadioItems(
                    id="filter-type",
                    options=[
                        {"label": "  Water Rescue",                    "value": "Water Rescue"},
                        {"label": "  Mountain or Wilderness Rescue",   "value": "Mountain or Wilderness"},
                        {"label": "  Disaster or Individual Tracking", "value": "Disaster or Individual Tracking"},
                        {"label": "  Reset (Show All)",                "value": "Reset"},
                    ],
                    value="Reset",
                    inline=True,
                    inputStyle={"marginRight": "6px"},
                    labelStyle={"marginRight": "25px", "fontSize": "1rem"},
                ),
            ],
        ),
        html.Hr(),

        # Data table
        dash_table.DataTable(
            id="datatable-id",
            columns=[{"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns],
            data=df.to_dict("records"),
            editable=False,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            column_selectable="single",
            row_selectable="single",
            row_deletable=False,
            selected_columns=[],
            selected_rows=[0],
            page_action="native",
            page_current=0,
            page_size=10,
            style_table={"overflowX": "auto"},
            style_cell={
                "textAlign": "left",
                "padding": "8px",
                "minWidth": "80px",
                "maxWidth": "180px",
                "overflow": "hidden",
                "textOverflow": "ellipsis",
            },
            style_header={
                "backgroundColor": "#2c3e50",
                "color": "white",
                "fontWeight": "bold",
            },
            style_data_conditional=[
                {"if": {"row_index": "odd"}, "backgroundColor": "#f2f2f2"}
            ],
        ),
        html.Br(),
        html.Hr(),

        # Chart and map side by side
        html.Div(
            className="row",
            style={"display": "flex"},
            children=[
                html.Div(id="graph-id", className="col s12 m6"),
                html.Div(id="map-id",   className="col s12 m6"),
            ],
        ),
    ])
