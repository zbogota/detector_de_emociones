# Emotion Detection Application

This project is a web-based Emotion Detection application developed using Python and Flask.

The application analyzes user-provided text and detects the dominant emotion using the Watson NLP Emotion Prediction API.

## Features

- Detects emotions from text input
- Returns scores for:
  - Anger
  - Disgust
  - Fear
  - Joy
  - Sadness
- Identifies the dominant emotion
- Handles invalid or blank input
- Web interface using Flask

## Technologies Used

- Python
- Flask
- Requests
- Watson NLP API

## Project Structure

```text
Final_Project/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── static/
│   └── mywebscript.js
│
├── templates/
│   └── index.html
│
├── server.py
├── test_emotion_detection.py
└── README.md
```

## Running the Application

Install dependencies:

```bash
pip install flask requests
```

Run the server:

```bash
python server.py
```

Open in browser:

```text
http://localhost:5000
```

## Example Output

```json
{
  "anger": 0.006274985,
  "disgust": 0.0025598293,
  "fear": 0.009251528,
  "joy": 0.9680386,
  "sadness": 0.049744144,
  "dominant_emotion": "joy"
}
```