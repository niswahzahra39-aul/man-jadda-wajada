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

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "DaftarSahamTerbaru.csv"

df = pd.read_csv(
    DATA_PATH,
    sep=";",
    encoding="latin1",
    engine="python"
)

# 🔧 INI YANG DITAMBAHKAN (PALING PENTING)
df.columns = df.columns.str.strip()

with st.expander("🔍 Lihat Data Saham"):
    st.dataframe(df)

st.subheader("📌 Pilih Sektor Industri")

sektor = st.multiselect(
    "Sektor Industri",
    options=df["Sector"].unique(),
    default=df["Sector"].unique()
)

df_filt = df[df["Sector"].isin(sektor)]

st.markdown("---")

with st.expander("📈 Lihat Grafik & Kesimpulan Kapitalisasi Pasar"):

    marketcap_sector = (
        df_filt.groupby("Sector")["MarketCap"]
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
