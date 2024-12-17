from flask import Flask, request, jsonify
from inference import run_inference
import prometheus_client

app = Flask(__name__)

REQUEST_COUNT = prometheus_client.Counter('request_count', 'Number of requests')
INFERENCE_LATENCY = prometheus_client.Histogram('inference_latency', 'Inference latency in seconds')

@app.route('/predict', methods=['POST'])
def predict():
    REQUEST_COUNT.inc()
    data = request.get_json()
    with INFERENCE_LATENCY.time():
        result = run_inference(data['input'])
    return jsonify({"result": result})

@app.route('/metrics')
def metrics():
    return prometheus_client.generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
