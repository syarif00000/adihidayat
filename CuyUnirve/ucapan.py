def ucapan_selamat_sarjana(Khiefdiatul Ilmi):
    """
    Fungsi untuk membuat ucapan selamat kepada seseorang yang baru saja meraih gelar sarjana.
    """
    ucapan = f"Selamat ya, {Khiefdiatul Ilmi}! Selamat telah meraih gelar Sarjana. Semoga ilmu yang telah kamu dapatkan dapat bermanfaat untuk masa depanmu."
    return ucapan

# Inputkan nama mahasiswa yang baru saja meraih gelar sarjana
nama_mahasiswa = input("Khiefdiatul Ilmi: ")

# Panggil fungsi ucapan_selamat_sarjana() dengan nama mahasiswa sebagai argumen
ucapan = ucapan_selamat_sarjana(nama_mahasiswa)

# Cetak ucapan selamat
print(ucapan)
