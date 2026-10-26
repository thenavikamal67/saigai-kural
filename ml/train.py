"""Train a baseline classifier from verified landmark records."""

import argparse
import csv
import json
from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestClassifier


FEATURE_COUNT = 63


def load_training_data(csv_path):
    features = []
    labels = []

    with Path(csv_path).open(
        "r", encoding="utf-8-sig", newline=""
    ) as file:
        reader = csv.DictReader(file)

        required = {
            "label", "features_json", "status"
        }
        if not reader.fieldnames or not required.issubset(
            reader.fieldnames
        ):
            raise ValueError("CSV is missing required columns")

        for row in reader:
            if row["status"].strip().lower() != "verified":
                continue

            label = row["label"].strip()
            if not label:
                raise ValueError("Verified rows need a label")

            try:
                vector = json.loads(row["features_json"])
            except (TypeError, json.JSONDecodeError) as exc:
                raise ValueError(
                    f"Invalid JSON features for {label}"
                ) from exc

            if not isinstance(vector, list):
                raise ValueError("Features must be a JSON list")

            if len(vector) != FEATURE_COUNT:
                raise ValueError(
                    f"Expected {FEATURE_COUNT} features"
                )

            if any(
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                for value in vector
            ):
                raise ValueError("Features must be numeric")

            features.append([float(value) for value in vector])
            labels.append(label)

    if len(set(labels)) < 2:
        raise ValueError(
            "Training requires at least two verified classes"
        )

    return features, labels


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    features, labels = load_training_data(args.data)

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight="balanced",
    )
    model.fit(features, labels)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output_path)

    print(f"Saved baseline model to {output_path}")
    print(f"Training records: {len(labels)}")
    print(f"Classes: {sorted(set(labels))}")


if __name__ == "__main__":
    main()
