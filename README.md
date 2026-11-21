
"""Detect emotions using IBM Watson NLP."""

import requests

WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

WATSON_HEADERS = {
    "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
}

EMOTION_KEYS = ("anger", "disgust", "fear", "joy", "sadness")


def _empty_result():
    return {
        **{key: None for key in EMOTION_KEYS},
        "dominant_emotion": None
    }


def emotion_detector(text_to_analyze):
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return _empty_result()

    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(
            WATSON_URL,
            json=payload,
            headers=WATSON_HEADERS,
            timeout=20,
        )

        if response.status_code == 400:
            return _empty_result()

        response.raise_for_status()
        result = response.json()

        scores = result["emotionPredictions"][0]["emotion"]
        formatted = {
            key: float(scores[key]) for key in EMOTION_KEYS
        }

        formatted["dominant_emotion"] = max(
            EMOTION_KEYS,
            key=lambda key: formatted[key]
        )

        return formatted

    except (
        requests.RequestException,
        ValueError,
        KeyError,
        IndexError,
        TypeError,
    ):
        return _empty_result()
