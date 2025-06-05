import streamlit as st
import joblib
from streamlit.components.v1 import html

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

st.set_page_config(
    page_title="DNA Sequence Classifier",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🧬"
)

# Custom CSS with enhanced styling
st.markdown(
    """
    <style>
    :root {
        --primary: #4361ee;
        --secondary: #3a0ca3;
        --accent: #f72585;
        --light: #f8f9fa;
        --dark: #212529;
        --success: #4cc9f0;
        --warning: #f8961e;
        --danger: #ef233c;
    }
    
    body {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem 1rem;
        background: rgba(255, 255, 255, 0.95);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
        backdrop-filter: blur(4px);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    
    .header-container {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
        padding: 2rem;
        border-radius: 12px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(67, 97, 238, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .header-container::before {
        content: "";
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
        transform: rotate(30deg);
    }
    
    .stTitle h1 {
        font-size: 2.8rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        color: white;
        position: relative;
    }
    
    .stTitle h1::after {
        content: "";
        display: block;
        width: 80px;
        height: 4px;
        background: var(--accent);
        margin: 0.5rem 0;
        border-radius: 2px;
    }
    
    .stMarkdown p {
        font-size: 1.1rem;
        line-height: 1.6;
        color: black;
        margin-bottom: 0;
    }
    
    .dna-icon {
        font-size: 2rem;
        margin-right: 0.5rem;
        vertical-align: middle;
    }
    
    textarea {
        min-height: 180px !important;
        font-family: 'Courier New', monospace !important;
        font-size: 1rem !important;
        border-radius: 12px !important;
        border: 2px solid var(--primary) !important;
        padding: 16px !important;
        box-shadow: 0 4px 12px rgba(67, 97, 238, 0.1) !important;
        transition: all 0.3s ease !important;
    }
    
    textarea:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 4px 16px rgba(247, 37, 133, 0.2) !important;
        outline: none !important;
    }
    
    .stButton button {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
        color: white !important;
        font-weight: 600;
        font-size: 1.1rem;
        padding: 14px 28px;
        border-radius: 50px;
        border: none;
        transition: all 0.4s ease;
        box-shadow: 0 4px 15px rgba(67, 97, 238, 0.4);
        width: 200px;
        position: relative;
        overflow: hidden;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(67, 97, 238, 0.5);
    }
    
    .stButton button::after {
        content: "";
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: all 0.5s ease;
    }
    
    .stButton button:hover::after {
        left: 100%;
    }
    
    .stButton button.clicked {
        background: linear-gradient(135deg, var(--accent) 0%, #b5179e 100%);
        animation: pulse 1.5s infinite;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(247, 37, 133, 0.7); }
        70% { box-shadow: 0 0 0 12px rgba(247, 37, 133, 0); }
        100% { box-shadow: 0 0 0 0 rgba(247, 37, 133, 0); }
    }
    
    .result-container {
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        background: white;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        border-left: 4px solid var(--primary);
        transition: all 0.3s ease;
    }
    
    .result-container:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
    
    .stSuccess {
        font-size: 1.4rem;
        font-weight: 700;
        color: var(--primary);
        padding: 0.5rem 0;
    }
    
    .stWarning {
        font-size: 1.2rem;
        font-weight: 600;
        color: var(--warning);
        padding: 0.5rem 0;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 0 12px 12px 0;
        padding: 1.5rem;
        box-shadow: 4px 0 20px rgba(0,0,0,0.05);
    }
    
    .sidebar h2 {
        color: var(--secondary);
        font-weight: 700;
        font-size: 1.6rem;
        margin-bottom: 1rem;
        position: relative;
    }
    
    .sidebar h2::after {
        content: "";
        display: block;
        width: 50px;
        height: 3px;
        background: var(--accent);
        margin: 0.5rem 0;
        border-radius: 2px;
    }
    
    .sidebar p {
        font-size: 1rem;
        color: var(--dark);
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }
    
    footer {
        font-size: 0.9rem;
        text-align: center;
        color: var(--dark);
        margin-top: 3rem;
        padding-top: 1.5rem;
        border-top: 1px solid rgba(0,0,0,0.1);
        position: relative;
    }
    
    footer::before {
        content: "🧬";
        font-size: 1.5rem;
        position: absolute;
        top: -0.8rem;
        left: 50%;
        transform: translateX(-50%);
        background: white;
        padding: 0 1rem;
    }
    
    .dna-animation {
        position: absolute;
        right: 2rem;
        top: 50%;
        transform: translateY(-50%);
        opacity: 0.1;
        z-index: 0;
    }
    
    @media (max-width: 768px) {
        .stApp {
            padding: 1rem;
            border-radius: 0;
        }
        
        .header-container {
            padding: 1.5rem;
        }
        
        .stTitle h1 {
            font-size: 2rem;
        }
        
        .dna-animation {
            display: none;
        }
    }
    
    /* DNA strand animation */
    .dna-strand {
        position: relative;
        width: 100px;
        height: 200px;
    }
    
    .dna-strand::before {
        content: "";
        position: absolute;
        left: 50%;
        top: 0;
        bottom: 0;
        width: 2px;
        background: linear-gradient(to bottom, transparent 0%, var(--primary) 50%, transparent 100%);
        transform: translateX(-50%);
    }
    
    .dna-strand .node {
        position: absolute;
        width: 12px;
        height: 12px;
        background: var(--accent);
        border-radius: 50%;
        left: 50%;
        transform: translateX(-50%);
        animation: dnaFloat 3s infinite ease-in-out;
    }
    
    @keyframes dnaFloat {
        0%, 100% { transform: translateX(-50%) translateY(0) scale(1); }
        50% { transform: translateX(-50%) translateY(-5px) scale(1.1); }
    }
    </style>
    """, unsafe_allow_html=True)


# Header section
st.markdown(
    """
   <div class="header-container">
        <div class="dna-animation">
            <div class="dna-strand">
                <div class="node" style="top: 10%; animation-delay: 0s;"></div>
                <div class="node" style="top: 30%; animation-delay: 0.2s;"></div>
                <div class="node" style="top: 50%; animation-delay: 0.4s;"></div>
                <div class="node" style="top: 70%; animation-delay: 0.6s;"></div>
                <div class="node" style="top: 90%; animation-delay: 0.8s;"></div>
            </div>
        </div>
        <div class="stTitle">
            <h1><span class="dna-icon">🧬</span> Klasifikasi Sekuens DNA</h1>
        </div>
        <div class="stMarkdown">
            <p style="color:white;">Memprediksi apakah sekuens DNA terkait dengan Diabetes Tipe 1, Diabetes Tipe 2, atau kondisi Non-Diabetes menggunakan model Random Forest.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Main content
col1, col2 = st.columns([6, 4])

with col1:
    sequence_input = st.text_area(
        "Masukkan Sekuens DNA:",
        "",
        height=200,
        placeholder="Contoh: ATGCGCTAACGT... (minimal 5 karakter)",
        help="Masukkan urutan DNA menggunakan karakter A, T, C, G"
    )
    
    button_key = "predict_btn"
    button_clicked = False
    if st.button("Prediksi", key=button_key, type="primary"):
        st.session_state.pred_button_clicked = True
        button_clicked = True

    if st.session_state.pred_button_clicked:
        if len(sequence_input) < 5:
            st.warning("Masukkan setidaknya 5 karakter untuk prediksi.")
        else:
            with st.spinner("Menganalisis sekuens..."):
                predicted_class = predict_dna_sequence(sequence_input)
                st.markdown(
                    f"""
                    <div class="result-container">
                        <div class="stSuccess">
                            Hasil Prediksi: <strong>{predicted_class}</strong>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
        
        st.markdown(
            """
            <script>
            const btn = window.parent.document.querySelector('div.stButton > button');
            if(btn){
                btn.classList.add('clicked');
                setTimeout(() => {
                    btn.classList.remove('clicked');
                }, 3000);
            }
            </script>
            """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); 
                padding: 1.5rem; 
                border-radius: 12px; 
                height: 100%;">
        <h3 style="color: #3a0ca3; border-bottom: 2px solid #f72585; 
                   padding-bottom: 0.5rem; margin-top: 0;">Info</h3>
       <p><strong>Karakter yang valid:</strong> A, T, C, G</p>
        <p><strong>Panjang minimum:</strong> 5 karakter</p>
        <p><strong>Contoh sekuens:</strong></p>
        <div style="background: white; padding: 0.5rem; border-radius: 6px; 
                    font-family: monospace; font-size: 0.9rem; 
                    border-left: 3px solid #4361ee;">
            ATGCGCTAACGTAGCTAGCT...
        </div>
    </div>
    """, unsafe_allow_html=True)

# Sidebar content
st.sidebar.markdown("""
<div style="margin-bottom: 2rem;">
    <h2>📚 Petunjuk</h2>
    <p>1. Masukkan sekuens DNA yang ingin di prediksi pada input yang tersedia</p>
    <p>2. Klik button predict untuk melakukan prediksi</p>
    <p>3. Hasil prediksi akan menunjukkan penyakit diabetes tipe 1, tipe 2 atau Non Diabetes</p>
</div>

<div style="margin-bottom: 2rem;">
    <h2>⚙️ Detail Lainnya</h2>
    <p><strong>Algoritma:</strong> Random Forest</p>
    <p><strong>Akurasi:</strong> 93%</p>
    <p><strong>K-mers:</strong> 5-mer</p>
</div>

<div>
    <h2>ℹ️ Tentang</h2>
    <p>Website ini dikembangkan untuk tujuan mempermudah melakukan prediksi dari model yang diperoleh pada saat pengerjaan skripsi.</p>
    <p style="font-size: 0.9rem; color: #6c757d;">By: Moh Nurul Cholil<br>© 2025</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<footer>
    © 2025 develop by <a href="https://nurl-chl-site.webflow.io/">NurlChl</a> | Website hasil skripsi
</footer>
""", unsafe_allow_html=True)

# Add some JavaScript for additional interactivity
html("""
<script>
// Add hover effect to result container
document.addEventListener('mouseover', function(e) {
    if (e.target.closest('.result-container')) {
        e.target.closest('.result-container').style.transform = 'translateY(-3px)';
        e.target.closest('.result-container').style.boxShadow = '0 8px 25px rgba(0,0,0,0.1)';
    }
});

document.addEventListener('mouseout', function(e) {
    if (e.target.closest('.result-container')) {
        e.target.closest('.result-container').style.transform = '';
        e.target.closest('.result-container').style.boxShadow = '';
    }
});
</script>
""")