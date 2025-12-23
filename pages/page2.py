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

if "Sektor" in df.columns and not df['Sektor'].empty:
    sektor_count = df['Sektor'].value_counts()


st.subheader("Jumlah Saham per Sektor")
    fig1, ax1 = plt.subplots()
    sektor_count.plot(kind='bar', ax=ax1, color='skyblue')
    ax1.set_xlabel("Sektor Industri")
    ax1.set_ylabel("Jumlah Saham")
    ax1.set_title("Jumlah Saham per Sektor")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig1)

st.write("""
    Dari grafik di atas terlihat bahwa sektor dengan jumlah saham terbanyak
    adalah **sektor X**, sedangkan sektor dengan jumlah saham paling sedikit
    adalah **sektor Y**. Hal ini menunjukkan dominasi sektor X di pasar saham.
    """)