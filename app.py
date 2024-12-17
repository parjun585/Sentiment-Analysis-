import streamlit as st
import torch
from transformers import RobertaForSequenceClassification, RobertaTokenizer

# Load a pre-trained sentiment analysis model for 3 classes (RoBERTa model)
model_name = "cardiffnlp/twitter-roberta-base-sentiment"  # A pre-trained model for 3 classes
model = RobertaForSequenceClassification.from_pretrained(model_name, num_labels=3)

# Use the correct tokenizer for the RoBERTa model
tokenizer = RobertaTokenizer.from_pretrained(model_name)

# Function to classify sentiment
def predict_sentiment(text):
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)

    # Make prediction
    with torch.no_grad():
        outputs = model(**inputs).logits
        probabilities = torch.nn.functional.softmax(outputs, dim=1)
        predicted_class = torch.argmax(probabilities, dim=1).item()

    # Map the predicted class to sentiment label
    sentiment_mapping = {0: "Negative", 1: "Neutral", 2: "Positive"}
    sentiment = sentiment_mapping[predicted_class]
    confidence = probabilities[0][predicted_class] * 100

    return sentiment, confidence

# Streamlit Interface
st.title("Sentiment Analysis")
st.write("Enter a text and I will predict whether it's Positive, Negative, or Neutral.")

# User input
user_input = st.text_area("Enter text here:")

if user_input:
    sentiment, confidence = predict_sentiment(user_input)
    st.write(f"Sentiment: {sentiment} ({confidence:.2f}%)")
