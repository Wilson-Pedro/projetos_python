from Boletim.view import app

@app.route('/')
@app.route('/index')
def index():
    return "hello world!"