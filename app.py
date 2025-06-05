import streamlit as st
import joblib
from sklearn.feature_extraction.text import CountVectorizer

# Fungsi preprocessing
def getKmers(sequence, size=6):
    return [sequence[x:x+size] for x in range(len(sequence) - size + 1)]

# Load model dan vectorizer
model = joblib.load("random_forest_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")  # Harus Anda simpan juga

# Judul aplikasi
st.title("Prediksi Diabetes Berdasarkan Sekuens DNA")

# Input dari user
sequence_input = st.text_area("Masukkan Sekuens DNA Anda (A,T,G,C):", "")

if st.button("Prediksi"):
    if len(sequence_input) < 6:
        st.warning("Sekuens harus minimal 6 huruf untuk pembentukan k-mer.")
    else:
        kmer_sequence = getKmers(sequence_input)
        joined_kmer = ' '.join(kmer_sequence)
        features = vectorizer.transform([joined_kmer])
        prediction = model.predict(features)[0]
        st.success(f"Hasil Prediksi: {prediction}")
