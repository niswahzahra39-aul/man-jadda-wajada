import streamlit as st

st.header("📋 Analisis dan Kesimpulan")

st.write("""
Halaman ini menyajikan analisis hasil visualisasi data serta
kesimpulan dari penelitian mengenai kapitalisasi pasar saham
berdasarkan sektor industri di Bursa Efek Indonesia.
""")

st.markdown("---")


st.subheader("📊 Analisis Hasil Visualisasi")

st.write("""
Berdasarkan grafik kapitalisasi pasar pada setiap sektor industri, terlihat bahwa nilai kapitalisasi pasar saham di Bursa Efek Indonesia tidak sama antar sektor. Beberapa sektor memiliki kapitalisasi pasar yang lebih besar dibandingkan sektor lainnya, yang menunjukkan bahwa sektor tersebut memiliki peran dominan dalam struktur pasar saham Indonesia.""")

st.write("""
Sektor dengan nilai kapitalisasi pasar yang lebih kecil menunjukkan adanya perbedaan ukuran dan karakteristik perusahaan yang beroperasi di masing-masing sektor. Selain itu, grafik proporsi kapitalisasi pasar menunjukkan bahwa nilai pasar saham di Bursa Efek Indonesia cenderung terkonsentrasi pada sektor-sektor tertentu.""")

st.info("""
💡 **Insight utama:**  
Pergerakan pasar saham secara keseluruhan sangat dipengaruhi oleh
kinerja sektor-sektor dengan kapitalisasi pasar terbesar.
""")

st.markdown("---")


st.subheader("📌 Kesimpulan")

st.write("""
Berdasarkan hasil analisis yang telah dilakukan, dapat disimpulkan bahwa nilai kapitalisasi pasar saham di Bursa Efek Indonesia tidak terdistribusi secara merata antar sektor industri. Beberapa sektor memiliki nilai kapitalisasi pasar yang lebih besar dan cenderung mendominasi pasar saham, sementara sektor lainnya memberikan kontribusi yang relatif lebih kecil.
""")

st.write("""
Perbedaan ini mencerminkan variasi dalam skala usaha dan nilai pasar perusahaan di setiap sektor. Oleh karena itu, sektor industri merupakan faktor penting dalam memahami struktur pasar saham dan penyebaran nilai kapitalisasi pasar di Bursa Efek Indonesia, sehingga dapat menjadi bahan pertimbangan bagi investor dalam memahami kondisi pasar saham secara menyeluruh.
""")

st.markdown("---")


st.subheader("📚 Daftar Pustaka")

st.markdown("""
- Kaggle. *IHSG Stock Data*.  
  https://www.kaggle.com/datasets/muamkh/ihsgstockdata
""")

st.caption("📌 Halaman ini berisi analisis dan kesimpulan penelitian.")

