import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.title("Data Visualization")


df = pd.read_csv("data/DaftarSaham.csv")  

pilihan_tampil_tabel = st.checkbox('Tampilkan tabel')
if pilihan_tampil_tabel == True:
st.write(df.head())
st.write(df.tail())
