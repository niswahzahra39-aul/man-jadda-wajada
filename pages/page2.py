import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


st.header("📊 Visualisasi Data Struktur Pasar Saham")
st.write("Visualisasi struktur pasar saham berdasarkan sektor industri di Bursa Efek Indonesia.")
st.markdown("---")


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "daftarsahambaru.csv"
df = pd.read_csv(DATA_PATH, sep=';', encoding='latin1')


df.columns = df.columns.str.strip()


st.subheader("Tabel Data Saham")
st.dataframe(df)


if "Sector" in df.columns and not df['Sector'].empty:
    
    df["Sector"] = df["Sector"].astype(str)
    
    
    sektor_count = df["Sector"].value_counts()

if st.checkbox("Tampilkan Grafik dan Analisis Saham per Sektor"):
    
    st.subheader("Jumlah Saham per Sektor")
    fig1, ax1 = plt.subplots(figsize=(12,6))
    sektor_count.plot(kind="bar", ax=ax1, color="skyblue")
    ax1.set_xlabel("Sektor Industri")
    ax1.set_ylabel("Jumlah Saham")
    ax1.set_title("Jumlah Saham per Sektor")
    plt.xticks(rotation=45, ha='right') 
    plt.tight_layout()
    st.pyplot(fig1)

    
    st.write(f"""
    Dari grafik di atas terlihat bahwa sektor dengan jumlah saham terbanyak
    adalah **{sektor_count.idxmax()}**, sedangkan sektor dengan jumlah saham paling sedikit
    adalah **{sektor_count.idxmin()}**. Hal ini menunjukkan dominasi sektor {sektor_count.idxmax()} di pasar saham.
    """)

if st.checkbox("Tampilkan Pie Chart Saham per Sektor"):
    
    st.subheader("Persentase Saham per Sektor")
    fig2, ax2 = plt.subplots(figsize=(8,8))
    sektor_count.plot(kind="pie", ax=ax2, autopct="%1.1f%%", startangle=90)
    ax2.set_ylabel("")
    ax2.set_title("Distribusi Saham per Sektor")
    plt.tight_layout()
    st.pyplot(fig2)

    
    st.write(f"""
    Pie chart menunjukkan distribusi saham per sektor. Sektor **{sektor_count.idxmax()}** menguasai
    sebagian besar saham, sementara sektor **{sektor_count.idxmin()}** kontribusinya kecil. Informasi
    ini membantu memahami struktur pasar saham di Indonesia.
    """)

else:
    st.warning("Kolom 'Sektor' tidak ditemukan atau kosong.")
