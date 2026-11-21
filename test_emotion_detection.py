"""Offline unit tests: mock Watson responses; do not require the live API."""

import unittest
from unittest.mock import Mock, patch
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Verify parsing, dominant emotion selection, and HTTP 400 handling."""

    def check_dominant(self, text, dominant):
        scores = {
            "anger": 0.05,
            "disgust": 0.05,
            "fear": 0.05,
            "joy": 0.05,
            "sadness": 0.05,
        }
        scores[dominant] = 0.80
        fake_response = Mock(status_code=200)
        fake_response.json.return_value = {
            "emotionPredictions": [{"emotion": scores}]
        }
        with patch("EmotionDetection.emotion_detection.requests.post",
                   return_value=fake_response) as mocked_post:
            result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], dominant)
        self.assertEqual(result[dominant], 0.80)
        self.assertEqual(len(result), 6)
        mocked_post.assert_called_once()

    def test_joy(self):
        self.check_dominant("I am glad this happened", "joy")

    def test_anger(self):
        self.check_dominant("I am really mad about this", "anger")

    def test_disgust(self):
        self.check_dominant("I feel disgusted just hearing about this", "disgust")

    def test_sadness(self):
        self.check_dominant("I am so sad about this", "sadness")

    def test_fear(self):
        self.check_dominant("I am really afraid that this will happen", "fear")

    def test_invalid_input_response(self):
        fake_response = Mock(status_code=400)
        with patch("EmotionDetection.emotion_detection.requests.post",
                   return_value=fake_response):
            result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])
        self.assertTrue(all(value is None for value in result.values()))


if __name__ == "__main__":
    unittest.main()
