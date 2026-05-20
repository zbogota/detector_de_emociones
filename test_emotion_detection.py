from EmotionDetection import emotion_detector

def test_emotion_detection():

    test_sentences = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for sentence, expected_emotion in test_sentences.items():

        response = emotion_detector(sentence)

        detected_emotion = response['dominant_emotion']

        if detected_emotion == expected_emotion:
            print("Passed")
        else:
            print("Failed")

test_emotion_detection()