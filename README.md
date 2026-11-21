# Final Project: AI-Based Emotion Detection Web Application

This is an educational implementation of the **IBM AI Developer** final project using
Watson NLP, Python, a Python package, unit tests, Flask, error handling, and Pylint.

## Project layout

- `emotion_detection.py`: initial standalone version for Tasks 2–3 (same implementation as the package module)
- `EmotionDetection/emotion_detection.py`: packaged detector for Task 4
- `EmotionDetection/__init__.py`: exports `emotion_detector`
- `test_emotion_detection.py`: offline unit tests using mocked Watson responses
- `server.py`: Flask server with `/` and `/emotionDetector?textToAnalyze=...`
- `templates/index.html`: web interface
- `static/mywebscript.js`: browser request handler
- `static/mystyle.css`: web styling

## Setup

```bash
python3 -m pip install -r requirements.txt
```

## Run tests (offline)

```bash
python3 -m unittest -v test_emotion_detection.py
```

The unit tests use **mocked Watson API responses**, so they verify the code's parsing
and formatting logic, **not** that the live model correctly recognizes emotions.

## Run the application

```bash
python3 server.py
```

Open `http://localhost:5000` in the same environment, or use the Cloud IDE's
preview / forwarded port if available. Try: `I think I am having fun`.

## Interactive Watson test (requires network access)

```bash
python3
>>> from EmotionDetection import emotion_detector
>>> emotion_detector("I love this new technology.")
```

The Watson API endpoint is an IBM Skills Network training endpoint. It may be
unavailable outside the course lab or may change. Live results and screenshots
**must be obtained by actually running the application**.

## Static code analysis

```bash
python3 -m pylint server.py EmotionDetection/emotion_detection.py
```

## Submission notes

The assessment asks for **real** code excerpts, terminal output, screenshots,
and a **public GitHub repository URL**. A ZIP uploaded as a single file to GitHub
will not expose the individual project files to the grader. **Unzip first**, then
upload the actual files and folders. Do not claim a test or deployment succeeded
until it has been run in the appropriate environment.

## API behavior

The `/emotionDetector` route returns `Invalid text! Please try again!` with
HTTP 400 for blank input or an invalid-text response from the model.
Other network/service failures return HTTP 503.
