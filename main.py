from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Esto permite solicitudes CORS desde cualquier origen
CORS(app, resources={r"/*": {"origins": "*"}})

def calcular_bernoulli(p1, v1, h1, p2, v2, h2):
    g = 9.81  # Aceleración gravitacional en m/s^2
    rho = 1000  # Densidad del agua en kg/m^3

    term1 = p1 / (rho * g) + v1**2 / (2 * g) + h1
    term2 = p2 / (rho * g) + v2**2 / (2 * g) + h2

    return term1 - term2

from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route('/calcular', methods=['POST'])
def calcular_bernoulli():
    data = request.json
    P = data.get('P')
    p = data.get('p')
    v = data.get('v')
    g = data.get('g')
    h = data.get('h')

    resultado = P + (0.5 * p * math.pow(v, 2)) + (p * g * h)
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/', methods=['GET'])
def index():
    return "La aplicación BernoulliAPI está corriendo correctamente"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
