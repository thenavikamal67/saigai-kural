import csv
import json
from pathlib import Path


DATA_FILE = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "sample_signs.csv"
)

REQUIRED_COLUMNS = {
    "sample_id",
    "label",
    "english",
    "tamil",
    "features_json",
    "status",
}


def load_rows():
    with DATA_FILE.open(
        encoding="utf-8-sig", newline=""
    ) as file:
        reader = csv.DictReader(file)
        assert reader.fieldnames is not None
        assert REQUIRED_COLUMNS.issubset(reader.fieldnames)
        return list(reader)


def test_sample_dataset_has_records():
    assert load_rows()


def test_sample_ids_are_unique():
    rows = load_rows()
    ids = [row["sample_id"] for row in rows]
    assert len(ids) == len(set(ids))


def test_labels_and_translations_are_present():
    for row in load_rows():
        assert row["label"].strip()
        assert row["english"].strip()
        assert row["tamil"].strip()


def test_feature_data_is_valid_json():
    for row in load_rows():
        features = json.loads(row["features_json"])
        assert isinstance(features, list)


def test_examples_are_marked_as_placeholders():
    for row in load_rows():
        assert row["status"] == "placeholder"
        assert json.loads(row["features_json"]) == []
