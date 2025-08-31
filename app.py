from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def par_ou_impar(n: int) -> str:
    return "Par" if n % 2 == 0 else "Ímpar"

def curiosidade_numero(n: int) -> str:
    """Busca curiosidade sobre o número na API NumbersAPI"""
    try:
        url = f"http://numbersapi.com/{n}/math?json"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get("text", "Não foi encontrada curiosidade para este número.")
        return "Erro ao consultar API externa."
    except Exception:
        return "Não foi possível obter a curiosidade do número."

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    curiosidade = None
    if request.method == "POST":
        try:
            numero = int(request.form["numero"])
            resultado = par_ou_impar(numero)
            curiosidade = curiosidade_numero(numero)
        except ValueError:
            resultado = "Erro: informe um número inteiro válido."
    return render_template("index.html", resultado=resultado, curiosidade=curiosidade)

if __name__ == "__main__":
    app.run(debug=False)
