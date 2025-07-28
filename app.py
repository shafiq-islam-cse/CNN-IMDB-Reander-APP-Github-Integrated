from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import pickle

app = Flask(__name__)

# Load model and vectorizer
model = tf.keras.models.load_model("cnn_imdb_model.h5")

# Dummy tokenizer/vectorizer for now (replace with your real one if saved)
def dummy_vectorize(text):
    return np.ones((1, 500))  # Placeholder for actual vectorized input

@app.route("/")
def home():
    return "IMDB CNN Sentiment Classifier is live!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    x = dummy_vectorize(text)
    prediction = model.predict(x)[0][0]
    sentiment = "Positive" if prediction > 0.5 else "Negative"
    return jsonify({"prediction": float(prediction), "sentiment": sentiment})