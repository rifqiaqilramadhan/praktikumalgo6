def hitung_hari_dalam_bulan(tahun, bulan):
    bulan_hari = [31, 28 + (tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return bulan_hari[bulan - 1] if 1 <= bulan <= 12 else -1

bulan = int(input("Masukkan bulan (1-12): "))
tahun = int(input("Masukkan tahun: "))

jumlah_hari = hitung_hari_dalam_bulan(tahun, bulan)

if jumlah_hari != -1:
    print(f"Jumlah hari dalam bulan {bulan} tahun {tahun} adalah {jumlah_hari} hari.")
else:
    print("Bulan yang dimasukkan tidak valid. Harap masukkan antara 1 hingga 12.")
