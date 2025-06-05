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
st.title("Prediksi Sekuens DNA")
st.write("Masukkan sekuens DNA yang ingin diprediksi ke dalam input dibawah ini. Model akan memprediksi sekuens DNA yang telah diinput. Prediksi akan menghasilkan diabetes tipe 1, tipe 2 atau Non Diabetes.")

# Input: User enters the DNA sequence
sequence_input = st.text_area("Masukkan Sekuens DNA:", "")

# Button to make prediction
if st.button("Predict"):
    if len(sequence_input) < 5:  # Ensure the sequence length is sufficient for k-mer creation
        st.warning("Paling sedikit 5 karakter.")
    else:
        predicted_class = predict_dna_sequence(sequence_input)
        st.success(f"Kelas yang diprediksi untuk sekuens DNA yang dimasukkan adalah: **{predicted_class}**")
