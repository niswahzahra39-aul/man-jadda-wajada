import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.title("Data Visualization")

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot(fig)


df = pd.read_csv("data/DaftarSaham.csv")  

st.write(df.head())

st.header("Analisis")
st.write("Analisis data perusahaan yang terdaftar di Bursa Efek Indonesia menunjukkan bahwa struktur pasar saham sangat beragam dan didominasi oleh sektor Consumer Cyclicals, Financials, dan Industrials. Keragaman ini mencerminkan karakteristik kinerja saham yang berbeda antar sektor; misalnya, sektor finansial dan consumer cenderung stabil, sedangkan sektor energi dan bahan baku lebih dipengaruhi oleh volatilitas komoditas. Berdasarkan kapitalisasi pasar, perusahaan-perusahaan dalam data memiliki rentang market cap yang sangat luas, mulai dari small cap hingga big cap. Perusahaan dengan kapitalisasi besar biasanya lebih stabil dan menjadi pilihan investor institusional, sedangkan perusahaan small cap memiliki potensi return lebih tinggi tetapi diikuti risiko yang besar. Harga saham antar perusahaan juga bervariasi signifikan, dari puluhan rupiah hingga puluhan ribu rupiah per lembar. Variasi harga ini tidak selalu mencerminkan nilai fundamental, namun lebih menggambarkan likuiditas, persepsi pasar, dan jumlah saham yang beredar.
Jika dilihat dari papan pencatatan, perusahaan pada Papan Utama umumnya memiliki fundamental kuat dan performa saham yang lebih stabil, sementara perusahaan di Papan Pengembangan dan Papan Akselerasi memiliki volatilitas lebih tinggi karena berada pada tahap pertumbuhan. Selain itu, umur perusahaan berdasarkan tahun pencatatan menunjukkan bahwa perusahaan yang telah lama terdaftar di BEI cenderung memiliki reputasi lebih kuat dan fluktuasi harga yang lebih rendah dibanding perusahaan yang baru IPO. Secara keseluruhan, data menggambarkan bahwa performa saham di BEI dipengaruhi oleh sektor industri, kapitalisasi pasar, papan pencatatan, harga saham, serta umur pencatatan perusahaan. Analisis ini menunjukkan bahwa pasar saham Indonesia memiliki struktur yang kompleks dengan dinamika risiko dan return yang bervariasi antar kelompok perusahaan, sehingga pemahaman terhadap karakteristik tersebut penting dalam menilai performa saham secara komprehensif.")