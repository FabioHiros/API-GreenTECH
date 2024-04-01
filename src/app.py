from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def home():
    return render_template('index.html', current_page='home')

@app.route("/agua")
def agua():
    return render_template('agua.html', current_page='agua')