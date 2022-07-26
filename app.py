from flask import Flask, render_template

app = Flask("Hello")

@app.route("/")
@app.route("/hello")
def hello():
    return "Fala guerreiro"

@app.route("/meucontato")
def meuContato():
    return render_template('index.html')
