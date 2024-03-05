from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/boletim")
def boletim():
    return render_template("boletim.html")

@app.route("/trocar_senha")
def trocar_senha():
    render_template("trocar_senha")

@app.route("/homepage")
def voltar():
    return render_template("homepage.html")

if __name__ == "__main__":
    app.run(debug=True)