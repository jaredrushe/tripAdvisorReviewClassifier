from flask import Flask, request, render_template
import pickle
import numpy as np

with open('csc1052-nb1000-model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('csc1052-nb1000-features.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']  
        review_vectorized = vectorizer.transform([review]).toarray()
        
        prediction = model.predict(review_vectorized)
        sentiment = "Positive" if prediction[0] == 1 else "Negative"
        
        return render_template('predict.html', review=review, sentiment=sentiment)

app.run(debug=True, host='127.0.0.1', port=5001)
