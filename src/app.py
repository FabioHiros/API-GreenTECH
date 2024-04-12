from flask import Flask, render_template, request

app = Flask("__name__")

@app.route("/")
def home():
    return render_template('index.html', current_page='home')

@app.route("/chart")
def chart():
    return render_template('grafico.html', current_page='chart')

@app.route("/agua")
def agua():
    return render_template('agua.html', current_page='agua')

@app.route("/temp")
def temp():
    return render_template('temp.html', current_page='temp')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
    