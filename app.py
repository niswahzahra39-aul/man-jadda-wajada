import streamlit as st

st.set_page_config(
    page_title="Analisis Kapitalisasi Pasar BEI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .stApp {
        background-color: #F8FAFC;
        color: #0F172A;
    }

    .stSidebar {
        background-color: #FFFFFF;
    }

    h1, h2, h3 {
        color: #2563EB;
    }

    div[data-testid="stMetric"] {
        background-color: #FFFFFF;
        padding: 1rem;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

    

pages = [
    st.Page(page="pages/page1.py", title="Home", icon="🏠"),
    st.Page(page="pages/page2.py", title="Visualisasi Data", icon="📊"),
    st.Page(page="pages/page3.py", title="Analisis", icon="📋"),
    st.Page(page="pages/page4.py", title="Cara Mengunduh Data", icon="📝"),

]

pg = st.navigation(
    pages,
    position="sidebar",
    expanded=True
)

pg.run()

st.markdown("---")
st.caption("© 2025 | Analisis Kapitalisasi Pasar BEI | Tugas Akademik")