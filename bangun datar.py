import math

# Fungsi untuk menghitung panjang jika lebar dan luas diketahui
def hitung_panjang_dari_luas(lebar, luas):
    panjang = luas / lebar
    return panjang

# Fungsi untuk menghitung panjang jika lebar dan keliling diketahui
def hitung_panjang_dari_keliling(lebar, keliling):
    panjang = (keliling / 2) - lebar
    return panjang

# Fungsi untuk menghitung lebar jika panjang dan luas diketahui
def hitung_lebar_dari_luas(panjang, luas):
    lebar = luas / panjang
    return lebar

# Fungsi untuk menghitung lebar jika panjang dan keliling diketahui
def hitung_lebar_dari_keliling(panjang, keliling):
    lebar = (keliling / 2) - panjang
    return lebar

# Fungsi untuk menghitung sisi persegi jika luas diketahui
def hitung_sisi_dari_luas(luas):
    sisi = luas ** 0.5
    return sisi

# Fungsi untuk menghitung sisi persegi jika keliling diketahui
def hitung_sisi_dari_keliling(keliling):
    sisi = keliling / 4
    return sisi

# Fungsi untuk menghitung radius lingkaran jika luas diketahui
def hitung_radius_dari_luas(luas):
    radius = math.sqrt(luas / math.pi)
    return radius

# Fungsi untuk menghitung radius lingkaran jika keliling diketahui
def hitung_radius_dari_keliling(keliling):
    radius = keliling / (2 * math.pi)
    return radius

# Input dari pengguna untuk menghitung panjang, lebar, sisi persegi, atau radius lingkaran
pilihan = input("Apakah Anda ingin menghitung 'panjang', 'lebar', 'sisi persegi', atau 'radius lingkaran'? ").strip().lower()

if pilihan == "panjang":
    lebar = float(input("Masukkan lebar persegi panjang: "))
    pilihan_luas_keliling = input("Apakah Anda mengetahui 'luas' atau 'keliling'? ").strip().lower()
    
    if pilihan_luas_keliling == "luas":
        luas = float(input("Masukkan luas persegi panjang: "))
        panjang = hitung_panjang_dari_luas(lebar, luas)
        print(f"Panjang persegi panjang adalah: {panjang}")
    
    elif pilihan_luas_keliling == "keliling":
        keliling = float(input("Masukkan keliling persegi panjang: "))
        panjang = hitung_panjang_dari_keliling(lebar, keliling)
        print(f"Panjang persegi panjang adalah: {panjang}")
    
    else:
        print("Input tidak valid. Harap masukkan 'luas' atau 'keliling'.")
    
elif pilihan == "lebar":
    panjang = float(input("Masukkan panjang persegi panjang: "))
    pilihan_luas_keliling = input("Apakah Anda mengetahui 'luas' atau 'keliling'? ").strip().lower()
    
    if pilihan_luas_keliling == "luas":
        luas = float(input("Masukkan luas persegi panjang: "))
        lebar = hitung_lebar_dari_luas(panjang, luas)
        print(f"Lebar persegi panjang adalah: {lebar}")
    
    elif pilihan_luas_keliling == "keliling":
        keliling = float(input("Masukkan keliling persegi panjang: "))
        lebar = hitung_lebar_dari_keliling(panjang, keliling)
        print(f"Lebar persegi panjang adalah: {lebar}")
    
    else:
        print("Input tidak valid. Harap masukkan 'luas' atau 'keliling'.")
    
elif pilihan == "sisi persegi":
    pilihan_luas_keliling = input("Apakah Anda mengetahui 'luas' atau 'keliling' dari persegi? ").strip().lower()
    
    if pilihan_luas_keliling == "luas":
        luas = float(input("Masukkan luas persegi: "))
        sisi = hitung_sisi_dari_luas(luas)
        print(f"Sisi persegi adalah: {sisi}")
    
    elif pilihan_luas_keliling == "keliling":
        keliling = float(input("Masukkan keliling persegi: "))
        sisi = hitung_sisi_dari_keliling(keliling)
        print(f"Sisi persegi adalah: {sisi}")
    
    else:
        print("Input tidak valid. Harap masukkan 'luas' atau 'keliling'.")
    
elif pilihan == "radius lingkaran":
    pilihan_luas_keliling = input("Apakah Anda mengetahui 'luas' atau 'keliling' dari lingkaran? ").strip().lower()
    
    if pilihan_luas_keliling == "luas":
        luas = float(input("Masukkan luas lingkaran: "))
        radius = hitung_radius_dari_luas(luas)
        print(f"Radius lingkaran adalah: {radius}")
    
    elif pilihan_luas_keliling == "keliling":
        keliling = float(input("Masukkan keliling lingkaran: "))
        radius = hitung_radius_dari_keliling(keliling)
        print(f"Radius lingkaran adalah: {radius}")
    
    else:
        print("Input tidak valid. Harap masukkan 'luas' atau 'keliling'.")
    
else:
    print("Input tidak valid. Harap masukkan 'panjang', 'lebar', 'sisi persegi', atau 'radius lingkaran'.")

