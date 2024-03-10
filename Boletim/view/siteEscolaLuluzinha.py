from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import requests

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'escola'

mysql = MySQL(app)

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

@app.route("/duvidas_login_diretor")
def duvidas():
    return render_template("duvidas_login_diretor.html")

@app.route("/Admin", methods=['POST'])
def Admin():
    nome = request.form['nome']
    return render_template('Admin.html', nome=nome)

@app.route("/boletim")
def boletim():
    return render_template('boletim.html')

@app.route("/cadastar_alunos", methods=['GET', 'POST'])
def cadastrar_alunos():
    if request.method == 'POST':
        nome = request.form['nome']
        matricula = request.form['matricula']
        telefone = request.form['telefone']
        nascimento = request.form['nascimento']
        endereco = request.form['endereco']

        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO alunos (nome, matricula, telefone, nascimento, endereco) VALUES (%s, %s, %s, %s, %s)",
            (nome, matricula, telefone, nascimento, endereco)
        )
        mysql.connection.commit()
        cursor.close()
        return "Formulário enviado com sucesso!"
    else:
        return render_template('cadastrar_alunos.html')

@app.route("/cadastrar_professores")
def cadastrar_professores():
    return render_template('cadastrar_professores.html')

if __name__ == "__main__":
    app.run(debug=True)