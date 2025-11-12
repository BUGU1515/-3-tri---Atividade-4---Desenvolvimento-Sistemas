from flask import Flask, redirect, template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, Flask !!</h1>"

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/versao')
def versao():
    versao = "1.1.0"
    return f"<h1>App v{versao}</h1>"


@app.get("/saudar/<usuario>") 
def bemvindo(usuario):
   return f"<h1>Bem-vindo, {usuario.capitalize()}!<h1>"


@app.route('/quadrado/<int:n>')
def quadrado(n):
    return f"{n}² = {n ** 2}"


@app.route('/home')
def home():
    return redirect('/')
