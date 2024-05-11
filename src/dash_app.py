from connect_db import connect
from dash import Dash, html, dash_table, dcc, Input, Output
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime,timedelta
import dash_bootstrap_components as dbc

app = Dash(__name__, url_base_pathname="/dash/", meta_tags=[{'name': 'viewport',
                                                             'content': 'width=device-width, initial-scale=1.0, maximun-scale=1.2, minimun-scale=0.5'}])

def filter_data(df, start_date, end_date):
    return df[(df['datahora'] >= start_date) & (df['datahora'] < end_date)]

def create_figures(dados):
    if dados.empty:
        # If there's no data, return empty figures
        fig_main = go.Figure()
        fig_solo = go.Figure()
        fig_temperatura = go.Figure()
        fig_ambiente = go.Figure()
        fig_agua = go.Figure()
    else:
        fig_main = go.Figure(data=[
        go.Bar(name='Umidade Solo', x=dados['datahora'], y=dados['umidade_solo'], marker=dict(color='orange'), legendgroup='solo'),
        go.Scatter(x=dados['datahora'], y=dados['umidade_solo'], mode='lines', name='Umidade Solo Line', line=dict(color='orange'), showlegend=False, legendgroup='solo'),

        go.Bar(name='Umidade Ambiente', x=dados['datahora'], y=dados['umidade_ambiente'], marker=dict(color='green'), legendgroup='ambiente'),
        go.Scatter(x=dados['datahora'], y=dados['umidade_ambiente'], mode='lines', name='Umidade Ambiente Line', line=dict(color='green'), showlegend=False, legendgroup='ambiente'),

        go.Bar(name='Temperatura', x=dados['datahora'], y=dados['temperatura'], marker=dict(color='red'), legendgroup='temperatura'),
        go.Scatter(x=dados['datahora'], y=dados['temperatura'], mode='lines', name='Temperatura Line', line=dict(color='red'), showlegend=False, legendgroup='temperatura'),

        go.Bar(name='Volume de Água', x=dados['datahora'], y=dados['volume_agua'], marker=dict(color='navy'), legendgroup='agua'),
        go.Scatter(x=dados['datahora'], y=dados['volume_agua'], mode='lines', name='Volume de Água Line', line=dict(color='navy'), showlegend=False, legendgroup='agua')
        ])

        fig_main.update_layout(title="",
                        xaxis_title="Data", yaxis_title="Valores", legend=dict(
                        orientation="h", # "h" for horizontal, "v" for vertical
                        yanchor="bottom", # Positioning anchor for the y-axis
                        y=1.02, # Adjust as needed, 1.02 for moving it slightly above the plot
                        xanchor="right", # Positioning anchor for the x-axis
                        x=1 ,# Adjust as needed, 1 for moving it to the right of the plot
                    entrywidthmode='fraction'
                    ))

        #Figs da esquerda
        fig_solo = go.Figure(data=[
            go.Bar(name='Umidade Solo', x=dados['datahora'], y=dados['umidade_solo'], marker=dict(color='orange')),
            go.Scatter(x=dados['datahora'], y=dados['umidade_solo'], mode='lines', name='Umidade Solo', line=dict(color='orange'))
        ])
        fig_solo.update_layout(title="Umidade Solo", showlegend=False, dragmode=False)

        fig_temperatura = go.Figure(data=[
            go.Bar(name='Temperatura', x=dados['datahora'], y=dados['temperatura'], marker=dict(color='red')),
            go.Scatter(x=dados['datahora'], y=dados['temperatura'], mode='lines', name='Temperatura', line=dict(color='red'))
        ])
        fig_temperatura.update_layout(title="Temperatura", showlegend=False, dragmode=False)

        #Figs da Direita
        fig_ambiente = go.Figure(data=[
            go.Bar(name='Umidade Ambiente', x=dados['datahora'], y=dados['umidade_ambiente'], marker=dict(color='green')),
            go.Scatter(x=dados['datahora'], y=dados['umidade_ambiente'], mode='lines', name='Umidade Ambiente', line=dict(color='green'))
        ])
        fig_ambiente.update_layout(title="Umidade Ambiente", showlegend=False, dragmode=False)

        fig_agua = go.Figure(data=[
            go.Bar(name="Volume d'Água", x=dados['datahora'], y=dados['volume_agua'], marker=dict(color='navy')),
            go.Scatter(x=dados['datahora'], y=dados['volume_agua'], mode='lines', name="Volume d'Água", line=dict(color='navy'))
        ])
        fig_agua.update_layout(title="Volume d'Água", showlegend=False, dragmode=False)
        
    return fig_main, fig_solo, fig_temperatura, fig_ambiente, fig_agua

engine=connect()
available_dates=pd.read_sql("SELECT DISTINCT DATE(datahora) AS available_date FROM estufa;", engine)
if available_dates.empty:
    engine.dispose()
    start_date = datetime.now() - timedelta(days=7)
    end_date = datetime.now()
    selected_days = pd.DataFrame()
    available_dates = pd.DataFrame({'available_date': [start_date, end_date]})
else:
    seven_days = available_dates['available_date'].max() - timedelta(days=7)
    selected_days = pd.read_sql(f"SELECT * FROM estufa WHERE datahora >= '{seven_days}'", engine)
    engine.dispose()

fig_main, fig_solo, fig_temperatura, fig_ambiente, fig_agua = create_figures(selected_days)

def initialize_date_picker_and_graphs():
    engine = connect()
    available_dates_df = pd.read_sql("SELECT DISTINCT DATE(datahora) AS available_date FROM estufa;", engine)

    if available_dates_df.empty:
        # If there's no data in the database, return default start and end dates
        engine.dispose()
        return datetime.now() - timedelta(days=7), datetime.now()
    else:
        seven_days = available_dates_df['available_date'].max() - timedelta(days=7)
        selected_days_df = pd.read_sql(f"SELECT * FROM estufa WHERE datahora >= '{seven_days}'", engine)
        engine.dispose()
        start_date = selected_days_df['datahora'].min()
        end_date = selected_days_df['datahora'].max()
        return start_date, end_date

@app.callback(
    [Output('my-date-picker-range', 'start_date'),
     Output('my-date-picker-range', 'end_date')],
    [Input('app-layout', 'children')]
)
def update_available_dates(n):
    return initialize_date_picker_and_graphs()

#     return available_dates, start_date, end_date

    # Layout do Dash
app.layout = html.Div(id='app-layout', children=[
    html.Div([
    dcc.DatePickerRange(
    id='my-date-picker-range',
        min_date_allowed=available_dates['available_date'].min(),
        max_date_allowed=available_dates['available_date'].max(),
        initial_visible_month=initialize_date_picker_and_graphs()[1],
        start_date=initialize_date_picker_and_graphs()[0],
        end_date=initialize_date_picker_and_graphs()[1],
        # disabled_days=[date for date in pd.date_range(start=available_dates['available_date'].min(), end=available_dates['available_date'].max()) if date.date() not in available_dates['available_date']]
    ),
    html.Div(id='output-container-date-picker-range'),
    dcc.Graph(
        id='id_main',
        figure=fig_main,
        config={
                'displaylogo': False
                
        }
    ),
    html.Div(
    dash_table.DataTable(data=selected_days.to_dict('records'), page_size=5 ),id="table-wrap")
    ],style={'width': '100%'}),
    dbc.Row([
        dbc.Col([
        dcc.Graph(
            id='id_solo',
            figure=fig_solo,
            config={
                    'displayModeBar': False
            }
        ),
        dcc.Graph(
            id='id_temp',
            figure=fig_temperatura,
            config={
                    'displayModeBar': False
            }
        )],style={'width': '50%', 'min-width':'22rem'}),
        dbc.Col([
        dcc.Graph(
            id='id_ambiente',
            figure=fig_ambiente,
            config={
                    'displayModeBar': False
            }
        ),
        dcc.Graph(
            id='id_agua',
            figure=fig_agua,
            config={
                    'displayModeBar': False
            }
        )],style={'width': '50%', 'min-width':'22rem'})
    ],style={'width': '100%'})
],style={'width': '100%', 'min-width':'400px'})

@app.callback(
    [Output('id_main', 'figure'),
     Output('id_solo', 'figure'),
     Output('id_temp', 'figure'),
     Output('id_ambiente', 'figure'),
     Output('id_agua', 'figure'),
     Output("table-wrap", "children")],
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date')
)
def update_graph(start_date, end_date):
    engine=connect()
    if start_date and end_date:
        sql_query = f"SELECT * FROM estufa WHERE DATE(datahora) BETWEEN '{start_date}' AND '{end_date}'"
        selected_days = pd.read_sql(sql_query, engine)
    else:
        selected_days = pd.DataFrame()
    # Create the updated Plotly figure
    fig_main, fig_solo, fig_temperatura, fig_ambiente, fig_agua  = create_figures(selected_days)

    # Create/update the Dash table with filtered data
    table = dash_table.DataTable(data=selected_days.to_dict('records'), page_size=5)
    engine.dispose()
    return fig_main, fig_solo, fig_temperatura, fig_ambiente, fig_agua, table