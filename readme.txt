============================================================
        APLIKASI KLASIFIKASI PENYAKIT DIABETES
      BERDASARKAN SEKUENS DNA MENGGUNAKAN RANDOM FOREST
============================================================

Deskripsi Singkat:
-------------------
Aplikasi ini adalah sebuah web sederhana berbasis Streamlit yang digunakan untuk mendeteksi jenis penyakit Diabetes (Tipe 1, Tipe 2, atau Non-Diabetes) berdasarkan input sekuens DNA. Model machine learning yang digunakan adalah Random Forest, dengan proses ekstraksi fitur berbasis metode 5-mers.

Aplikasi ini merupakan bagian dari proyek skripsi dan bertujuan untuk memudahkan proses prediksi dengan antarmuka yang user-friendly.

Fitur Utama:
-------------
- Input sekuens DNA dari pengguna
- Validasi panjang minimum sekuens
- Ekstraksi fitur k-mers
- Prediksi jenis penyakit menggunakan model Random Forest
- Tampilan antarmuka modern dan informatif dengan animasi DNA

Struktur File:
---------------
- `app.py`               : File utama Streamlit untuk menjalankan aplikasi.
- `random_forest_model.pkl` : File model Random Forest yang telah dilatih.
- `vectorizer.pkl`       : File vectorizer (CountVectorizer) untuk mengubah teks k-mers menjadi fitur numerik.
- `label_encoder.pkl`    : Encoder label dari kelas target.
- `requirements.txt`     : Daftar semua library Python yang diperlukan.

Cara Menjalankan Aplikasi:
---------------------------
1. **Clone atau download repository ini ke komputer Anda.**

2. **Buka terminal/command prompt dan masuk ke direktori project:**
cd path_ke_folder_project

3. **Aktifkan virtual environment (opsional tapi disarankan):**
- Untuk Windows:
  ```
  python -m venv venv
  venv\Scripts\activate
  ```
- Untuk macOS/Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

4. **Install semua dependencies yang diperlukan:**
pip install -r requirements.txt


5. **Jalankan aplikasi dengan Streamlit:**
streamlit run app.py


6. **Aplikasi akan terbuka di browser secara otomatis. Jika tidak, akses secara manual di alamat:**
http://localhost:8501


Catatan:
---------
- Pastikan file `random_forest_model.pkl`, `vectorizer.pkl`, dan `label_encoder.pkl` sudah berada dalam direktori yang sama dengan `app.py`.
- Input sekuens DNA harus terdiri dari huruf A, T, C, G dengan minimal 5 karakter.
- Model memanfaatkan ekstraksi fitur berbasis 5-mers dan memiliki akurasi sekitar 93%.

Lisensi:
---------
Aplikasi ini dibuat untuk keperluan skripsi dan bersifat open source untuk tujuan pembelajaran.

Pengembang:
------------
Nama                : Moh Nurul Cholil  
Tahun               : 2025  
Website Portofolio  : https://nurl-chl-site.webflow.io/

============================================================
