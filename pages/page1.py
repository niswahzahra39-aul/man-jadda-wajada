import streamlit as st

st.title("Analisis Performa Saham Perusahaan Terdaftar di Bursa Efek Indonesia")
st.title("Tugas Kelompok Man Jadda Wajada")


st.header("Pendahuluan")
st.write("""Pasar modal merupakan salah satu pilar penting dalam mendukung pertumbuhan ekonomi melalui penyediaan sumber pembiayaan jangka panjang bagi perusahaan serta peluang investasi bagi masyarakat. Di Indonesia, Bursa Efek Indonesia (BEI) menjadi pusat aktivitas perdagangan investor memerlukan informasi dan analisis yang akurat untuk dapat mengevaluasi prospek suatu saham secara lebih objektif. Oleh karena itu, penelitian mengenai analisis performa saham perusahaan yang terdaftar di BEI diperlukan untuk memberikan gambaran yang lebih komprehensif mengenai karakteristik dan perilaku saham di pasar modal Indonesia. Penelitian ini bertujuan untuk menelaah performa saham perusahaan di BEI dengan meninjau aspek return, risiko, dan indikator pasar lainnya. Hasilnya diharapkan dapat memperkaya literatur akademik sekaligus menjadi referensi bagi investor, analis, maupun pihak terkait dalam merumuskan strategi dan keputusan investasi yang lebih tepat.""")

st.header("Deskripsi Data")
st.write("""Penelitian ini menggunakan data sekunder yang diunduh dari platform Kaggle, berupa data historis harga saham perusahaan yang terdaftar di Bursa Efek Indonesia (BEI). Dataset tersebut memuat informasi seperti tanggal perdagangan, harga pembukaan, harga penutupan, harga tertinggi, harga terendah, serta volume transaksi. Data kemudian melalui proses cleaning untuk memastikan konsistensi dan kelengkapan, sebelum diolah menjadi variabel analisis seperti return dan volatilitas. Penggunaan dataset dari Kaggle memudahkan proses pengumpulan data karena formatnya sudah terstruktur dan siap digunakan untuk analisis lebih lanjut.""")


import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.header("Data Visualization")


df = pd.read_csv("data/DaftarSaham.csv")  

st.write(df.head())


st.header("Analisis")
st.write("""Analisis terhadap perusahaan-perusahaan yang tercatat di Bursa Efek Indonesia menunjukkan bahwa komposisi pasar saham cukup beragam, dengan dominasi sektor Consumer Cyclicals, Financials, dan Industrials. Keragaman ini menggambarkan perbedaan karakteristik kinerja saham antar sektor; sektor finansial dan consumer relatif lebih stabil, sedangkan sektor energi dan bahan baku lebih rentan terhadap perubahan harga komoditas. Dari sisi kapitalisasi pasar, perusahaan dalam sampel mencakup rentang yang luas, mulai dari small cap hingga big cap. Perusahaan berkapitalisasi besar biasanya menawarkan stabilitas dan menarik bagi investor institusional, sementara perusahaan small cap berpotensi memberi imbal hasil lebih tinggi namun disertai risiko yang lebih besar. Harga saham juga menunjukkan variasi signifikan, dari nominal sangat rendah hingga tinggi, yang lebih mencerminkan likuiditas, persepsi pasar, dan jumlah saham beredar daripada nilai fundamental.
Berdasarkan papan pencatatan, emiten di Papan Utama umumnya memiliki fundamental lebih kuat dan pergerakan harga yang cenderung stabil. Sebaliknya, emiten di Papan Pengembangan dan Papan Akselerasi sering kali menunjukkan volatilitas lebih tinggi karena masih berada dalam fase pertumbuhan. Selain itu, usia perusahaan sejak pertama kali tercatat di BEI turut memengaruhi fluktuasi harga; perusahaan yang telah lama listing biasanya memiliki reputasi lebih mapan dan pergerakan harga yang lebih stabil dibanding perusahaan yang baru IPO. Secara keseluruhan, data menunjukkan bahwa kinerja saham di BEI dipengaruhi oleh sektor industri, besaran kapitalisasi pasar, papan pencatatan, tingkat harga saham, serta usia listing perusahaan. Hal ini menegaskan bahwa pasar saham Indonesia memiliki struktur yang kompleks dengan dinamika risiko dan imbal hasil yang beragam, sehingga pemahaman mendalam mengenai karakteristik tersebut penting dalam mengevaluasi performa saham secara menyeluruh.""")


st.header("Kesimpulan")

st.markdown("""Data tersebut berisi daftar emiten saham di Bursa Efek Indonesia yang mencakup informasi penting seperti kode saham, nama perusahaan, tanggal listing, jumlah lembar saham beredar, sektor industri, harga terakhir, serta berbagai indikator aktivitas perdagangan. Secara umum, data ini menggambarkan keragaman perusahaan publik di Indonesia dari berbagai sector mulai dari agrikultur, media, asuransi, hingga ritel dengan variasi kapitalisasi dan umur listing yang cukup luas. Informasi ini dapat digunakan untuk analisis pasar modal, seperti penilaian kinerja sektor, identifikasi likuiditas saham, maupun pemetaan karakteristik emiten berdasarkan harga, volume, serta riwayat perdagangannya.""")


st.header("Daftar Pustaka")
st.markdown("https://www.kaggle.com/datasets/muamkh/ihsgstockdata")