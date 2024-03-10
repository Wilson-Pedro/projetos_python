from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import requests

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin1'
app.config['MYSQL_DB'] = 'escola'

mysql = MySQL(app)

# HOMEPAGE
@app.route("/")
def homepage():
    return render_template("homepage.html")

# LOGIN
@app.route("/login")
def login():
    return render_template("login.html")

# LOGIN ALUNO
@app.route("/login_aluno")
def login_aluno():
    return render_template("login_aluno.html")

# TROCAR SENHA
@app.route("/trocar_senha")
def trocar_senha():
    render_template("trocar_senha")

# DÚVIDAS LOGIN DIRETOT
@app.route("/duvidas_login_diretor")
def duvidas():
    return render_template("duvidas_login_diretor.html")

# ADMIN
@app.route("/admin", methods=['POST'])
def admin():
    nome = request.form['nome']
    return render_template('admin.html', nome=nome)

# BOLETIM
@app.route("/boletim")
def boletim():
    return render_template('boletim.html')


# CADASTRO SUCESSO
@app.route("/cadastro_sucesso")
def cadastro_sucesso():
    return render_template('cadastro_sucesso.html')


# CADASTRAR ALUNOS
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
            "INSERT INTO tb_aluno (nome, matricula, telefone, data_nascimento, endereco) VALUES (%s, %s, %s, %s, %s)",
            (nome, matricula, telefone, nascimento, endereco)
        )
        mysql.connection.commit()
        cursor.close()
        return render_template('cadastro_sucesso.html')
    else:
        return render_template('cadastrar_alunos.html')



# CADASTRAR PROFESSORES
@app.route("/cadastrar_professores", methods=['GET', 'POST'])
def cadastrar_professores():
    if request.method == 'POST':
        nome = request.form['nome']
        disciplina = request.form['disciplina']
        email = request.form['email']
        senha = request.form['senha']
        endereco = request.form['endereco']

        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO tb_professor (nome, disciplina, email, senha, endereco) VALUES (%s, %s, %s, %s, %s)",
            (nome, disciplina, email, senha, endereco)
        )

        mysql.connection.commit()
        cursor.close()

        return render_template('cadastro_sucesso.html')
    
    else:
        return render_template('cadastrar_professores.html')



if __name__ == "__main__":
    app.run(debug=True)