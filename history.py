def simpan(teks):
    with open("riwayat.txt", "a") as f:
        f.write(teks + "\n")