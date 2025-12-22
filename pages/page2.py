import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header("📊 Visualisasi Data Kapitalisasi Pasar")

st.write("""
Halaman ini menyajikan visualisasi data kapitalisasi pasar saham
berdasarkan sektor industri di Bursa Efek Indonesia.
""")

st.markdown("---")


from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "DaftarSahamTerbaru.csv"

df = pd.read_csv(
    DATA_PATH,
    sep=";",            
    encoding="latin1",  
    engine="python"     
)
  

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

col1, col2 = st.columns(2)


with col1:
    st.subheader("📈 Kapitalisasi Pasar per Sektor")

    marketcap_sector = (
        df_filt.groupby("Sector")["MarketCap"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots()
    marketcap_sector.plot(kind="bar", ax=ax)
    ax.set_xlabel("Sektor Industri")
    ax.set_ylabel("Total Kapitalisasi Pasar")
    ax.set_title("Kapitalisasi Pasar Saham per Sektor")

    st.pyplot(fig)

    st.caption("""
    Grafik batang menunjukkan perbedaan total kapitalisasi pasar
    antar sektor industri di Bursa Efek Indonesia.
    """)


with col2:
    st.subheader("🥧 Proporsi Kapitalisasi Pasar")

    fig2, ax2 = plt.subplots()
    ax2.pie(
        marketcap_sector,
        labels=marketcap_sector.index,
        autopct="%1.1f%%",
        startangle=90
    )
    ax2.set_title("Proporsi Kapitalisasi Pasar Saham per Sektor")

    st.pyplot(fig2)

    st.caption("""
    Grafik lingkaran menggambarkan kontribusi relatif masing-masing
    sektor terhadap total kapitalisasi pasar saham di BEI.
    """)

st.markdown("---")

with st.expander("📝 Interpretasi Visualisasi"):
    st.write("""Hasil visualisasi menunjukkan bahwa kapitalisasi pasar saham di Bursa Efek Indonesia tidak terdistribusi secara merata antar sektor. Beberapa sektor memiliki nilai kapitalisasi yang jauh lebih besar, yang mengindikasikan dominasi sektor tertentu dalam struktur pasar saham.""")
