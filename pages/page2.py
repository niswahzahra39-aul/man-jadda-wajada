import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.header("📊 Visualisasi Data Struktur Pasar Saham")

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "daftarsahambaru.csv"

df = pd.read_csv(DATA_PATH, sep=';', encoding='latin1')

df.columns = df.columns.str.strip()

st.subheader("Tabel Data Saham")
st.dataframe(df)


if "Sector" in df.columns:
    df["Sector"] = df["Sector"].astype(str)
    sektor_count = df["Sector"].value_counts()
    
    st.subheader("Jumlah Saham per Sektor")
    fig, ax = plt.subplots()
    sektor_count.plot(kind="bar", ax=ax, color="skyblue")
    ax.set_xlabel("Sektor Industri")
    ax.set_ylabel("Jumlah Saham")
    ax.set_title("Jumlah Saham per Sektor")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)