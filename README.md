This repo is a testing ground for an assignment in DSC4828. The Assignment6 notebook is the tutorial from Machine Learning Mastery https://machinelearningmastery.com/machine-learning-in-python-step-by-step/.

The notebook titled "Classifier" is the same classification idea but this time using text and a combination of LinearSVC and SentenceTransformers. The model was trained on a selection of tweets from https://huggingface.co/datasets/zeroshot/twitter-financial-news-sentiment.

# How to run
1. Install requirements.txt
2. Start the streamlit serivce by running streamlit run streamlit_app.py in your terminal
3. The streamlit serivce will run locally in your browser. Enter text and the model will load and classify your text into Neutral, Bearish or Bullish
