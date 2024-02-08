import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } } 
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:                                                          # If response is not blank
        anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]        # (1/2) pulls out percentage in deciamal point format and assigns
        disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]    # (2/2) to emotion_score
        fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
        joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
        sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
        response_dic = formatted_response["emotionPredictions"][0]["emotion"]                # pulls emotion dictionary and assigns to variable
        dominant_emotion = max(response_dic, key=response_dic.get)                           # gets highest value in dictionary and assigns key to dominant_emotion
    elif response.status_code == 400:                                                        # If response is blank
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
    return {"anger": anger_score, "disgust": disgust_score, "fear": fear_score, "joy": joy_score, "sadness": sadness_score, "dominant_emotion": dominant_emotion}
