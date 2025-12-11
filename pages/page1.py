import streamlit as st

st.title("Analisis Performa Saham Perusahaan Terdaftar di Bursa Efek Indonesia")
st.title("Tugas Kelompok Man Jadda Wajada")
st.header("Pendahuluan")
st.write("""Pasar modal merupakan salah satu pilar penting dalam mendukung pertumbuhan ekonomi melalui penyediaan sumber pembiayaan jangka panjang bagi perusahaan serta peluang investasi bagi masyarakat. Di Indonesia, Bursa Efek Indonesia (BEI) menjadi pusat aktivitas perdagangan saham yang mencerminkan dinamika kinerja perusahaan, kondisi industri, serta perubahan ekonomi nasional dan global. Pergerakan harga saham sering kali menjadi indikator awal terhadap perubahan fundamental maupun sentimen pasar, sehingga analisis performa saham menjadi aspek penting dalam pengambilan keputusan investasi. Memahami performa saham tidak hanya berkaitan dengan mengukur tingkat pengembalian, tetapi juga menilai risiko yang menyertainya serta faktor-faktor yang memengaruhi fluktuasinya. Investor memerlukan informasi dan analisis yang akurat untuk dapat mengevaluasi prospek suatu saham secara lebih objektif. Oleh karena itu, penelitian mengenai analisis performa saham perusahaan yang terdaftar di BEI diperlukan untuk memberikan gambaran yang lebih komprehensif mengenai karakteristik dan perilaku saham di pasar modal Indonesia. Penelitian ini bertujuan untuk menelaah performa saham perusahaan di BEI dengan meninjau aspek return, risiko, dan indikator pasar lainnya. Hasilnya diharapkan dapat memperkaya literatur akademik sekaligus menjadi referensi bagi investor, analis, maupun pihak terkait dalam merumuskan strategi dan keputusan investasi yang lebih tepat.""")

st.header("Deskripsi Data")
st.write("""Penelitian ini menggunakan data sekunder yang diunduh dari platform Kaggle, berupa data historis harga saham perusahaan yang terdaftar di Bursa Efek Indonesia (BEI). Dataset tersebut memuat informasi seperti tanggal perdagangan, harga pembukaan, harga penutupan, harga tertinggi, harga terendah, serta volume transaksi. Data kemudian melalui proses cleaning untuk memastikan konsistensi dan kelengkapan, sebelum diolah menjadi variabel analisis seperti return dan volatilitas. Penggunaan dataset dari Kaggle memudahkan proses pengumpulan data karena formatnya sudah terstruktur dan siap digunakan untuk analisis lebih lanjut.""")


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
st.write("""Analisis data perusahaan yang terdaftar di Bursa Efek Indonesia menunjukkan bahwa struktur pasar saham sangat beragam dan didominasi oleh sektor Consumer Cyclicals, Financials, dan Industrials. Keragaman ini mencerminkan karakteristik kinerja saham yang berbeda antar sektor; misalnya, sektor finansial dan consumer cenderung stabil, sedangkan sektor energi dan bahan baku lebih dipengaruhi oleh volatilitas komoditas. Berdasarkan kapitalisasi pasar, perusahaan-perusahaan dalam data memiliki rentang market cap yang sangat luas, mulai dari small cap hingga big cap. Perusahaan dengan kapitalisasi besar biasanya lebih stabil dan menjadi pilihan investor institusional, sedangkan perusahaan small cap memiliki potensi return lebih tinggi tetapi diikuti risiko yang besar. Harga saham antar perusahaan juga bervariasi signifikan, dari puluhan rupiah hingga puluhan ribu rupiah per lembar. Variasi harga ini tidak selalu mencerminkan nilai fundamental, namun lebih menggambarkan likuiditas, persepsi pasar, dan jumlah saham yang beredar.

Jika dilihat dari papan pencatatan, perusahaan pada Papan Utama umumnya memiliki fundamental kuat dan performa saham yang lebih stabil, sementara perusahaan di Papan Pengembangan dan Papan Akselerasi memiliki volatilitas lebih tinggi karena berada pada tahap pertumbuhan. Selain itu, umur perusahaan berdasarkan tahun pencatatan menunjukkan bahwa perusahaan yang telah lama terdaftar di BEI cenderung memiliki reputasi lebih kuat dan fluktuasi harga yang lebih rendah dibanding perusahaan yang baru IPO. Secara keseluruhan, data menggambarkan bahwa performa saham di BEI dipengaruhi oleh sektor industri, kapitalisasi pasar, papan pencatatan, harga saham, serta umur pencatatan perusahaan. Analisis ini menunjukkan bahwa pasar saham Indonesia memiliki struktur yang kompleks dengan dinamika risiko dan return yang bervariasi antar kelompok perusahaan, sehingga pemahaman terhadap karakteristik tersebut penting dalam menilai performa saham secara komprehensif."""
        )


st.header("Kesimpulan")
st.write("""Data tersebut berisi daftar emiten saham di Bursa Efek Indonesia yang mencakup informasi penting seperti kode saham, nama perusahaan, tanggal listing, jumlah lembar saham beredar, sektor industri, harga terakhir, serta berbagai indikator aktivitas perdagangan. Secara umum, data ini menggambarkan keragaman perusahaan publik di Indonesia dari berbagai sector mulai dari agrikultur, media, asuransi, hingga ritel dengan variasi kapitalisasi dan umur listing yang cukup luas. Informasi ini dapat digunakan untuk analisis pasar modal, seperti penilaian kinerja sektor, identifikasi likuiditas saham, maupun pemetaan karakteristik emiten berdasarkan harga, volume, serta riwayat perdagangannya."""
        )