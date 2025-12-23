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
Pasar modal memainkan peran penting dalam perekonomian Indonesia, karena menjadi sarana bagi perusahaan untuk mendapatkan dana sekaligus menjadi pilihan investasi bagi masyarakat. Salah satu indikator utama yang digunakan untuk melihat nilai dan posisi perusahaan di pasar saham adalah kapitalisasi pasar. Perusahaan yang terdaftar di Bursa Efek Indonesia berasal dari berbagai sektor industri dengan karakteristik dan ukuran bisnis yang berbeda, sehingga nilai kapitalisasi pasar di setiap sektor tidak selalu sama. Oleh karena itu, analisis kapitalisasi pasar per sektor dilakukan untuk mengetahui kontribusi
masing-masing sektor terhadap total nilai pasar saham serta memahami struktur pasar saham Indonesia secara lebih jelas.
""")

st.markdown("---")


st.subheader("📊 Deskripsi Data")
st.write("""
Penelitian ini menggunakan data sekunder yang diperoleh dari platform Kaggle, berupa data historis harga saham perusahaan yang terdaftar di Bursa Efek Indonesia (BEI). Dataset mencakup informasi tanggal perdagangan, harga pembukaan, harga penutupan, harga tertinggi, harga terendah, serta volume transaksi. Data kemudian melalui proses pembersihan (data cleaning) untuk menjaga konsistensi dan kelengkapan sebelum diolah menjadi variabel analisis yang relevan.""")

