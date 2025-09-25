# streamlit_app.py
import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.svm import LinearSVC
import pandas as pd
import re
import pickle


with open("clf.pkl", "rb") as f:
    clf = pickle.load(f)

with open("embedder.pkl", "rb") as f:
    embedder = pickle.load(f)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text


def predict_sentiment(tweets):
    tweets_clean = [clean_text(t) for t in tweets]
    X = embedder.encode(tweets_clean, convert_to_tensor=False)
    preds = clf.predict(X)
    reverse_label_map = {0:'Bearish', 1:'Bullish', 2:'Neutral'}
    return [reverse_label_map[p] for p in preds]

st.title("Financial News Tweet Sentiment Classifier")
st.write("Enter one or more tweets (one per line) to predict their sentiment:")

user_input = st.text_area("Enter tweets here:")

if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter at least one tweet.")
    else:
        tweets = user_input.strip().split("\n")
        predictions = predict_sentiment(tweets)
        results = pd.DataFrame({"Tweet": tweets, "Predicted Sentiment": predictions})
        st.write(results)

#%%
