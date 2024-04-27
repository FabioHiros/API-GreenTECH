import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash
from flask import Flask, render_template

 
server = Flask(__name__)

 
app = Dash(__name__, server=server)

 
df = pd.read_csv('dadosensores_media.csv')  

 
 
df = pd.DataFrame({
    "media": ["umidade do solo", "umidade do solo", "umidade do solo", "umidade do solo", "umidade do solo",
              "umidade do ambiente", "umidade do ambiente", "umidade do ambiente", "umidade do ambiente", "umidade do ambiente",
              "temperatura", "temperatura", "temperatura", "temperatura", "temperatura",
              "volume da agua", "volume da agua", "volume da agua", "volume da agua", "volume da agua"],
    "dia": ["segunda", "terça", "quarta", "quinta", "sexta", "segunda", "terça", "quarta", "quinta", "sexta",
            "segunda", "terça", "quarta", "quinta", "sexta", "segunda", "terça", "quarta", "quinta", "sexta"],
    "horario": [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4],
    "valor": [10, 20, 30, 25, 35, 15, 25, 20, 30, 35, 20, 22, 24, 26, 28, 50, 55, 60, 65, 70],
})

 
fig = px.line(df, x='dia', y='horario', color='media')

# Layout do Dash
app.layout = html.Div(children=[
    html.H1(children='Gráfico de média de umidade'),
    html.Div(children='Média de umidade do solo e do ambiente'),
    
    dcc.Graph(
        id='id_media',
        figure=fig
    ),
])

# Rotas do Flask

@server.route("/")
def home():
    return render_template('index.html')

@server.route("/grafico.html")
def chart():
    return app.grafico('grafico.html')


if __name__ == "__main__":
    server.run(host='0.0.0.0', port=5000, debug=True)
