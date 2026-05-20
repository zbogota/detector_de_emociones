import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """
    Unit tests for emotion detection.
    """

    def test_emotion_detection(self):
        """
        Test multiple sentences for expected dominant emotions.
        """

        test_cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear"
        }

        for sentence, expected_emotion in test_cases.items():

            response = emotion_detector(sentence)

            detected_emotion = response['dominant_emotion']

            self.assertEqual(detected_emotion, expected_emotion)


if __name__ == "__main__":
    unittest.main()