"""Prediction helper for a trained landmark classifier."""

import joblib


FEATURE_COUNT = 63


def predict_sign(model_path, features, threshold=0.70):
    """Return a label and confidence, or None if uncertain.

    The threshold is an example starting value. It must be
    calibrated using validation data before real-world use.
    """
    if len(features) != FEATURE_COUNT:
        raise ValueError(
            f"Expected {FEATURE_COUNT} landmark features"
        )

    model = joblib.load(model_path)
    probabilities = model.predict_proba([features])[0]

    best_index = probabilities.argmax()
    confidence = float(probabilities[best_index])
    label = str(model.classes_[best_index])

    if confidence < threshold:
        return {
            "label": None,
            "confidence": confidence,
            "message": "Sign not recognized confidently",
        }

    return {
        "label": label,
        "confidence": confidence,
        "message": "Prediction available",
    }
