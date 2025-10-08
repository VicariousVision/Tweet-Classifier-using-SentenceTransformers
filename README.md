# Tweet classifier 
This is a repo for an assignment in DSC4828 - Applied data science at UNISA. The objective of this is to build a simple classifier that takes in data and classifies it in n classes. I have selected textual data and that being tweets related to the finance community. The data and model sources are referenced in the 'Classifier' notebook.

### How to run
- Clone this repo and install the requirements
- Start the streamlit service
- Input text and the model will classify its sentiment

Some areas explored in this project were Topic modeling using BERTopic, sentiment analysis and comparing the use of TF-IDF vectorisation against BERT encodings as a way to classify text. 

### Results
LinearSCV performed best, the base model using a blanaced weighting parameter performed just as good as the model that was optimized with cross fold validation. Encoding the text with a pretrained BERT encoder performed worse.

Any comments, feedback and improvements are welcome. 
