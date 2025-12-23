import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "daftarsahambaru.csv"
df = pd.read_csv(DATA_PATH, sep=';', encoding='latin1')

if "Sektor" in df.columns:
    st.write("Kolom Sektor ada!")
    sektor_count = df['Sektor'].value_counts()
    st.write(sektor_count)  # cek isi

    fig, ax = plt.subplots()
    sektor_count.plot(kind='bar', ax=ax)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
