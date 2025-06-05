import streamlit as st
import joblib

# Load pre-trained model, vectorizer, and label encoder
model = joblib.load('random_forest_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')
encoder = joblib.load('label_encoder.pkl')

def getKmers(sequence, size=5):
    return [sequence[x:x+size].upper() for x in range(len(sequence) - size + 1)]

def predict_dna_sequence(sequence):
    kmer_sequence = getKmers(sequence)
    joined_kmer = ' '.join(kmer_sequence)
    features = vectorizer.transform([joined_kmer])
    prediction = model.predict(features)
    predicted_class = encoder.inverse_transform(prediction)
    return predicted_class[0]

if 'pred_button_clicked' not in st.session_state:
    st.session_state.pred_button_clicked = False

st.set_page_config(page_title="Prediksi Sekuens DNA", layout="wide", initial_sidebar_state="expanded")

st.markdown(
    """
    <style>
    body {
        background: #f9fafb;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stApp {
        max-width: 100%;
        margin: auto;
        padding: 2rem;
        background: white;
        box-shadow: 0 4px 12px rgb(0 0 0 / 0.1);
        border-radius: 12px;
    }
    .css-1v0mbdj.edgvbvh3 {
        font-weight: 700;
        font-size: 2.8rem !important;
        color: #0a52a1;
        margin-bottom: 0.3rem;
    }
    .css-1d391kg p {
        font-size: 1.2rem;
        color: #444444;
        margin-bottom: 2rem;
    }
    textarea.css-1emrehy-textarea {
        min-height: 140px !important;
        font-family: monospace;
        font-size: 1rem;
        border-radius: 8px !important;
        border: 1.8px solid #0a52a1 !important;
        padding: 12px !important;
        resize: vertical;
        max-height: 400px;
    }
    div.stButton > button:first-child {
        background: #0a52a1;
        color: white;
        font-weight: 600;
        padding: 12px 24px;
        border-radius: 8px;
        border: none;
        transition: background-color 0.4s ease, color 0.4s ease, box-shadow 0.4s ease;
        box-shadow: 0 4px 8px rgb(10 82 161 / 0.3);
        width: 180px;
    }
    div.stButton > button:first-child:hover {
        background: #084080;
        box-shadow: 0 6px 14px rgb(8 64 128 / 0.5);
        cursor: pointer;
    }
    /* Animated button after clicked */
    div.stButton > button.clicked {
        background: linear-gradient(270deg, #667eea, #764ba2, #6b8dd6, #af64f5);
        background-size: 800% 800%;
        color: white !important;
        font-weight: 700;
        box-shadow: 0 8px 20px rgb(106 90 205 / 0.7);
        animation: gradientShift 8s ease infinite;
    }
    @keyframes gradientShift {
        0%{background-position:0% 50%;}
        50%{background-position:100% 50%;}
        100%{background-position:0% 50%;}
    }
    .stSuccess {
        font-size: 1.3rem;
        font-weight: 600;
        color: #107c10;
        padding: 1rem 0;
    }
    .stWarning {
        font-size: 1.1rem;
        font-weight: 600;
        color: #d87024;
        padding: 1rem 0;
    }
    .sidebar .css-15tx938 h2 {
        color: #0a52a1;
        font-weight: 700;
        font-size: 1.8rem;
        margin-bottom: 0.4rem;
    }
    .sidebar .css-15tx938 p {
        font-size: 1rem;
        color: #222222;
        line-height: 1.5;
    }
    footer {
        font-size: 0.85rem;
        text-align: center;
        color: #888888;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #e1e1e1;
    }
    @media (max-width: 1024px) {
        .stApp {
            padding: 1rem;
            margin: 0.5rem;
            border-radius: 8px;
        }
        .css-1oe6wyh {
            width: 100% !important;
        }
    }
    @media (max-width: 600px) {
        #MainMenu {display:none;}
        header {display:none;}
        footer {font-size:0.75rem;}
        .stApp {
            padding: 1rem 1rem 4rem 1rem;
            margin: 0 !important;
            box-shadow: none;
            border-radius: 0;
        }
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔬 Prediksi Sekuens DNA")
st.write("""
Masukkan sekuens DNA yang ingin diprediksi ke dalam input di bawah ini.  
Model akan memprediksi sekuens DNA yang telah diinput dan menentukan apakah termasuk diabetes tipe 1, tipe 2, atau Non Diabetes.
""")

st.sidebar.header("📚 Petunjuk Penggunaan")
st.sidebar.write("""
1. Masukkan sekuens DNA Anda di area teks utama.  
2. Pastikan minimal 5 karakter agar dapat diproses (k-mers dibuat dari ukuran 5).  
3. Klik tombol **Prediksi** untuk mendapatkan hasil klasifikasi.  
4. Hasil prediksi akan muncul di bawah tombol.  
5. Gunakan huruf A, T, C, G untuk sekuens DNA.
""")

st.sidebar.header("ℹ️ About")
st.sidebar.write("""
Website ini menggunakan model machine learning berbasis Random Forest untuk memprediksi kelas sekuens DNA terkait risiko diabetes tipe 1, tipe 2, atau Non Diabetes.  
Dibangun dengan Python, Streamlit dan scikit-learn.  
By: NurlChl  
© 2023  
""")

sequence_input = st.text_area("Masukkan Sekuens DNA:", "", height=180)

button_key = "predict_btn"

button_clicked = False
if st.button("Prediksi", key=button_key):
    st.session_state.pred_button_clicked = True
    button_clicked = True

if st.session_state.pred_button_clicked:
    if len(sequence_input) < 5:
        st.warning("Paling sedikit 5 karakter.")
    else:
        predicted_class = predict_dna_sequence(sequence_input)
        st.success(f"Kelas yang diprediksi untuk sekuens DNA yang dimasukkan adalah: **{predicted_class}**")
    st.markdown(
        """
        <script>
        const btn = window.parent.document.querySelector('div.stButton > button');
        if(btn){
            btn.classList.add('clicked');
        }
        </script>
        """, unsafe_allow_html=True)
        
st.markdown('<footer>© 2023 NurlChl. All rights reserved.</footer>', unsafe_allow_html=True)
