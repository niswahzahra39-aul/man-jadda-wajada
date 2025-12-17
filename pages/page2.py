import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.subheader("Data Visualization")


df = pd.read_csv("data/DaftarSaham.csv")  

st.write(df.head())
st.write(df.tail())

st.subheader("Data Kapitalisasi Pasar Berdasarkan Sektor Industri")

marketcap_sector = df.groupby('Sector')['MarketCap'].sum().sort_values(ascending=False)
    
plt.figure()
marketcap_sector.plot(kind='bar')
plt.xlabel("Sektor Industri")
plt.ylabel("Total Kapitalisasi Pasar")
plt.title("Kapitalisasi Pasar Saham Berdasarkan Sektor di Bursa Efek Indonesia")
    
st.pyplot(plt)

st.write("Grafik menunjukkan bahwa kapitalisasi pasar saham di Bursa Efek Indonesia didominasi oleh beberapa sektor industri tertentu, sementara sektor lainnya memiliki kontribusi yang relatif lebih kecil. Hal ini mengindikasikan adanya perbedaan kinerja saham antar sektor, yang mencerminkan perbedaan skala usaha dan nilai pasar perusahaan di masing-masing sektor.")

st.subheader("Data Jumlah Perusahaan per Sektor")

jumlah_perusahaan = df['Sector'].value_counts()

plt.figure()
jumlah_perusahaan.plot(kind='bar')
plt.xlabel("Sektor Industri")
plt.ylabel("Jumlah Perusahaan")
plt.title("Jumlah Perusahaan Terdaftar per Sektor di BEI")
st.pyplot(plt)

st.write("Grafik menunjukkan bahwa jumlah perusahaan yang terdaftar di Bursa Efek Indonesia berbeda-beda antar sektor. Hal ini mencerminkan struktur pasar modal Indonesia, di mana beberapa sektor memiliki jumlah emiten yang lebih banyak dibandingkan sektor lainnya.")