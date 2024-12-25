import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import DES
import base64

# Fungsi padding
def pad(teks):
    while len(teks) % 8 != 0:
        teks += ' '
    return teks

# Fungsi enkripsi
def encrypt(teks_plain, key):
    des = DES.new(key, DES.MODE_ECB)
    teks_terpad = pad(teks_plain)
    teks_enkripsi = des.encrypt(teks_terpad.encode('utf-8'))
    return base64.b64encode(teks_enkripsi).decode('utf-8')

# Fungsi dekripsi
def decrypt(teks_enkripsi, key):
    des = DES.new(key, DES.MODE_ECB)
    teks_terdekripsi = base64.b64decode(teks_enkripsi)
    teks_dekripsi = des.decrypt(teks_terdekripsi).decode('utf-8')
    return teks_dekripsi.rstrip()

# Fungsi untuk enkripsi dan dekripsi pada GUI
def enkripsi():
    teks_plain = entry_teks_plain.get()
    key_input = entry_kunci.get()
    
    if len(key_input) != 8:
        messagebox.showerror("Error", "Kunci harus terdiri dari 8 karakter.")
        return

    key = key_input.encode('utf-8')
    teks_enkripsi = encrypt(teks_plain, key)
    entry_teks_enkripsi.delete(0, tk.END)
    entry_teks_enkripsi.insert(tk.END, teks_enkripsi)

def dekripsi():
    teks_enkripsi = entry_teks_enkripsi.get()
    key_input = entry_kunci.get()
    
    if len(key_input) != 8:
        messagebox.showerror("Error", "Kunci harus terdiri dari 8 karakter.")
        return

    key = key_input.encode('utf-8')
    teks_dekripsi = decrypt(teks_enkripsi, key)
    entry_teks_dekripsi.delete(0, tk.END)
    entry_teks_dekripsi.insert(tk.END, teks_dekripsi)

# Fungsi untuk menutup aplikasi
def close_app():
    root.quit()

# Membuat jendela GUI
root = tk.Tk()
root.title("Enkripsi dan Dekripsi DES")

# Mengatur fullscreen
root.attributes("-fullscreen", True)

# Membuat gradien warna menggunakan Canvas
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack(fill="both", expand=True)

# Menambahkan gradien yang lebih lembut
for i in range(256):
    color = f"#{255-i:02x}{255-i:02x}{200:02x}"
    canvas.create_rectangle(0, i * 3, root.winfo_screenwidth(), (i+1) * 3, fill=color, outline=color)

# Frame untuk elemen GUI
frame = tk.Frame(canvas, bg="#f5f5f5", bd=10, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor="center", width=700, height=550)

# Label judul
judul = tk.Label(frame, text="DES Encryption & Decryption", font=("Helvetica", 20, "bold"), bg="#f5f5f5", fg="#333")
judul.pack(pady=10)

# Entry dan Label
label_teks_plain = tk.Label(frame, text="Teks Plain:", font=("Helvetica", 14), bg="#f5f5f5")
label_teks_plain.pack(anchor="w", padx=10, pady=5)
entry_teks_plain = tk.Entry(frame, font=("Helvetica", 14), width=50)
entry_teks_plain.pack(pady=5)

label_kunci = tk.Label(frame, text="Kunci (8 karakter):", font=("Helvetica", 14), bg="#f5f5f5")
label_kunci.pack(anchor="w", padx=10, pady=5)
entry_kunci = tk.Entry(frame, font=("Helvetica", 14), width=50, show="*")
entry_kunci.pack(pady=5)

# Tombol Enkripsi
button_enkripsi = tk.Button(frame, text="Enkripsi", command=enkripsi, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
button_enkripsi.pack(pady=10)

label_teks_enkripsi = tk.Label(frame, text="Teks Enkripsi:", font=("Helvetica", 14), bg="#f5f5f5")
label_teks_enkripsi.pack(anchor="w", padx=10, pady=5)
entry_teks_enkripsi = tk.Entry(frame, font=("Helvetica", 14), width=50)
entry_teks_enkripsi.pack(pady=5)

# Tombol Dekripsi
button_dekripsi = tk.Button(frame, text="Dekripsi", command=dekripsi, bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"))
button_dekripsi.pack(pady=10)

label_teks_dekripsi = tk.Label(frame, text="Teks Dekripsi:", font=("Helvetica", 14), bg="#f5f5f5")
label_teks_dekripsi.pack(anchor="w", padx=10, pady=5)
entry_teks_dekripsi = tk.Entry(frame, font=("Helvetica", 14), width=50)
entry_teks_dekripsi.pack(pady=5)

# Tombol Close
button_close = tk.Button(frame, text="Close", command=close_app, bg="red", fg="white", font=("Helvetica", 12, "bold"))
button_close.pack(pady=20)

# Menjalankan loop utama GUI
root.mainloop()
