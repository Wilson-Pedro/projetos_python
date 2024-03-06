from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login_aluno")
def login_aluno():
    return render_template("login_aluno.html")

@app.route("/trocar_senha")
def trocar_senha():
    render_template("trocar_senha")

@app.route("/duvidas")
def duvidas():
    return render_template("duvidas.html")

@app.route("/Admin", methods=['POST'])
def Admin():
    nome = request.form['nome']
    return render_template('Admin.html', nome=nome)

@app.route("/boletim")
def boletim():
    return render_template('boletim.html')

@app.route("/cadastar_alunos")
def cadastrar_alunos():
    return render_template('cadastrar_alunos.html')

if __name__ == "__main__":
    app.run(debug=True)