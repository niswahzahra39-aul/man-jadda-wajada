import streamlit as st

st.title("Analisis Kapitalisasi Pasar Saham Berdasarkan Sektor di Bursa Efek Indonesia")



st.header("Tugas Kelompok Man Jadda Wajada")
st.header("Anggota Kelompok")
st.write("__Riski Pratama Novianto__")
st.write("__Amanda Kharisma__")
st.write("__Niswah Aulia Zahra__")
st.write("__Azka Safira Farsya__")



st.subheader("Pendahuluan")
st.write("Pasar modal memainkan peran penting dalam perekonomian Indonesia, karena menjadi sarana bagi perusahaan mendapatkan dana dan juga menjadi pilihan investasi bagi masyarakat. Salah satu indikator utama yang digunakan untuk melihat nilai dan posisi perusahaan di pasar saham adalah kapitalisasi pasar. Perusahaan yang terdaftar di Bursa Efek Indonesia berasal dari berbagai sektor industri, dengan karakteristik dan ukuran bisnis yang berbeda, sehingga nilai kapitalisasi pasar di setiap sektor tidak selalu sama. Karena itu, dilakukan analisis kapitalisasi pasar per sektor di Bursa Efek Indonesia agar dapat mengetahui bagaimana masing-masing sektor berkontribusi terhadap total nilai pasar saham, serta memahami struktur pasar saham Indonesia secara lebih jelas.")

st.subheader("Deskripsi Data")
st.write("""Penelitian ini menggunakan data sekunder yang diunduh dari platform Kaggle, berupa data historis harga saham perusahaan yang terdaftar di Bursa Efek Indonesia (BEI). Dataset tersebut memuat informasi seperti tanggal perdagangan, harga pembukaan, harga penutupan, harga tertinggi, harga terendah, serta volume transaksi. Data kemudian melalui proses cleaning untuk memastikan konsistensi dan kelengkapan, sebelum diolah menjadi variabel analisis seperti return dan volatilitas. Penggunaan dataset dari Kaggle memudahkan proses pengumpulan data karena formatnya sudah terstruktur dan siap digunakan untuk analisis lebih lanjut.""")



