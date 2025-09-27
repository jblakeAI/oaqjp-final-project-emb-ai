import requests 
import json


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=headers)
    
    # Response output is formatted to python dictionary 
    formatted_response = json.loads(response.text)
    
    # Extracting emotions from formatted_response
    emotions = formatted_response['emotionPredictions'][0]['emotion']
   
    # Finding dominant emotion
    dominant_emotion = max(emotions, key = emotions.get)
    
    # Updating emotions dictionary to include dominant resposne
    emotions['dominant_emotion'] = dominant_emotion

    return emotions
