from flask import Flask, render_template, request

app = Flask("__name__")

@app.route("/")
def home():
    return render_template('index.html', current_page='home')

@app.route("/chart")
def chart():
    return render_template('grafico.html', current_page='chart')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
    