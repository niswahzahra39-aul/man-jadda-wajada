import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.header("📊 Visualisasi Data Kapitalisasi Pasar")

st.write("""
Halaman ini menyajikan visualisasi data kapitalisasi pasar saham
berdasarkan sektor industri di Bursa Efek Indonesia.
""")

st.markdown("---")

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "daftarsahambaru.xlsx"

df = pd.read_excel(
    DATA_PATH,
    sep=";",
    encoding="latin1",
    engine="python"
)

# Bersihkan nama kolom
df.columns = df.columns.str.strip()

# 🔍 Deteksi kolom sektor otomatis
if "Sector" in df.columns:
    sector_col = "Sector"
elif "Sektor" in df.columns:
    sector_col = "Sektor"
else:
    st.error("Kolom sektor tidak ditemukan di dataset.")
    st.write("Kolom yang tersedia:", df.columns.tolist())
    st.stop()

with st.expander("🔍 Lihat Data Saham"):
    st.dataframe(df)

st.subheader("📌 Pilih Sektor Industri")

sektor = st.multiselect(
    "Sektor Industri",
    options=df[sector_col].unique(),
    default=df[sector_col].unique()
)

df_filt = df[df[sector_col].isin(sektor)]

st.markdown("---")

with st.expander("📈 Lihat Grafik & Kesimpulan Kapitalisasi Pasar"):

    marketcap_sector = (
        df_filt.groupby(sector_col)["MarketCap"]
        .sum()
        .sort_values(ascending=False)
    )

    st.subheader("📊 Kapitalisasi Pasar Saham per Sektor")

    fig, ax = plt.subplots(figsize=(10, 5))
    marketcap_sector.plot(kind="bar", ax=ax)

    ax.set_xlabel("Sektor Industri")
    ax.set_ylabel("Total Kapitalisasi Pasar")
    ax.set_title("Kapitalisasi Pasar Saham per Sektor di Bursa Efek Indonesia")
    plt.xticks(rotation=45, ha="right")

    st.pyplot(fig)

    st.markdown("### 📝 Kesimpulan")
    st.write("""
    Berdasarkan grafik batang di atas, dapat disimpulkan bahwa kapitalisasi pasar
    saham di Bursa Efek Indonesia tidak tersebar secara merata antar sektor industri.
    Beberapa sektor menunjukkan nilai kapitalisasi pasar yang lebih besar dibandingkan
    sektor lainnya, yang menandakan adanya dominasi sektor tertentu dalam struktur
    pasar saham. Kondisi ini mencerminkan perbedaan skala perusahaan dan minat investor
    pada masing-masing sektor industri.
    """)
