import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE

# Load pre-trained model, vectorizer, and label encoder
model = joblib.load('random_forest_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')
encoder = joblib.load('label_encoder.pkl')

# Function to create k-mers from DNA sequence
def getKmers(sequence, size=5):
    return [sequence[x:x+size].upper() for x in range(len(sequence) - size + 1)]

# Function to predict the class of a given DNA sequence
def predict_dna_sequence(sequence):
    kmer_sequence = getKmers(sequence)
    joined_kmer = ' '.join(kmer_sequence)
    
    # Transform the sequence into features using the vectorizer
    features = vectorizer.transform([joined_kmer])
    
    # Predict the class
    prediction = model.predict(features)
    
    # Decode the prediction into the original class label
    predicted_class = encoder.inverse_transform(prediction)
    return predicted_class[0]

# Streamlit UI
st.title("DNA Sequence Prediction")
st.write("Enter a DNA sequence to predict its class (DMT1, DMT2, NONDM).")

# Input: User enters the DNA sequence
sequence_input = st.text_area("Enter DNA Sequence:", "")

# Button to make prediction
if st.button("Predict"):
    if len(sequence_input) < 5:  # Ensure the sequence length is sufficient for k-mer creation
        st.warning("Please enter a DNA sequence with at least 5 characters.")
    else:
        predicted_class = predict_dna_sequence(sequence_input)
        st.success(f"The predicted class for the entered DNA sequence is: **{predicted_class}**")
