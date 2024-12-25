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

### tampilan des gui
![2024-12-25 (3)](https://github.com/user-attachments/assets/35aee8cc-c32d-4101-abb9-392ab68cc7e9)


---

## 2. Aplikasi Kalkulator Caesar Cipher

### Deskripsi:
Aplikasi ini menerapkan metode Caesar Cipher untuk enkripsi dan dekripsi teks dengan pergeseran karakter. Pengguna dapat memasukkan teks dan nilai pergeseran untuk melakukan proses tersebut.

### Cara Menjalankan:
1. Jalankan file `kalkulator_caesar.py`.
2. Masukkan teks dan nilai pergeseran (antara 1 dan 25).
3. Klik tombol "Enkripsi" untuk mendapatkan hasil enkripsi, dan "Dekripsi" untuk mendapatkan teks asli.

### tampilan caesar chiper gui
![2024-12-25 (7)](https://github.com/user-attachments/assets/a67e0c6d-9440-42ce-8e70-9e68009eb70d)


---

## 3. Aplikasi Steganografi

### Deskripsi:
Aplikasi ini memungkinkan pengguna untuk menyembunyikan pesan dalam gambar menggunakan teknik steganografi. Pengguna dapat menyembunyikan pesan dalam gambar PNG atau JPG dan mengekstrak pesan dari gambar tersebut.

### Cara Menjalankan:
1. Jalankan file `steganogui.py`.
2. Pilih gambar untuk menyembunyikan pesan atau untuk mengekstrak pesan.
3. Ikuti instruksi di GUI untuk menyembunyikan atau menampilkan pesan.

### tampilan stegano gui

![2024-12-25 (10)](https://github.com/user-attachments/assets/d2c4bb03-eb06-491e-9679-a0740bbeeda1)
![2024-12-25 (11)](https://github.com/user-attachments/assets/9bdb5fb8-be6c-457a-9b38-7b35141f7897)
![2024-12-25 (9)](https://github.com/user-attachments/assets/e95a264e-bfd7-42fe-817e-04f2f359510e)

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

