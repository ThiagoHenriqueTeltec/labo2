from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Lista com 5 nomes
nomes = ["Enzo", "Felipe Breno", "Luã", "Mickael", "Thiago Henrique"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spin')
def spin():
    selecionado = random.choice(nomes)
    return jsonify({'name': selecionado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)