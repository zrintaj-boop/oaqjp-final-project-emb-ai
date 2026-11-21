"""Flask web application for IBM AI-based emotion detection."""

from flask import Flask, render_template, request
from requests.exceptions import RequestException
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Show the emotion detection interface."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """Analyze text passed as the textToAnalyze query parameter."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    if not text_to_analyze.strip():
        return "Invalid text! Please try again!", 400

    try:
        result = emotion_detector(text_to_analyze)
    except (RequestException, ValueError, KeyError, IndexError, TypeError):
        app.logger.exception("Emotion analysis failed")
        return "Emotion analysis service is unavailable. Please try again later!", 503

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 400

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
