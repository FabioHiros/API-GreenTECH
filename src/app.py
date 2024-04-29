from dash_app import app as dash_app
from flask import Flask, render_template, request

app = Flask(__name__)

# Rotas do Flask
selected_type=None
@app.route("/")
def home() -> str:
    """Carrega a página home e retorna o valor 'home' \n
        Não recebe nenhuma entrada de dados"""

    return render_template('index.html', current_page="home")

@app.route("/grafico", methods=["POST","GET"])
def chart() -> str:
    """
    Carrega a página dos gráficos e retorna o valor 'chart' \n
    Não recebe entrada de dados
    """

    dash_content=dash_app.index()
    return render_template('grafico.html',current_page="chart",dash_content=dash_content)

dash_app.config.suppress_callback_exceptions = True
dash_app.init_app(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)