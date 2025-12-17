import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.title("Data Visualization")


df = pd.read_csv("data/DaftarSaham.csv")  

st.write(df.head())
st.write(df.tail())

tampil = st.checkbox("Tampilkan grafik kapitalisasi pasar per sektor")

if tampil:
    marketcap_sector = df.groupby('Sector')['MarketCap'].sum().sort_values(ascending=False)
    
    plt.figure()
    marketcap_sector.plot(kind='bar')
    plt.xlabel("Sektor Industri")
    plt.ylabel("Total Kapitalisasi Pasar")
    plt.title("Kapitalisasi Pasar Saham Berdasarkan Sektor di Bursa Efek Indonesia")
    
    st.pyplot(plt)