# TripAdvisor Review Star Rating Predictor

A machine learning pipeline that classifies TripAdvisor hotel reviews into 1–5 star ratings using a One vs Rest (OvR) multiclass classification approach, deployed as both a Flask web app and a Gradio interface with OCR support.

## Features

- **OvR Multiclass Classification** — Breaks 5-star prediction into five binary classification tasks
- **Multiple Model Support** — Choose between Logistic Regression, Random Forest, or Multinomial Naive Bayes
- **Flask Web App** — Submit reviews as text and receive predicted star ratings
- **Gradio Interface** — Upload screenshots of reviews using Tesseract OCR for image-to-text prediction
- **201,295 real TripAdvisor reviews** sourced from HuggingFace for training and evaluation

## Tech Stack

- **ML:** Python, scikit-learn, TF-IDF, Pickle
- **Web:** Flask, HTML, CSS
- **OCR:** Pytesseract, Gradio
- **Environment:** Jupyter Notebooks, VSCode

## Model Performance

| Model               | Accuracy |
|----------------------|----------|
| Logistic Regression  | 0.65     |
| Multinomial Naive Bayes | 0.60  |
| Random Forest        | 0.55     |
