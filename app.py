import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load processed data
df = pd.read_csv("data/processed_sales.csv")
df['date'] = pd.to_datetime(df['date'])

# Create line chart
fig = px.line(
    df.groupby("date", as_index=False).sum(),
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

# Build Dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales Visualiser", style={"textAlign": "center"}),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)
