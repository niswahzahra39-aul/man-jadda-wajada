import streamlit as st

st.set_page_config(
    page_title="Analisis Kapitalisasi Pasar BEI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
# 📊 Analisis Kapitalisasi Pasar per Sektor di BEI
Aplikasi interaktif untuk menyajikan analisis kapitalisasi pasar
berdasarkan sektor industri di Bursa Efek Indonesia.
""")

st.markdown("---")

with st.sidebar:
    st.markdown("## 🔎 Navigasi")
    st.caption("Gunakan menu di bawah untuk berpindah halaman")
    

pages = [
    st.Page(page="pages/page1.py", title="Home", icon="🏠"),
    st.Page(page="pages/page2.py", title="Visualisasi Data", icon="📊"),
    st.Page(page="pages/page3.py", title="Analisis", icon="📋"),

]

pg = st.navigation(
    pages,
    position="sidebar",
    expanded=True
)

pg.run()