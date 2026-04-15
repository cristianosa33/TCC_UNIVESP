from flask import Flask, render_template, jsonify, request
import os

# Configura o Flask para encontrar o HTML na pasta correta
app = Flask(__name__, 
            template_folder='../frontend', 
            static_folder='../static')

# Rota para abrir a página do Mapa
@app.route('/')
def index():
    return render_template('index.html')

# API que enviará os pontos para o mapa (futuramente virá do Banco de Dados)
@app.route('/api/ocorrencias', methods=['GET'])
def listar_ocorrencias():
    # Exemplo de dados simulados (Mock)
    ocorrencias = [
        {
            "id": 1,
            "tipo": "Descarte de Resíduos",
            "lat": -23.5505,
            "lng": -46.6333,
            "criticidade": "Alta",
            "descricao": "Acúmulo de entulho na calçada."
        },
        {
            "id": 2,
            "tipo": "Arborização",
            "lat": -23.5590,
            "lng": -46.6580,
            "criticidade": "Média",
            "descricao": "Árvore com risco de queda após chuva."
        }
    ]
    return jsonify(ocorrencias)

if __name__ == '__main__':
    app.run(debug=True)
