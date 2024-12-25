# cryptographygui
# Deskripsi Tugas

Tugas ini terdiri dari tiga aplikasi yang berfungsi untuk melakukan enkripsi, dekripsi, dan steganografi. Berikut adalah rincian dari masing-masing aplikasi:

## 1. Aplikasi Enkripsi dan Dekripsi DES

### Deskripsi:
Aplikasi ini menggunakan algoritma DES (Data Encryption Standard) untuk mengenkripsi dan mendekripsi teks. Pengguna dapat memasukkan teks dan kunci (harus 8 karakter) untuk melakukan enkripsi dan dekripsi.

### Cara Menjalankan:
1. Jalankan file `desgui.py`.
2. Masukkan teks yang ingin dienkripsi dan kunci yang valid.
3. Klik tombol "Enkripsi" untuk mendapatkan teks terenkripsi, dan "Dekripsi" untuk mendapatkan teks asli.

---

## 2. Aplikasi Kalkulator Caesar Cipher

### Deskripsi:
Aplikasi ini menerapkan metode Caesar Cipher untuk enkripsi dan dekripsi teks dengan pergeseran karakter. Pengguna dapat memasukkan teks dan nilai pergeseran untuk melakukan proses tersebut.

### Cara Menjalankan:
1. Jalankan file `kalkulator_caesar.py`.
2. Masukkan teks dan nilai pergeseran (antara 1 dan 25).
3. Klik tombol "Enkripsi" untuk mendapatkan hasil enkripsi, dan "Dekripsi" untuk mendapatkan teks asli.

---

## 3. Aplikasi Steganografi

### Deskripsi:
Aplikasi ini memungkinkan pengguna untuk menyembunyikan pesan dalam gambar menggunakan teknik steganografi. Pengguna dapat menyembunyikan pesan dalam gambar PNG atau JPG dan mengekstrak pesan dari gambar tersebut.

### Cara Menjalankan:
1. Jalankan file `steganogui.py`.
2. Pilih gambar untuk menyembunyikan pesan atau untuk mengekstrak pesan.
3. Ikuti instruksi di GUI untuk menyembunyikan atau menampilkan pesan.

---

## Cara Menjalankan

Untuk menjalankan aplikasi-aplikasi ini, pastikan Anda memiliki Python terinstal di sistem Anda. Anda juga perlu menginstal beberapa pustaka yang diperlukan. Berikut adalah langkah-langkah untuk menjalankan aplikasi:

### Instalasi Pustaka yang Diperlukan:
1. Buka terminal atau command prompt.
2. Jalankan perintah berikut untuk menginstal pustaka yang diperlukan:

### Menjalankan Aplikasi:
Navigasikan ke direktori tempat file aplikasi disimpan.

Jalankan aplikasi dengan perintah berikut:

Untuk Enkripsi dan Dekripsi DES:
bash
Salin kode
python desgui.py
Untuk Kalkulator Caesar Cipher:
bash
Salin kode
python kalkulator_caesar.py
Untuk Steganografi:
bash
Salin kode
python steganogui.py
Dengan mengikuti langkah-langkah di atas, Anda dapat menjalankan dan menggunakan aplikasi-aplikasi yang telah dibuat.

```bash
pip install tkinter pycryptodome pillow stegano

