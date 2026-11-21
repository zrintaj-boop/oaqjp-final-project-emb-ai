"""Watson NLP emotion-detection client for the IBM final project."""

import requests

API_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze):
    """Return five emotion scores and the strongest emotion for text.

    A 400 response returns None for all values, as expected in the lab.
    Other network and HTTP errors are raised so they can be handled by Flask.
    """
    if not isinstance(text_to_analyze, str):
        raise TypeError("text_to_analyze must be a string")

    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(
        API_URL, json=payload, headers=HEADERS, timeout=30
    )

    if response.status_code == 400:
        return {**{emotion: None for emotion in EMOTIONS},
                "dominant_emotion": None}

    response.raise_for_status()
    scores = response.json()["emotionPredictions"][0]["emotion"]
    formatted = {emotion: float(scores[emotion]) for emotion in EMOTIONS}
    formatted["dominant_emotion"] = max(
        EMOTIONS, key=lambda emotion: formatted[emotion]
    )
    return formatted
