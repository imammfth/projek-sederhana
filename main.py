import eel
import basic_math
import multi_divide
import power_root
import history_logger

# Kasih tau Eel folder web-nya
eel.init('web')

# Fungsi ini yang akan dipanggil oleh JavaScript saat user klik tombol '='
@eel.expose
def proses_hitung(angka1, operator, angka2):
    try:
        angka1 = float(angka1)
        angka2 = float(angka2)
        hasil = 0

        # MENGHUBUNGKAN KODE TEMAN-TEMANMU
        if operator == '+':
            hasil = basic_math.tambah(angka1, angka2)
        elif operator == '-':
            hasil = basic_math.kurang(angka1, angka2)
        elif operator == '*':
            hasil = multi_divide.kali(angka1, angka2)
        elif operator == '/':
            hasil = multi_divide.bagi(angka1, angka2)
        # Tambahkan pangkat dari power_root.py kalau sudah ada
        
        # Simpan ke riwayat (Tugas Anggota 5)
        teks = f"{angka1} {operator} {angka2} = {hasil}"
        history_logger.simpan(teks)

        return hasil # Kirim balik hasilnya ke layar (HTML)
        
    except Exception as e:
        return "Error"

# Jalankan aplikasinya
print("Aplikasi Kalkulator Terbuka...")
eel.start('index.html', size=(400, 500))