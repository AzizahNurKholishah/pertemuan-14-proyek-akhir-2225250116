# pertemuan-14-proyek-akhir-2225250116

| **Keterangan** | **Data** |
|---|---|
| **Nama** | Azizah NUr Kholishah |
| **NIM** | 2225250116 |
| **Kelas** | 3-E |

## Deskripsi

Kalkulator Geometri Bangun Datar merupakan program sederhana menggunakan bahasa Python untuk menghitung luas dan keliling beberapa bangun datar. Program dijalankan melalui terminal dengan memilih menu yang tersedia.

## Fitur Wajib

1. Menghitung luas dan keliling persegi.
2. Menghitung luas dan keliling persegi panjang.
3. Menghitung luas dan keliling segitiga.
4. Menghitung luas dan keliling lingkaran.
5. Memvalidasi input agar nilai yang dimasukkan lebih dari nol.
6. Menampilkan hasil perhitungan kepada pengguna.

## Cara Menjalankan

Prasyarat: Python 3 (tanpa library tambahan).

```bash
# 1. Pastikan Python aktif
python3 --version

# 2. Jalankan program
python3 src/main.py
```

Di Windows, gunakan `python` atau `py` jika `python3` tidak dikenali.

## Cara Menjalankan Test

```bash
python3 -m unittest discover -s tests -v
```

Daftar test case ada di [`tests/test_case.md`](tests/test_case.md).

## Contoh Output

```text
================================
     KALKULATOR GEOMETRI
================================
1. Persegi
2. Persegi Panjang
3. Segitiga
4. Lingkaran
5. Keluar

Pilih bangun datar (1-5): 1
Masukkan panjang sisi: 5

--- HASIL PERHITUNGAN ---
Luas: 25.00
Keliling: 20.00
```

## Struktur Folder

```text
kalkulator-geometri/
|-- README.md
|-- proposal.md
|-- .gitignore
|-- src/
|   |-- main.py
|   `-- perhitungan.py
|-- tests/
|   |-- test_case.md
|   `-- test_program.py
`-- output/
    `-- .gitkeep
```


## Penilaian Diri

- [x] Saya dapat menjelaskan masalah proyek dalam 2–3 kalimat.
- [x] Saya dapat menjelaskan pengguna dan manfaat program.
- [x] Saya dapat menunjukkan hubungan kebutuhan → IPO → fungsi → test case.
- [x] Saya dapat menjelaskan struktur folder dan pembagian modul.
- [x] Saya memahami kontribusi saya dalam mengerjakan proyek secara individu.
- [ ] Saya dapat menunjukkan commit rancangan di GitHub.

## Exit Ticket

- **1. Bagian rancangan yang paling siap adalah ...** Bagian rancangan yang paling siap adalah struktur program dan fungsi perhitungan karena pembagian tugas setiap file sudah jelas. File `main.py` digunakan untuk menjalankan menu utama, sedangkan `perhitungan.py` berisi fungsi untuk menghitung luas dan keliling bangun datar.

- **2. Bagian yang masih berisiko adalah ...** Bagian yang masih berisiko adalah proses validasi input dan pengujian program karena perlu dipastikan bahwa program dapat menangani input yang tidak sesuai dan menghasilkan perhitungan yang benar.

- **3. Test case yang paling penting adalah ... karena ...** Test case yang paling penting adalah pengujian input ukuran bangun datar yang tidak valid, seperti nilai nol atau negatif, karena pengujian ini memastikan program dapat menolak ukuran yang tidak sesuai sebelum melakukan perhitungan.

- **4. Target pribadi sebelum Pertemuan 15 adalah ...** Target pribadi sebelum Pertemuan 15 adalah memastikan seluruh fungsi perhitungan berjalan dengan benar, melengkapi pengujian program, memperbaiki kesalahan yang ditemukan, dan memastikan seluruh file proyek sudah tersimpan di GitHub.