from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get("textToAnalyze")                # gets text from interface
    response = emotion_detector(text_to_analyze)                       # runs text through emotion_detector and stores in var response    
    
    anger_score = response["anger"]                                    # (1/2) breaks down the dictionary that is stored in response
    disgust_score = response["disgust"]                                # (2/2) and assigns each sentiment score to a variable
    fear_score = response["fear"]
    joy_score = response["joy"]
    sadness_score = response["sadness"]
    dominant_emotion = response["dominant_emotion"]
    if anger_score is None:                                            # if emotion_detector return None returns text
        return "Invalid text! Please try again!."
    else:                                                              # puts response into customer requested format
        return ("For the given statement, the system response is anger: " + str(anger_score) + ", disgust: " + str(disgust_score) + ", fear: " + str(fear_score) + ", joy: " + str(joy_score) + ", sadness: " + str(sadness_score) + ". The dominant emotion is " + str(dominant_emotion)+ ".")

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)

