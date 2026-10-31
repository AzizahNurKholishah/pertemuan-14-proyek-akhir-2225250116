
from perhitungan import (
    hitung_persegi,
    hitung_persegi_panjang,
    hitung_segitiga,
    hitung_lingkaran
)


def menu():
    print("\n=== KALKULATOR GEOMETRI ===")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Keluar")


def main():
    while True:
        menu()
        pilihan = input("Pilih bangun datar (1-5): ")

        if pilihan == "1":
            sisi = float(input("Masukkan panjang sisi: "))

            if sisi <= 0:
                print("Sisi harus lebih dari 0!")
                continue

            luas, keliling = hitung_persegi(sisi)

        elif pilihan == "2":
            panjang = float(input("Masukkan panjang: "))
            lebar = float(input("Masukkan lebar: "))

            if panjang <= 0 or lebar <= 0:
                print("Panjang dan lebar harus lebih dari 0!")
                continue

            luas, keliling = hitung_persegi_panjang(
                panjang, lebar
            )

        elif pilihan == "3":
            alas = float(input("Masukkan alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            a = float(input("Masukkan sisi pertama: "))
            b = float(input("Masukkan sisi kedua: "))
            c = float(input("Masukkan sisi ketiga: "))

            if min(alas, tinggi, a, b, c) <= 0:
                print("Semua nilai harus lebih dari 0!")
                continue

            if a + b <= c or a + c <= b or b + c <= a:
                print("Ketiga sisi tidak membentuk segitiga!")
                continue

            luas, keliling = hitung_segitiga(
                alas, tinggi, a, b, c
            )

        elif pilihan == "4":
            jari_jari = float(input("Masukkan jari-jari: "))

            if jari_jari <= 0:
                print("Jari-jari harus lebih dari 0!")
                continue

            luas, keliling = hitung_lingkaran(jari_jari)

        elif pilihan == "5":
            print("Terima kasih telah menggunakan program!")
            break

        else:
            print("Pilihan tidak tersedia!")
            continue

        print("\n--- HASIL PERHITUNGAN ---")
        print(f"Luas: {luas:.2f}")
        print(f"Keliling: {keliling:.2f}")


if __name__ == "__main__":
    main()
