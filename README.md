# Saigai Kural (சைகை குரல்)
### Voice of Signs | An Open-Source Sign Language Accessibility Project

Saigai Kural is an open-source mobile application designed to improve communication between Indian Sign Language (ISL) users and people who do not know sign language.

The application aims to recognize signs through a smartphone camera and display their meanings in Tamil and English. It also aims to help users learn signs for common words.

**Project status:** Prototype / Under Development

## Table of Contents

- About the Project
- Problem Statement
- Objectives
- Features
- Technology Stack
- System Architecture
- Project Structure
- Installation and Setup
- Running the Project
- Sample Data
- Testing
- Limitations
- Roadmap
- Contributing
- License

## About the Project

Communication can be difficult when two people use different communication methods. Saigai Kural aims to make everyday communication more accessible through mobile technology.

The application focuses on Indian Sign Language and regional-language support, beginning with Tamil and English.

The initial prototype is planned to support a small vocabulary of common signs. The project can later be extended with more signs, larger datasets, improved recognition models, and additional Indian languages.

## Problem Statement

Many sign language users face communication barriers in education, healthcare, public services, and everyday activities. People who do not know sign language may find it difficult to understand signed communication.

Existing dictionaries and prerecorded demonstrations can help people learn signs, but they may not provide real-time recognition of a user's gestures.

Saigai Kural aims to explore an accessible, low-cost mobile solution for sign recognition and sign-language learning.

## Objectives

1. Recognize selected ISL signs using a smartphone camera.
2. Display recognized words in Tamil and English.
3. Provide speech output for supported text.
4. Help users learn signs through a dedicated learning section.
5. Develop an interface with readable text, clear feedback, and accessible controls.
6. Explore offline operation and privacy-friendly on-device processing.
7. Make the source code available for learning, testing, and community contributions.

## Features

### Recognize

- Capture hand gestures using the mobile camera.
- Extract hand landmarks using MediaPipe.
- Pass extracted features to a trained classifier.
- Display the predicted word in Tamil and English.
- Provide speech output when supported by the device.
- Show a fallback message when a sign cannot be recognized confidently.

### Learn

- Browse supported words.
- View sign demonstrations or instructional images.
- Display Tamil and English meanings.
- Practice signs using learning materials.

### Accessibility

- High-contrast interface options.
- Large, readable text.
- Clear recognition status messages.
- Text and audio feedback where supported.

## Technology Stack

| Component | Proposed technology |
|---|---|
| Mobile application | Flutter and Dart |
| Hand tracking | MediaPipe |
| Model development | Python |
| Machine learning | scikit-learn initially; TensorFlow Lite or another compatible runtime for mobile deployment |
| Data storage | CSV for initial data; SQLite for local application data |
| Speech output | Android/iOS text-to-speech capabilities |
| Version control | Git and GitHub |
| Testing | pytest and Flutter testing tools |

The final stack may change as the prototype develops.

## System Architecture

1. The user opens the Recognize screen.
2. The camera captures a hand gesture.
3. A hand-landmark detector extracts hand keypoints.
4. The feature-processing module prepares the landmarks.
5. A trained classifier predicts a supported sign.
6. The application checks the prediction confidence.
7. The application displays the corresponding Tamil and English text.
8. The speech module reads the supported text aloud when requested.

The Learn screen uses a vocabulary catalogue containing words, translations, and verified learning resources.

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the detailed design.

## Project Structure

```text
saigai-kural/
├── app/
│   └── README.md
├── ml/
│   ├── README.md
│   ├── predict.py
│   └── train.py
├── data/
│   ├── sample_signs.csv
│   └── README.md
├── docs/
│   ├── ARCHITECTURE.md
│   └── MODEL_CARD.md
├── tests/
│   └── test_sample_data.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── .gitignore
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── requirements.txt
└── README.md
```

## Installation and Setup

### Prerequisites

Install the following tools:

- Git
- Python 3.12 or another Python version supported by the selected dependencies
- Flutter SDK if you are developing the mobile application
- Android Studio or a compatible Android development setup for Android testing
- A code editor such as Visual Studio Code

Check your installations:

```bash
git --version
python --version
flutter --version
```

The Flutter command is required only for the mobile application.

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/saigai-kural.git
cd saigai-kural
```

Replace `YOUR-USERNAME` with your GitHub username.

### Step 2: Install Python dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Step 3: Run the sample-data tests

```bash
python -m pytest
```

These tests validate the example dataset and its expected structure. They do not prove that real-world ISL recognition works.

### Step 4: Set up the mobile app

The `app/` directory will contain the Flutter project.

Once the Flutter project files have been created:

```bash
cd app
flutter pub get
flutter run
```

A complete mobile build requires the Flutter source code, application configuration, camera integration, and a compatible recognition model. These steps alone do not create those components.

## Sample Data

The repository includes a small illustrative CSV file to demonstrate the dataset format.

Each record contains a sample identifier, a label, translations, and a feature vector.

The example records are placeholders for demonstrating data handling. They are not verified ISL examples and must not be used to claim recognition accuracy.

See [data/README.md](data/README.md).

## Testing

Run the Python tests:

```bash
python -m pytest -v
```

Planned testing includes:

- CSV format validation
- Label and translation validation
- Feature extraction tests
- Model prediction tests
- Low-confidence prediction handling
- Mobile UI tests
- Camera permission tests
- Tamil and English text rendering
- Speech output tests
- Testing under different lighting conditions

## Limitations

- The initial vocabulary is limited.
- The example dataset is not a trained ISL dataset.
- Recognition quality depends on the dataset, model, camera conditions, and signing variation.
- Real ISL communication includes movement, facial expressions, body posture, and context. A hand-landmark classifier alone cannot fully represent the language.
- Tamil speech output depends on device and voice support.
- The project must be evaluated with fluent ISL users before it is used for important communication.

Saigai Kural is a communication-assistance prototype, not a certified interpreter or a replacement for qualified sign language interpreters.

## Roadmap

- [ ] Create the initial mobile application.
- [ ] Implement the login and home screens.
- [ ] Build the Recognize and Learn screens.
- [ ] Add a verified initial vocabulary.
- [ ] Collect consented and appropriately licensed training samples.
- [ ] Implement landmark extraction.
- [ ] Train and evaluate an initial classifier.
- [ ] Integrate a compatible mobile inference model.
- [ ] Add Tamil and English text output.
- [ ] Integrate speech output.
- [ ] Add unit and integration tests.
- [ ] Evaluate recognition with diverse users.
- [ ] Improve offline support and accessibility.
- [ ] Expand the vocabulary and supported languages.

## Contributing

Contributions are welcome. You can help with Flutter development, machine learning, dataset quality, Tamil translations, accessibility testing, documentation, and bug reports.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes.

Do not upload private recordings, personal information, or sign-language datasets unless you have the necessary permissions and consent.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Third-party models, datasets, libraries, and learning resources may have separate licenses and conditions.

## Acknowledgements

- MediaPipe for hand landmark detection tools.
- Flutter for cross-platform mobile development.
- The Indian Sign Language community and accessibility advocates whose knowledge and feedback are essential to this project.

## Contact

For questions, suggestions, and contributions, open an issue in this repository.

**Saigai Kural — making communication more accessible through technology.**
