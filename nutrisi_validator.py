import streamlit as st

# Judul dan deskripsi aplikasi
st.title("Aplikasi Validasi Data Nutrisi")
st.write("Masukkan informasi nutrisi untuk produk pangan dan aplikasi ini akan memvalidasi input.")

# Input nama produk
nama_produk = st.text_input("Masukkan nama produk:", "")

# Input data nutrisi (kalori, protein, lemak, karbohidrat, dll.)
kalori = st.number_input("Masukkan jumlah kalori (kkal):", min_value=0.0, step=1.0, format="%.1f")
protein = st.number_input("Masukkan jumlah protein (gram):", min_value=0.0, step=0.1, format="%.1f")
lemak = st.number_input("Masukkan jumlah lemak (gram):", min_value=0.0, step=0.1, format="%.1f")
karbohidrat = st.number_input("Masukkan jumlah karbohidrat (gram):", min_value=0.0, step=0.1, format="%.1f")

# Tombol untuk melakukan validasi
if st.button("Validasi Data Nutrisi"):
    # Validasi nama produk
    if not nama_produk.strip():
        st.error("Nama produk tidak boleh kosong.")

    # Validasi jumlah kalori
    if kalori <= 0:
        st.error("Jumlah kalori harus lebih dari 0.")

    # Validasi protein
    if protein < 0:
        st.error("Jumlah protein tidak boleh negatif.")

    # Validasi lemak
    if lemak < 0:
        st.error("Jumlah lemak tidak boleh negatif.")

    # Validasi karbohidrat
    if karbohidrat < 0:
        st.error("Jumlah karbohidrat tidak boleh negatif.")

    # Validasi total gizi (kalori = protein * 4 + lemak * 9 + karbohidrat * 4)
    total_kalori = (protein * 4) + (lemak * 9) + (karbohidrat * 4)

    if total_kalori < kalori:
        st.error("Total kalori yang dihitung lebih kecil dari input kalori. Mohon cek kembali input data.")

    # Jika validasi berhasil
    if all([nama_produk.strip(), kalori > 0, protein >= 0, lemak >= 0, karbohidrat >= 0, total_kalori >= kalori]):
        st.success("Validasi berhasil. Data nutrisi valid.")