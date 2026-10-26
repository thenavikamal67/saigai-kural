# Sample Dataset

## Purpose

`sample_signs.csv` demonstrates the proposed vocabulary and metadata format for Saigai Kural.

## Fields

- `sample_id`: Unique identifier for a sample record.
- `label`: Machine-readable class label.
- `english`: English text associated with the label.
- `tamil`: Tamil text associated with the label.
- `features_json`: JSON array containing extracted landmark features.
- `status`: Indicates whether the row is a placeholder or has been verified.

## Important

All records in the initial example file are placeholders. They do not contain real landmark measurements and must not be used to train a classifier.

For a training-ready record, replace `features_json` with an array of 63 numeric values representing 21 hand landmarks with x, y, and z coordinates, using the same coordinate processing applied by the inference pipeline.

The exact representation may change if the project uses additional features or temporal sequences.

## Data Collection Guidelines

1. Use a verified ISL vocabulary source and consult fluent ISL users.
2. Record the intended meaning and signing variation.
3. Obtain informed consent before collecting participant recordings.
4. Store only the data needed for the project.
5. Separate participants across training and evaluation sets to reduce data leakage.
6. Document the data source, licence, collection method, and limitations.
7. Remove private or identifying information when it is not needed.

Do not describe placeholder records as a trained dataset or claim model accuracy from them.
