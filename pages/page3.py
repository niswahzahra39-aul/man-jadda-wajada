import streamlit as st

st.header("📋 Analisis dan Kesimpulan")

st.write("""
Halaman ini menyajikan analisis hasil visualisasi data serta
kesimpulan dari penelitian mengenai struktur pasar saham
berdasarkan sektor industri di Bursa Efek Indonesia.
""")

st.markdown("---")


st.subheader("📊 Analisis Hasil Visualisasi")

st.write("""
Berdasarkan grafik jumlah saham per sektor terlihat bahwa sektor Consumer Cyclicals memiliki jumlah saham terbanyak, sementara sektor Healthcare menempati posisi paling sedikit. Hal ini menunjukkan bahwa pasar saham di Indonesia lebih didominasi oleh perusahaan yang bergerak di bidang konsumsi yang bersifat siklis. Sementara itu, dari pie chart distribusi saham per sektor, terlihat bahwa sektor Consumer Cyclicals menguasai porsi terbesar, sedangkan kontribusi sektor Healthcare relatif kecil. Gambaran ini membantu memahami bagaimana struktur pasar saham Indonesia terbagi menurut sektor, dengan konsentrasi yang lebih tinggi pada sektor konsumsi dibandingkan sektor lainnya.""")


st.markdown("---")


st.subheader("📌 Kesimpulan")

st.write("""
Berdasarkan dari analisis grafik jumlah saham dan distribusi saham per sektor, terlihat bahwa pasar saham Indonesia didominasi oleh sektor Consumer Cyclicals, baik dari segi jumlah saham maupun proporsi distribusi. Sektor ini menempati posisi teratas, sedangkan sektor Healthcare memiliki kontribusi paling kecil. Kondisi ini menunjukkan bahwa struktur pasar saham cenderung terkonsentrasi pada sektor konsumsi yang bersifat siklis. Informasi ini penting bagi investor dan pemangku kepentingan untuk memahami dinamika pasar, menilai risiko, serta membuat keputusan investasi yang lebih tepat dengan memperhatikan dominasi sektor-sektor tertentu.
""")


st.markdown("---")


st.subheader("📚 Daftar Pustaka")

st.markdown("""
- IDX. *Daftar Saham*.  
  https://www.idx.co.id/id/data-pasar/data-saham/daftar-saham/
""")

st.caption("📌 Halaman ini berisi analisis dan kesimpulan penelitian.")

