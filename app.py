import streamlit as st

pages = [
    st.Page(page="pages/page1.py", title="Home", icon="🏠"),

]

pg = st.navigation(
    pages,
    position="sidebar",
    expanded=True
)

pg.run()