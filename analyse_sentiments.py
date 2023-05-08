import speech_recognition as sr
import librosa
import librosa.display
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Load the audio file
audio_file = r'static\audios\Recording.m4a'

def analyze_sentiment():                  # to analyze the sentiment emotions of audio
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)

    # Convert speech to text
    text = r.recognize_google(audio)

    # Perform sentiment analysis using NLTK's SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)

    # Load the ML model for emotion detection
    model_file = 'path/to/model.h5'
    model = load_model(model_file)

    # Extract audio features
    y, sr = librosa.load(audio_file)
    mfccs = librosa.feature.mfcc(y, sr=sr, n_mfcc=40)
    mfccs_scaled = np.mean(mfccs.T,axis=0)

    # Predict the emotion using the ML model
    emotion_dict = {0: 'neutral', 1: 'calm', 2: 'happy', 3: 'sad', 4: 'angry', 5: 'fearful', 6: 'disgust', 7: 'surprised'}
    emotion_pred = model.predict_classes(np.array([mfccs_scaled]))
    emotion = emotion_dict[emotion_pred[0]]

    # Print the sentiment and emotion
    print('Sentiment:', sentiment_scores)
    print('Emotion:', emotion)

if __name__=='__main__':
    analyze_sentiment() 
