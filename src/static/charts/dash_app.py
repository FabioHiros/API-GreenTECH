from dash import Dash, html, dash_table, dcc
import plotly.graph_objects as go
import pandas as pd

app = Dash(__name__, url_base_pathname="/dash/")


dados=pd.read_csv('./static/charts/dadosensores_media.csv')
dados['datahora']=pd.to_datetime(dados['datahora'])

    # Seleciona Ano e Mês
desired_year = 2023
desired_month = 12
desired_day = [3,9]

    # Filtrando baseado no ano e mês
if desired_month==0:
    dados = dados[(dados['datahora'].dt.year == desired_year)]
elif not desired_day:
    dados = dados[(dados['datahora'].dt.year == desired_year) & (dados['datahora'].dt.month == desired_month)]
else:
    dados = dados[(dados['datahora'].dt.year == desired_year) & (dados['datahora'].dt.month == desired_month) & (dados['datahora'].dt.day.between(desired_day[0], desired_day[1]))]

    # Calculando média do dia ('d')
    # dados=dados.resample('d', on='datahora').mean().reset_index()
        
    # Puxando as colunas e adicionando barras baseado nos valores obtidos
fig = go.Figure(data=[
    go.Bar(name='Umidade Solo', x=dados['datahora'], y=dados['umidade_solo'], marker=dict(color='orange')),
    go.Bar(name='Umidade Ambiente', x=dados['datahora'], y=dados['umidade_ambiente'], marker=dict(color='green')),
    go.Bar(name='Temperatura', x=dados['datahora'], y=dados['temperatura'], marker=dict(color='red')),
    go.Bar(name='Volume de Água', x=dados['datahora'], y=dados['volume_agua'], marker=dict(color='navy'))
])

fig.add_trace(go.Scatter(x=dados['datahora'], y=dados['umidade_solo'], mode='lines', name='Umidade Solo Line', line=dict(color='orange')))
fig.add_trace(go.Scatter(x=dados['datahora'], y=dados['umidade_ambiente'], mode='lines', name='Umidade Ambiente Line', line=dict(color='green')))
fig.add_trace(go.Scatter(x=dados['datahora'], y=dados['temperatura'], mode='lines', name='Temperatura Line', line=dict(color='red')))
fig.add_trace(go.Scatter(x=dados['datahora'], y=dados['volume_agua'], mode='lines', name='Volume de Água Line', line=dict(color='navy')))
        
    # Não sei, mas precisa disso
fig.update_layout(title="Data Analysis",
                  xaxis_title="Data", yaxis_title="Valores", showlegend=True)

    # Layout do Dash
app.layout = html.Div([
    dcc.Graph(
        id='id_media',
        figure=fig
    ),
    dash_table.DataTable(data=dados.to_dict('records'), page_size=10)
])