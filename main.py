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

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    p1 = data['p1']
    v1 = data['v1']
    h1 = data['h1']
    p2 = data['p2']
    v2 = data['v2']
    h2 = data['h2']

    # Cálculo de la energía total en el punto 1
    e1 = p1 + 0.5 * 1000 * v1**2 + 1000 * 9.81 * h1

    # Cálculo de la energía total en el punto 2
    e2 = p2 + 0.5 * 1000 * v2**2 + 1000 * 9.81 * h2

    # Cálculo de la diferencia de energía entre los dos puntos
    resultado = e1 - e2

    return jsonify({"resultado": resultado})

@app.route('/', methods=['GET'])
def index():
    return "La aplicación BernoulliAPI está corriendo correctamente"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
