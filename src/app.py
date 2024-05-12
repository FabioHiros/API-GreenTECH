# app.py
from connect_db import connect
from dash_app import app as dash_app
from flask import Flask, render_template, request, make_response, jsonify
import pandas as pd
import os

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = {'csv'}

# Establish the database connection
estufadb = connect()

@app.errorhandler(413)
def too_large(e):
    return make_response(jsonify(message="Arquivo muito grande!"), 413)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def update_file(file):
    try:
        new_data=pd.read_csv(file)
        new_data.to_sql(name='estufa', con=estufadb, if_exists='append', index=False)
        print("Data appended successfully.")
    except Exception as e:
        print("Error appending data:", e)

# Rotas do Flask
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

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' in request.files:
        file = request.files['file']
        if file and allowed_file(file.filename):
            update_file(file)
            return jsonify({'message': 'Upload feito com sucesso!'})

    return jsonify({'message': 'Upload falhou!'}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
