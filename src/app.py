from static.charts.dash_app import app as dash_app
from flask import Flask, render_template

app = Flask(__name__)

# Rotas do Flask

@app.route("/")
def home():
    return render_template('index.html', current_page="home")

@app.route("/grafico")
def chart():
    return render_template('grafico.html',current_page="chart")

dash_app.config.suppress_callback_exceptions = True
dash_app.init_app(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)