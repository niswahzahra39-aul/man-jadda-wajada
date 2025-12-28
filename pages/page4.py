import streamlit as st
from pathlib import Path
from PIL import Image

# =========================
# PATH CONFIG (AMAN STREAMLIT CLOUD)
# =========================
BASE_DIR = Path(__file__).resolve().parents[1]  # root project
ASSETS = BASE_DIR / "assets"

# =========================
# TITLE & INTRO
# =========================
st.title("📥 Cara Mengunduh Data Daftar Saham BEI")

st.markdown("""
Halaman ini berisi panduan langkah-langkah mengunduh data daftar saham
berdasarkan sektor industri dari website resmi Bursa Efek Indonesia (IDX).
""")

st.markdown("---")

# =========================
# HELPER FUNCTION (ANTI MediaFileStorageError)
# =========================
def show_image(filename, caption):
    img_path = ASSETS / filename

    if not img_path.exists():
        st.warning(f"⚠️ Gambar **{filename}** tidak ditemukan di folder assets/")
        return

    try:
        img = Image.open(img_path)
        st.image(img, caption=caption, use_container_width=True)
    except Exception as e:
        st.error(f"❌ Gagal membuka gambar: {filename}\n{e}")

# =========================
# STEP 1
# =========================
st.subheader("🧭 Step 1: Membuka Website Resmi BEI")

col1, col2 = st.columns([1.2, 1.8])

with col1:
    st.markdown("""
    - Buka browser (Chrome / Firefox / Edge)
    - Akses website resmi Bursa Efek Indonesia:
      [https://www.idx.co.id](https://www.idx.co.id)
    """)

with col2:
    show_image("step1_idx_home.png", "Halaman utama website BEI")

st.markdown("---")

# =========================
# STEP 2
# =========================
st.subheader("🧭 Step 2: Masuk ke Menu Data Pasar")

col1, col2 = st.columns([1.2, 1.8])

with col1:
    st.markdown("""
    - Klik menu **Data Pasar**
    - Pilih submenu **Data Saham**
    """)

with col2:
    show_image("step2_data_pasar.png", "Menu Data Pasar pada website IDX")

st.markdown("---")

# =========================
# STEP 3
# =========================
st.subheader("🧭 Step 3: Mengakses Daftar Saham")

col1, col2 = st.columns([1.2, 1.8])

with col1:
    st.markdown("""
    - Klik menu **Daftar Saham**
    - Menampilkan seluruh saham tercatat di BEI
    - Lengkap dengan sektor & subsektor
    """)

with col2:
    show_image("step3_daftar_saham.png", "Halaman daftar saham di BEI")

st.markdown("---")

# =========================
# STEP 4
# =========================
st.subheader("🧭 Step 4: Mengunduh Data")

st.markdown("""
- Klik tombol **Download / Unduh**
- Pilih format:
  - 📄 CSV (.csv)
  - 📊 Excel (.xlsx)
- Simpan ke folder proyek, misalnya:
  `data/DaftarSahamIDX.csv`
""")

st.markdown("---")

st.success("""
✅ Data siap digunakan untuk:
- Analisis struktur pasar saham
- Visualisasi jumlah saham per sektor
- Pengolahan data lanjutan dengan Python
""")
