import streamlit as st

st.markdown("""
<style>
.title-box {
    background: linear-gradient(90deg, #1f4037, #99f2c8);
    padding: 25px;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 30px;
}
.group-box {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
}
.member {
    font-size: 16px;
    margin-bottom: 6px;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="title-box">
    <h1>📈 Analisis Struktur Pasar Saham</h1>
    <h4>Berdasarkan Sektor di Bursa Efek Indonesia</h4>
</div>
""", unsafe_allow_html=True)


st.markdown("### 📌 Tugas Kelompok – <i>Man Jadda Wajada</i>", unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="group-box">
        <h4>👤 Anggota Kelompok</h4>
        <div class="member">• Riski Pratama Novianto</div>
        <div class="member">• Amanda Kharisma</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="group-box">
        <h4>&nbsp;</h4>
        <div class="member">• Niswah Aulia Zahra</div>
        <div class="member">• Azka Safira Farsya</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)


st.subheader("📖 Pendahuluan")
st.write("""
Pasar saham di Bursa Efek Indonesia terdiri dari berbagai sektor industri dengan karakteristik yang berbeda, baik dari sisi jumlah emiten maupun skala perusahaannya. Perbedaan tersebut menyebabkan struktur pasar pada setiap sektor tidak sama, ada sektor yang cenderung didominasi oleh beberapa perusahaan besar dan ada pula yang persaingannya lebih merata. Analisis struktur pasar saham berdasarkan sektor dilakukan untuk memberikan gambaran mengenai pola persaingan dan tingkat penguasaan pasar saham sektoral di Bursa Efek Indonesia.
""")

st.markdown("---")


st.subheader("📊 Deskripsi Data")
st.write("""
Data yang digunakan dalam analisis ini berasal dari perusahaan yang terdaftar di Bursa Efek Indonesia dan dikelompokkan berdasarkan sektor industri. Data ini memuat informasi mengenai sektor usaha dan jumlah saham beredar pada masing-masing emiten, sehingga dapat digunakan untuk melihat distribusi perusahaan dan skala saham beredar di setiap sektor. Data tersebut menjadi dasar dalam menganalisis struktur pasar saham berdasarkan sektor di Bursa Efek Indonesia.""")

