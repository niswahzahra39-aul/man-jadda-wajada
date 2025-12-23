import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.header("📊 Visualisasi Data Struktur Pasar Saham")

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "daftarsahambaru.csv"

df = pd.read_csv(DATA_PATH, sep=';', encoding='latin1')

st.dataframe(df)

if "Sektor" in df.columns and not df['Sektor'].empty:
    sektor_count = df['Sektor'].value_counts()

    # Bar chart
    st.subheader("Jumlah Saham per Sektor")
    fig1, ax1 = plt.subplots()
    sektor_count.plot(kind='bar', ax=ax1, color='skyblue')
    st.pyplot(fig1)

    st.write("Analisis bar chart di sini")

    # Pie chart
    st.subheader("Persentase Saham per Sektor")
    fig2, ax2 = plt.subplots()
    sektor_count.plot(kind='pie', ax=ax2, autopct="%1.1f%%")
    st.pyplot(fig2)

    st.write("Analisis pie chart di sini")
