# CRUD Toko HP Xiaomi (contoh)
Capstone Project Module 1
```
StudentID : JCDSOL-009-002
Kelas     : JCDSOL-09 (WA)
Topik     : Penjualan Barang Toko
```
## Dataset
Dataset awal tersimpan dalam dictionary dengan 7 buah keys
```
| Kode          |Seri   |  Tipe         | RAM   |    Internal   | Warna         | Stok  | Harga |
| PF4-6128Gn    |POCO   | POCO F4       | 6GB   |     128GB     | Green         |  3    | 5200k |
| PF4-6128Ba    |POCO   | POCO F4       | 6GB   |     128GB     | Black         |  10   | 5200k |
| PF4-8256Si    |POCO   | POCO F4       | 8GB   |     256GB     | Silver        |  2    | 5700k |
| PF4-8256Gn    |POCO   | POCO F4       | 8GB   |     256GB     | Green         |  8    | 5700k |
| PF4-8256Ba    |POCO   | POCO F4       | 8GB   |     256GB     | Black         |  0    | 5700k |
| PM5-464Ba     |POCO   | POCO M5       | 4GB   |     64GB      | Black         |  6    | 2100k |
| PM5-464Gn     |POCO   | POCO M5       | 4GB   |     64GB      | Green         |  3    | 2100k |
| PM5-464Ye     |POCO   | POCO M5       | 4GB   |     64GB      | Yellow        |  0    | 2100k |
| PM5-4128Ba    |POCO   | POCO M5       | 4GB   |     128GB     | Black         |  6    | 2400k |
| PM5-4128Gn    |POCO   | POCO M5       | 4GB   |     128GB     | Green         |  8    | 2400k |
| PM5-4128Ye    |POCO   | POCO M5       | 4GB   |     128GB     | Yellow        |  6    | 2400k |
| X12T-8256Ba   |Xiaomi | Xiaomi 12T    | 8GB   |     256GB     | Black         |  9    | 6600k |
| X12T-8256Bu   |Xiaomi | Xiaomi 12T    | 8GB   |     256GB     | Blue          |  9    | 6600k |
| N11P-8128Bu   |Redmi  | Note 11 Pro   | 8GB   |     128GB     | Blue          |  3    | 4100k |
| N11P-8128Gy   |Redmi  | Note 11 Pro   | 8GB   |     128GB     | Gray          |  4    | 4100k |
```
## Menu dan Kata Sandi
Terdapat 3 menu utama
```
1. Penjualan
2. Menu Admin
3. Keluar Aplikasi
```
Menu penjualan merupakan menu untuk handle kegiatan pembelian barang, yang nantinya stok pada katalog akan berkurang sesuai jumlah barang yang terjual.

Menu Admin membutuhkan kata sandi agar bisa diakses. Penambahan kata sandi idealnya untuk melindungi data katalog toko dari perubahan dari pihak yang tidak diinginkan. Value kata sandi untuk contoh ini disimpan pada variabel **kata_sandi**.

Kata sandi default adalah **admin**

## CRUD
Penggunaan CRUD yang mendekati flow program yang diberikan terdapat pada di dalam Menu Admin. Ada 5 pilihan dalam **Menu Admin**.
```
1. Tampilkan Katalog Toko --> Read
2. Tambah Data ke Katalog --> Create
3. Ubah Data di Katalog ----> Update
4. Hapus Data dari Katalog -> Delete
5. Kembali ke Homepage -----> break
```
Masing-masing menu sudah mewaliki bagian-bagian dari CRUD
