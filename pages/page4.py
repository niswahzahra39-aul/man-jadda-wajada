import streamlit as st

st.title("📥 Cara Mengunduh Data Daftar Saham BEI")

st.markdown("""
Halaman ini berisi panduan langkah-langkah mengunduh data daftar saham
berdasarkan sektor industri dari website resmi Bursa Efek Indonesia (IDX).
""")

st.markdown("---")

st.markdown("""
### 🧭 Step 1: Membuka Website Resmi BEI
- Buka browser (Chrome/Firefox/Edge)
- Akses website resmi Bursa Efek Indonesia:
  https://www.idx.co.id
""")

st.image(
    "../assets/step1_idx_home.png",
    caption="Halaman utama website BEI",
    use_container_width=True
)
