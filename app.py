from flask import Flask, render_template, request

app = Flask(__name__)

def par_ou_impar(n: int) -> str:
    return "Par" if n % 2 == 0 else "Ímpar"

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        try:
            numero = int(request.form["numero"])
            resultado = par_ou_impar(numero)
        except ValueError:
            resultado = "Erro: informe um número inteiro válido."
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
