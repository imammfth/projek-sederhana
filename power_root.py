import math

def hitung_pangkat(bilangan, eksponen):
    try:
        return math.pow(float(bilangan), float(eksponen))
    except Exception as e:
        return f"Error: {e}"

def hitung_akar(bilangan, n=2):
    try:
        bil = float(bilangan)
        akar_n = float(n)
        if bil < 0 and akar_n % 2 == 0:
            return "Error: Akar genap angka negatif"
        return math.pow(bil, 1/akar_n)
    except Exception as e:
        return f"Error: {e}"