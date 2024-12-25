import tkinter as tk
from tkinter import messagebox

# Fungsi enkripsi Caesar Cipher
def enkripsi(plain_text, shift):
    chipert_text = ""
    for char in plain_text:
        if char.isupper():
            chipert_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            chipert_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            chipert_text += char
    return chipert_text

# Fungsi dekripsi Caesar Cipher
def dekripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isupper():
            plain_text += chr(((ord(char) - shift - 65) % 26) + 65)
        elif char.islower():
            plain_text += chr(((ord(char) - shift - 97) % 26) + 97)
        else:
            plain_text += char
    return plain_text

# Fungsi untuk tombol Enkripsi
def proses_enkripsi():
    plain_text = entry_text.get()
    try:
        shift = int(entry_shift.get())
        if 1 <= shift <= 25:
            result = enkripsi(plain_text, shift)
            entry_result.delete(0, tk.END)
            entry_result.insert(0, result)
        else:
            messagebox.showwarning("Peringatan", "Nilai pergeseran harus antara 1 dan 25.")
    except ValueError:
        messagebox.showwarning("Peringatan", "Nilai pergeseran harus berupa angka.")

# Fungsi untuk tombol Dekripsi
def proses_dekripsi():
    cipher_text = entry_text.get()
    try:
        shift = int(entry_shift.get())
        if 1 <= shift <= 25:
            result = dekripsi(cipher_text, shift)
            entry_result.delete(0, tk.END)
            entry_result.insert(0, result)
        else:
            messagebox.showwarning("Peringatan", "Nilai pergeseran harus antara 1 dan 25.")
    except ValueError:
        messagebox.showwarning("Peringatan", "Nilai pergeseran harus berupa angka.")

# Fungsi untuk keluar dari aplikasi
def keluar_aplikasi():
    root.destroy()

# Pengaturan jendela utama
root = tk.Tk()
root.title("Caesar Cipher Calculator")
root.configure(bg="#34495e")

# Mengatur full screen
root.attributes('-fullscreen', True)

# Warna dan gaya untuk komponen
label_fg_color = "#ecf0f1"
entry_bg_color = "#ffffff"
entry_fg_color = "#2c3e50"
button_bg_color = "#3498db"
button_fg_color = "#ffffff"
font_label = ("Helvetica", 16, "bold")
font_entry = ("Helvetica", 14)
font_button = ("Helvetica", 14, "bold")

# Frame untuk layout yang rapi
frame_main = tk.Frame(root, bg="#34495e")
frame_main.pack(expand=True, fill='both')

# Mengatur grid agar kolom dan baris mengisi ruang
frame_main.grid_columnconfigure(0, weight=1)
frame_main.grid_columnconfigure(1, weight=2)
frame_main.grid_rowconfigure(0, weight=1)
frame_main.grid_rowconfigure(1, weight=1)
frame_main.grid_rowconfigure(2, weight=1)
frame_main.grid_rowconfigure(3, weight=1)

# Label dan Entry untuk teks input
label_text = tk.Label(frame_main, text="Masukkan Teks:", fg=label_fg_color, bg="#34495e", font=font_label)
label_text.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

entry_text = tk.Entry(frame_main, width=50, bg=entry_bg_color, fg=entry_fg_color, font=font_entry, relief="flat")
entry_text.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

# Label dan Entry untuk pergeseran
label_shift = tk.Label(frame_main, text="Pergeseran:", fg=label_fg_color, bg="#34495e", font=font_label)
label_shift.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

entry_shift = tk.Entry(frame_main, width=10, bg=entry_bg_color, fg=entry_fg_color, font=font_entry, relief="flat")
entry_shift.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

# Tombol Enkripsi
button_encrypt = tk.Button(frame_main, text="Enkripsi", command=proses_enkripsi, bg=button_bg_color, fg=button_fg_color, font=font_button)
button_encrypt.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

# Tombol Dekripsi
button_decrypt = tk.Button(frame_main, text="Dekripsi", command=proses_dekripsi, bg=button_bg_color, fg=button_fg_color, font=font_button)
button_decrypt.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

# Tombol Keluar
button_exit = tk.Button(frame_main, text="Keluar", command=keluar_aplikasi, bg=button_bg_color, fg=button_fg_color, font=font_button)
button_exit.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

# Label dan Entry untuk hasil
label_result = tk.Label(frame_main, text="Hasil:", fg=label_fg_color, bg="#34495e", font=font_label)
label_result.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

entry_result = tk.Entry(frame_main, width=50, bg=entry_bg_color, fg=entry_fg_color, font=font_entry, relief="flat")
entry_result.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

# Menjalankan aplikasi
root.mainloop()