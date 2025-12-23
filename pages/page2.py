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

df = pd.read_csv(DATA_PATH)

st.dataframe(df)

