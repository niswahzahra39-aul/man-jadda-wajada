import streamlit as st

st.markdown("## 🪜 Steps Mengunduh Data Daftar Saham per Sektor dari BEI (IDX)")

st.markdown("""
### 🧭 Step 1: Membuka Website Resmi BEI
- Buka browser (Chrome/Firefox/Edge)
- Akses website resmi Bursa Efek Indonesia:
   https://www.idx.co.id

### 🧭 Step 2: Masuk ke Menu Data Pasar
- Pada halaman utama IDX, klik menu **Data Pasar**
- Pilih submenu **Data Saham**

### 🧭 Step 3: Mengakses Daftar Saham
- Klik menu **Daftar Saham**
- Halaman akan menampilkan seluruh saham yang tercatat di BEI

### 🧭 Step 4: Melihat Klasifikasi Sektor
- Perhatikan kolom **Sektor** atau **Sub Sektor**
- Data menggunakan klasifikasi **IDX Industrial Classification (IDX-IC)**

### 🧭 Step 5: Mengunduh Data
- Klik tombol **Download / Unduh**
- Pilih format file:
  - 📄 CSV (.csv)
  - 📊 Excel (.xlsx)

### 🧭 Step 6: Menyimpan File
- Simpan file ke dalam folder proyek, contoh:
  `data/DaftarSahamIDX.csv`

### 🧭 Step 7: Data Siap Digunakan
- Data dapat digunakan untuk:
  - Analisis struktur pasar saham
  - Visualisasi jumlah saham per sektor
  - Pengolahan data lanjutan menggunakan Python
""")
