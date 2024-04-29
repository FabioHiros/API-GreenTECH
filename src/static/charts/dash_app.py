from dash import Dash, html, dash_table, dcc, Input, Output, callback
import plotly.graph_objects as go
import pandas as pd
from datetime import date

app = Dash(__name__, url_base_pathname="/dash/")

# Read the CSV file and convert 'datahora' column to datetime
dados = pd.read_csv('./static/charts/dadosensores_media.csv')
dados['datahora'] = pd.to_datetime(dados['datahora'])

# Initial date range
start_date_default = '2023-09-12'
end_date_default = '2023-09-15'

# Create the initial figure
fig = go.Figure()

# Update the layout
fig.update_layout(
    title="Data Analysis",
    xaxis_title="Data",
    yaxis_title="Valores",
    showlegend=True,
    autosize=True,
    margin=dict(l=60,r=60,t=60,b=60)
)

# Define layout
app.layout = html.Div([
    dcc.DatePickerRange(
    id='my-date-picker-range',
    min_date_allowed=date(2023, 9, 12),
    max_date_allowed=date(2023, 12, 31),
    initial_visible_month=date(2023, 9, 12),
    start_date=start_date_default,
    end_date=end_date_default,
    minimum_nights=0
),
    html.Div(id='output-container-date-picker-range'),
    dcc.Graph(id='id_media', figure=fig,style={'height': '90vh',"widht":'100px'}),
    dash_table.DataTable(data=dados.to_dict('records'), page_size=10)
])


# Callback to update the graph based on the selected date range
@app.callback(
    Output('id_media', 'figure'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date')
)
def update_graph(start_date, end_date):
    start_date = pd.to_datetime(start_date)  # Convert to datetime64[ns]
    end_date = pd.to_datetime(end_date) + pd.DateOffset(days=1)  # Convert to datetime64[ns] and add one day
    print("Selected Date Range:", start_date, "-", end_date)
    
    # print(start_date)
    # print(end_date)
    # Filter the DataFrame based on the selected date range
    dados_filtered = filter_data(dados, start_date, end_date)
    print(dados_filtered)
    # Create the updated Plotly figure
    updated_fig = create_figure(dados_filtered)
    
    return updated_fig


# Function to filter DataFrame based on date range
def filter_data(df, start_date, end_date):
    return df[(df['datahora'] >= start_date) & (df['datahora'] < end_date)]


# Function to create Plotly figure
def create_figure(df):
    fig = go.Figure(data=[
        go.Bar(name='Umidade Solo', x=df['datahora'], y=df['umidade_solo'], marker=dict(color='orange')),
        go.Bar(name='Umidade Ambiente', x=df['datahora'], y=df['umidade_ambiente'], marker=dict(color='green')),
        go.Bar(name='Temperatura', x=df['datahora'], y=df['temperatura'], marker=dict(color='red')),
        go.Bar(name='Volume de Água', x=df['datahora'], y=df['volume_agua'], marker=dict(color='navy'))
    ])

    # Add traces for line plots
    fig.add_trace(go.Scatter(x=df['datahora'], y=df['umidade_solo'], mode='lines', name='Umidade Solo Line', line=dict(color='orange')))
    fig.add_trace(go.Scatter(x=df['datahora'], y=df['umidade_ambiente'], mode='lines', name='Umidade Ambiente Line', line=dict(color='green')))
    fig.add_trace(go.Scatter(x=df['datahora'], y=df['temperatura'], mode='lines', name='Temperatura Line', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=df['datahora'], y=df['volume_agua'], mode='lines', name='Volume de Água Line', line=dict(color='navy')))
    
    # Update the layout
    fig.update_layout(title="Data Analysis", xaxis_title="Data", yaxis_title="Valores", showlegend=True)
    
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
