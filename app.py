from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def home():
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
def index():
    return redirect('/')


@app.route("/pagina")
def pagina():
    return render_template("pagina.html")


itens = ["maçã", "banana", "laranja", "uva"]
@app.route("/buscar/<item>")
def buscar(item):
    for i in itens:
        if i == item:
            return f"Item '{item}' encontrado!"
    return f"Item '{item}' não encontrado."

