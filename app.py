import streamlit as st

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