import streamlit as st

st.markdown("""
# 📈 Analisis Kapitalisasi Pasar Saham  
### Berdasarkan Sektor di Bursa Efek Indonesia
""")

st.markdown("---")



st.subheader("📌 Tugas Kelompok – Man Jadda Wajada")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Anggota Kelompok:**")
    st.markdown("""
    - Riski Pratama Nofianto  
    - Amanda Kharisma  
    """)

with col2:
    st.markdown("&nbsp;")
    st.markdown("""
    - Niswah Aulia Zahra  
    - Azka Safira Farsya  
    """)

st.markdown("---")


st.subheader("📖 Pendahuluan")
st.write("""
Pasar modal memainkan peran penting dalam perekonomian Indonesia, karena menjadi sarana bagi perusahaan untuk mendapatkan dana sekaligus menjadi pilihan investasi bagi masyarakat. Salah satu indikator utama yang digunakan untuk melihat nilai dan posisi perusahaan di pasar saham adalah kapitalisasi pasar. Perusahaan yang terdaftar di Bursa Efek Indonesia berasal dari berbagai sektor industri dengan karakteristik dan ukuran bisnis yang berbeda, sehingga nilai kapitalisasi pasar di setiap sektor tidak selalu sama. Oleh karena itu, analisis kapitalisasi pasar per sektor dilakukan untuk mengetahui kontribusi
masing-masing sektor terhadap total nilai pasar saham serta memahami struktur pasar saham Indonesia secara lebih jelas.
""")

st.markdown("---")


st.subheader("📊 Deskripsi Data")
st.write("""
Penelitian ini menggunakan data sekunder yang diperoleh dari platform Kaggle, berupa data historis harga saham perusahaan yang terdaftar di Bursa Efek Indonesia (BEI). Dataset mencakup informasi tanggal perdagangan, harga pembukaan, harga penutupan, harga tertinggi, harga terendah, serta volume transaksi. Data kemudian melalui proses pembersihan (data cleaning) untuk menjaga konsistensi dan kelengkapan sebelum diolah menjadi variabel analisis yang relevan.""")


st.markdown("---")
st.caption("📌 Halaman ini berisi gambaran umum penelitian dan data yang digunakan.")
st.info("💡 Gunakan menu di samping untuk melihat visualisasi dan analisis data.")