import streamlit as st
import os

st.write("Cek file:",
         os.path.exists("assets/step1_idx_home.png"))

st.image("assets/step1_idx_home.png")
