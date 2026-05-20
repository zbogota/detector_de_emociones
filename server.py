"""
Emotion Detection Flask Application.

This module creates a Flask web server to analyze emotions in text
using the EmotionDetection package.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector  # pylint: disable=import-error

app = Flask(__name__)  # pylint: disable=invalid-name


@app.route("/")
def render_index_page():
    """
    Render the main index page.
    """
    return render_template('index.html')


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the text provided by the user and return the emotion scores.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return formatted_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)