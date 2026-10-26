# Machine Learning Module

This module contains the initial Python tools for preparing and training the Saigai Kural sign classifier.

## Current Scope

- Read landmark features from a CSV file.
- Validate training records.
- Train a baseline Random Forest classifier.
- Save the trained model.
- Predict a label from a feature vector.

## Requirements for Training

The CSV must contain verified examples with:

- A valid label.
- A JSON feature array containing exactly 63 numeric values.
- `status` set to `verified`.

The model is only as reliable as the data used to train and evaluate it. The repository's placeholder examples cannot be used for training.

## Train

From the repository root:

```bash
python -m ml.train --data data/training_signs.csv --output models/sign_classifier.joblib
```

Create `data/training_signs.csv` only after collecting or obtaining suitable training data.

## Prediction

Use the prediction function from your Python code after loading the trained model. See `predict.py`.

## Limitations

The baseline classifier processes a single landmark vector. It does not yet model sign movement, facial expression, or complete ISL grammar. It is a starting point for experimentation, not a production interpreter.
