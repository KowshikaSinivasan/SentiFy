from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os

# Load environment variables


app = Flask(__name__)
CORS(app)

# Set Flask debug mode
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False')

# Constants
MODEL_PATH = 'model.pkl'
REQUIRED_FEATURES = 500

# Load the trained model
try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    print(f"[INFO] Loaded model from {MODEL_PATH}")
except Exception as e:
    print(f"[FATAL] Failed to load model: {e}")
    exit(1)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({'error': 'No input text provided'}), 400

    try:
        print(f"[DEBUG] Received text: {text}")

        # Generate a random vector of shape (1, 500)
        random_vector = np.random.rand(1, REQUIRED_FEATURES)
        print(f"[DEBUG] Random input vector shape: {random_vector.shape}")

        prediction = model.predict(random_vector)[0]
        return jsonify({'prediction': int(prediction)})

    except Exception as e:
        print(f"[ERROR] Exception: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
