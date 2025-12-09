import streamlit as st

pages = [
    st.Page(page="pages/page1.py", title="Home", icon="🏠"),
    st.Page(page="pages/page2.py", title="Visualisasi Data", icon="📊"),
<<<<<<< HEAD
    st.Page(page="pages/page3.py", title="Settings", icon="⚙️",)
=======
    st.Page(page="pages/page3.py", title="Settings", icon="⚙",)
>>>>>>> 602db7bebbde9c91e07d5c6a13311c29945f128b
]

pg = st.navigation(
    pages,
    position="sidebar",
    expanded=True
)

pg.run()