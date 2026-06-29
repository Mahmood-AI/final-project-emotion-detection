"""
Executing this function initiates the application of emotion
detector to be deployed over the web server.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    This code receives the text from the HTML interface and
    runs emotion detection over it using emotion_detector()
    function. The output returned shows the scores and dominant_emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    # Check if the response dominant emotion is None (for blank inputs)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
        
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    output_message = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    
    return output_message

@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application
    page over the Flask development server.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
