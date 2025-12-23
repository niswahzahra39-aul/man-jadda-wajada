import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.header("📊 Visualisasi Data Struktur Pasar Saham")

st.write("""
Halaman ini menyajikan visualisasi data struktur pasar saham
berdasarkan sektor industri di Bursa Efek Indonesia.
""")

st.markdown("---")

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "daftarsahambaru.csv"

df = pd.read_csv(DATA_PATH, sep=';', encoding='latin1')

st.dataframe(df)

if "Sektor" in df.columns:
    sektor_count = df['Sektor'].value_counts()

with st.expander("📈 Lihat Grafik dan Analisis Saham per Sektor"):
    st.subheader("Jumlah Saham per Sektor")
        fig1, ax1 = plt.subplots()
        sektor_count.plot(kind='bar', ax=ax1, color='skyblue')
        ax1.set_xlabel("Sektor Industri")
        ax1.set_ylabel("Jumlah Saham")
        ax1.set_title("Jumlah Saham per Sektor")
        plt.xticks(rotation=45)
        st.pyplot(fig1)

st.write("""
        Dari grafik di atas, terlihat sektor dengan jumlah saham terbanyak
        adalah **sektor X**, sedangkan sektor dengan jumlah saham paling sedikit
        adalah **sektor Y**. Hal ini menunjukkan bahwa sektor X lebih dominan
        di pasar saham Indonesia.
        """)

st.subheader("Persentase Saham per Sektor")
        fig2, ax2 = plt.subplots()
        sektor_count.plot(kind='pie', ax=ax2, autopct="%1.1f%%", startangle=90)
        ax2.set_ylabel("")
        ax2.set_title("Distribusi Saham per Sektor")
        st.pyplot(fig2)

st.write("""
        Pie chart menunjukkan distribusi saham per sektor. Sektor X menguasai
        sebagian besar saham, sedangkan sektor Y kontribusinya kecil. Informasi
        ini berguna untuk memahami struktur pasar saham di Indonesia.
        """)