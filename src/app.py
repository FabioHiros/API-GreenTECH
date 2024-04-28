import pandas as pd
import plotly.graph_objects as go
from dash import dcc, html, Dash
from flask import Flask, render_template

app = Flask(__name__)
dash = Dash(__name__, server=app,url_base_pathname='/grafico/')

def puxa_dados():
    dados=pd.read_csv('dadosensores_media.csv')
    dados['datahora']=pd.to_datetime(dados['datahora'])

    # Seleciona Ano e Mês
    desired_year = 2023
    desired_month = 10 

    # Filtrando baseado no ano e mês
    dados_filtered = dados[(dados['datahora'].dt.year == desired_year) & (dados['datahora'].dt.month == desired_month)]

    # Calculando média do dia ('d')
    dados=dados_filtered.resample('d', on='datahora').mean().reset_index()
    
    # Puxando as colunas e adicionando barras baseado nos valores obtidos
    fig = go.Figure(data=[
        go.Bar(name='Umidade Solo', x=dados['datahora'], y=dados['umidade_solo']),
        go.Bar(name='Umidade Ambiente', x=dados['datahora'], y=dados['umidade_ambiente']),
        go.Bar(name='Temperatura', x=dados['datahora'], y=dados['temperatura']),
        go.Bar(name='Volume de Água', x=dados['datahora'], y=dados['volume_agua'])
    ])

    # Não sei, mas precisa disso
    fig.update_layout(title="Data Analysis",
                    xaxis_title="Data", yaxis_title="Valores", showlegend=True)
    
    return fig

# Layout do Dash
dash.layout = html.Div(children=[
    dcc.Graph(
        id='id_media',
        figure=puxa_dados(),
        config={'modeBarButtonsToRemove': ['zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d', 'hoverClosestCartesian', 'hoverCompareCartesian']}
    ),
])

# Rotas do Flask

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/grafico")
def chart():
    fig=puxa_dados()
    chart_html = fig.to_json()
    return render_template('grafico.html',chart=chart_html)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)