import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
ASSETS = BASE_DIR / "assets"

st.title("📥 Cara Mengunduh Data Daftar Saham BEI")

st.markdown("""
Halaman ini berisi panduan langkah-langkah mengunduh data daftar saham
berdasarkan sektor industri dari website resmi Bursa Efek Indonesia (IDX).
""")

st.markdown("---")


st.subheader("🧭 Step 1: Membuka Website Resmi BEI")

col1, col2 = st.columns([1.2, 1.8])

with col1:
    st.markdown("""
    - Buka browser (Chrome / Firefox / Edge)
    - Akses website resmi Bursa Efek Indonesia:
    - https://www.idx.co.id
    """)

with col2:
    img1 = ASSETS / "step1_idx_home.png"
    if img1.exists():
        st.image(str(img1), caption="Halaman utama website BEI", use_container_width=True)
    else:
        st.error("❌ Gambar step1_idx_home.png tidak ditemukan di folder assets")

st.markdown("---")


st.subheader("🧭 Step 2: Masuk ke Menu Data Pasar")

col1, col2 = st.columns([1.2, 1.8])

with col1:
    st.markdown("""
    - Klik menu **Data Pasar**
    - Pilih submenu **Data Saham**
    """)

with col2:
    img2 = ASSETS / "step2_data_pasar.png"
    if img2.exists():
        st.image(str(img2), caption="Menu Data Pasar pada website IDX", use_container_width=True)
    else:
        st.error("❌ Gambar step2_data_pasar.png tidak ditemukan di folder assets")

st.markdown("---")


st.subheader("🧭 Step 3: Mengakses Daftar Saham")

col1, col2 = st.columns([1.2, 1.8])

with col1:
    st.markdown("""
    - Klik menu **Daftar Saham**
    - Halaman menampilkan seluruh saham yang tercatat di BEI
    - Data sudah dilengkapi informasi sektor dan subsektor
    """)

with col2:
    img3 = ASSETS / "step3_daftar_saham.png"
    if img3.exists():
        st.image(str(img3), caption="Halaman daftar saham di BEI", use_container_width=True)
    else:
        st.error("❌ Gambar step3_daftar_saham.png tidak ditemukan di folder assets")

st.markdown("---")


st.subheader("🧭 Step 4: Mengunduh Data")

st.markdown("""
- Klik tombol **Unduh / Download**
- Pilih format file:
  - 📄 CSV (.csv)
  - 📊 Excel (.xlsx)
- Simpan file ke dalam folder proyek, misalnya:
  `data/DaftarSahamIDX.csv`
""")

st.markdown("---")

st.success("""
✅ Data berhasil diunduh dan siap digunakan untuk:
- Analisis struktur pasar saham
- Visualisasi jumlah saham per sektor
- Pengolahan data lanjutan menggunakan Python
""")
