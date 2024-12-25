from stegano import lsb
import os
from tkinter import Tk, Label, Button, filedialog, Text, messagebox, Toplevel
from PIL import Image

# Warna Palet
BACKGROUND_COLOR = "#1e1e2e"  # Hitam kebiruan
TEXT_COLOR = "#ffffff"  # Putih
BUTTON_COLOR = "#44475a"  # Abu-abu gelap
HIGHLIGHT_COLOR = "#bd93f9"  # Ungu terang

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganografi Tool")
        self.root.geometry("800x600")
        self.root.configure(bg=BACKGROUND_COLOR)
        self.root.state("zoomed")  # Fullscreen

        # Judul
        self.title_label = Label(
            root, text="Steganografi Tool", font=("Helvetica", 24, "bold"), 
            fg=HIGHLIGHT_COLOR, bg=BACKGROUND_COLOR
        )
        self.title_label.pack(pady=30)

        # Tombol Sembunyikan Pesan
        self.hide_button = Button(
            root, text="Sembunyikan Pesan", command=self.hide_message_gui, 
            bg=BUTTON_COLOR, fg=TEXT_COLOR, font=("Helvetica", 16), relief="raised", width=20
        )
        self.hide_button.pack(pady=20)

        # Tombol Tampilkan Pesan
        self.show_button = Button(
            root, text="Tampilkan Pesan", command=self.show_message_gui, 
            bg=BUTTON_COLOR, fg=TEXT_COLOR, font=("Helvetica", 16), relief="raised", width=20
        )
        self.show_button.pack(pady=20)

        # Tombol Keluar
        self.exit_button = Button(
            root, text="Close", command=self.confirm_exit, 
            bg=BUTTON_COLOR, fg=TEXT_COLOR, font=("Helvetica", 16), relief="raised", width=20
        )
        self.exit_button.pack(pady=20)

    def get_image_path(self):
        return filedialog.askopenfilename(filetypes=[("Image Files", ".png;.jpg")])

    def convert_to_png(self, img_path):
        if img_path.endswith('.jpg'):
            img = Image.open(img_path)
            png_path = img_path.rsplit('.', 1)[0] + ".png"
            img.save(png_path)
            return png_path
        return img_path

    def save_image_path(self):
        return filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Image Files", "*.png")])

    def hide_message_gui(self):
        img_path = self.get_image_path()
        if not img_path or not os.path.exists(img_path):
            messagebox.showerror("Error", "Path gambar tidak valid.")
            return

        img_path = self.convert_to_png(img_path)
        if not img_path.endswith('.png'):
            messagebox.showerror("Error", "Format file tidak didukung.")
            return

        # Input pesan
        input_window = Toplevel(self.root)
        input_window.title("Masukkan Pesan")
        input_window.configure(bg=BACKGROUND_COLOR)
        input_window.geometry("500x300")

        Label(
            input_window, text="Masukkan Pesan:", 
            bg=BACKGROUND_COLOR, fg=TEXT_COLOR, font=("Helvetica", 14)
        ).pack(pady=10)

        message_entry = Text(
            input_window, height=5, width=40, bg=BUTTON_COLOR, fg=TEXT_COLOR, font=("Helvetica", 12)
        )
        message_entry.pack(pady=10)

        def submit_message():
            message = message_entry.get("1.0", "end").strip()
            input_window.destroy()
            save_path = self.save_image_path()
            if not save_path:
                return
            try:
                secret = lsb.hide(img_path, message)
                secret.save(save_path)
                messagebox.showinfo("Success", f"Pesan berhasil disembunyikan dalam gambar. Gambar disimpan di: {save_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal menyembunyikan pesan: {e}")

        Button(
            input_window, text="Simpan", command=submit_message, 
            bg=BUTTON_COLOR, fg=TEXT_COLOR, font=("Helvetica", 14), relief="raised"
        ).pack(pady=10)

    def show_message_gui(self):
        img_path = self.get_image_path()
        if not img_path or not os.path.exists(img_path):
            messagebox.showerror("Error", "Path gambar tidak valid.")
            return

        img_path = self.convert_to_png(img_path)
        try:
            clear_message = lsb.reveal(img_path)
            if clear_message:
                messagebox.showinfo("Pesan Tersembunyi", f"Pesan: {clear_message}")
            else:
                messagebox.showinfo("Info", "Tidak ada pesan tersembunyi dalam gambar ini.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menampilkan pesan: {e}")

    def confirm_exit(self):
        result = messagebox.askyesno("Confirm Exit", "Apakah Anda yakin ingin keluar?")
        if result:
            self.root.quit()

# Main Program
if __name__ == "__main__":
    root = Tk()
    app = SteganographyApp(root)
    root.mainloop()
