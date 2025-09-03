import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load processed data
df = pd.read_csv("data/processed_sales.csv")
df['date'] = pd.to_datetime(df['date'])

# Dash app setup
app = dash.Dash(__name__)

app.layout = html.Div(style={"fontFamily": "Arial", "backgroundColor": "#f9f9f9", "padding": "20px"}, children=[
    html.H1("Pink Morsel Sales Visualiser", style={"textAlign": "center", "color": "#E91E63"}),

    html.Div([
        html.Label("Select a region:", style={"fontSize": "18px", "marginBottom": "10px"}),
        dcc.RadioItems(
            id="region-selector",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={"marginBottom": "20px"}
        ),
    ]),

    dcc.Graph(id="sales-line-chart")
])

# Callback to update chart based on region selection
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-selector", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"].str.lower() == selected_region]

    fig = px.line(
        filtered_df.groupby("date", as_index=False).sum(),
        x="date",
        y="sales",
        title=f"Pink Morsel Sales Over Time ({selected_region.capitalize()})"
    )
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#f9f9f9",
        font=dict(color="#333", size=14),
        title_x=0.5
    )
    return fig

if __name__ == "__main__":
    app.run(debug=True)
