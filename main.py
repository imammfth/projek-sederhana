import eel
import basic_math
import multi_divide
import power_root
import history_logger

eel.init('web')

@eel.expose
def proses_hitung(angka1, angka2, operator): 
    try:
        angka1 = float(angka1)
        angka2 = float(angka2)
        hasil = 0

        if operator == '+':
            hasil = basic_math.penjumlahan(angka1, angka2)
        elif operator == '-':
            hasil = basic_math.pengurangan(angka1, angka2)
        elif operator == '*':
            hasil = multi_divide.perkalian(angka1, angka2)
        elif operator == '/':
            hasil = multi_divide.pembagian(angka1, angka2)
        elif operator == '^':
            hasil = power_root.hitung_pangkat(angka1, angka2)
        elif operator == 'akar':
            hasil = power_root.hitung_akar(angka1) 
             
        teks = f"{angka1} {operator} {angka2} = {hasil}"
        history_logger.simpan(teks)

        return hasil 
        
    except Exception as e:
        return "Error"

print("Aplikasi Kalkulator Terbuka...")
eel.start('index.html', size=(400, 500))