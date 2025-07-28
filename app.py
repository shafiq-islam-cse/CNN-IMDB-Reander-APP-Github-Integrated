import tensorflow as tf
from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# Load model
model = tf.keras.models.load_model("cnn_imdb_model.h5")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    # Dummy vectorization
    x = np.ones((1, 500))  # replace with real vectorization

    prediction = model.predict(x)[0][0]
    sentiment = "Positive" if prediction > 0.5 else "Negative"

    return jsonify({
        "prediction": float(prediction),
        "sentiment": sentiment
    })
