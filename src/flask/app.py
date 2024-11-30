from flask import Flask, request, render_template
import pickle
import numpy as np

with open('rf_classifiers.pkl', 'rb') as rf_file:
    rf_classifiers = pickle.load(rf_file)
with open('nb_classifiers.pkl', 'rb') as nb_file:
    nb_classifiers = pickle.load(nb_file)
with open('lr_classifiers.pkl', 'rb') as lr_file:
    lr_classifiers = pickle.load(lr_file)

models = {
    "Random Forest": rf_classifiers,
    "Naive Bayes": nb_classifiers,
    "Logistic Regression": lr_classifiers
}

app = Flask(__name__)

def predict_star_rating(model_name, texts):
    classifiers = models[model_name]
    probabilities = np.zeros((len(texts), 5))
    for star, classifier in classifiers.items():
        probs = classifier.predict_proba(texts)[:, 1]
        probabilities[:, star - 1] = probs
    return np.argmax(probabilities, axis=1) + 1 


@app.route('/')
def home():
    return render_template('index.html', models=models.keys())

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        model_name = request.form['model']
        predicted_star = predict_star_rating(model_name, [review])[0]
        return render_template(
            'predict.html',
            review=review,
            rating=predicted_star,
            model_name=model_name
        )

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5001)


