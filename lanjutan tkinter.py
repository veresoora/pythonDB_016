import sqlite3
import tkinter as tk

# Fungsi untuk menentukan prediksi Fakultas berdasarkan nilai tertinggi
def hitung_prediksi():
    # Mengambil nilai dari entry
    nama = entry_nama.get()
    biologi = float(entry_biologi.get())
    fisika = float(entry_fisika.get())
    inggris = float(entry_inggris.get())

    # Untuk menentukan Fakultas berdasarkan nilai tertinggi
    fakultas = ""
    if biologi > fisika and biologi > inggris:
        fakultas = "Kedokteran"
    elif fisika > biologi and fisika > inggris:
        fakultas = "Teknik"
    elif inggris > biologi and inggris > fisika:
        fakultas = "Bahasa"
    else:
        return "Tidak dapat diprediksi"

    # Menampilkan hasil prediksi Fakultas
    label_hasil.config(text=f"Hasil Prediksi untuk {nama} adalah {fakultas}")

    # Simpan data ke database SQLite
    conn = sqlite3.connect('appdb.db')
    cursor = conn.cursor()

    # Membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nama_siswa TEXT,
                        biologi REAL,
                        fisika REAL,
                        inggris REAL,
                        prediksi_fakultas TEXT
                    )''')

    # Menyimpan nilai siswa ke dalam database
    cursor.execute('''INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
                      VALUES (?, ?, ?, ?, ?)''', (nama, biologi, fisika, inggris, fakultas))
    
    conn.commit()
    conn.close()

# Membuat GUI
root = tk.Tk()
root.configure(background='pink')
root.geometry("400x500")
root.resizable(False,False)

root.title("Aplikasi Prediksi Prodi Pilihan")

label_judul = tk.Label(root, text="Aplikasi prediksi Prodi Pilihan")
label_judul.pack(padx=10, pady=0, fill="x", expand=True)

label_nama = tk.Label(root, text="Nama Siswa:")
label_nama.pack(padx=10, pady=5, fill="x", expand=True)
entry_nama = tk.Entry(root)
entry_nama.pack()

label_biologi = tk.Label(root, text="Nilai Biologi:")
label_biologi.pack(padx=10, pady=5, fill="x", expand=True)
entry_biologi = tk.Entry(root)
entry_biologi.pack()

label_fisika = tk.Label(root, text="Nilai Fisika:")
label_fisika.pack(padx=10, pady=5, fill="x", expand=True)
entry_fisika = tk.Entry(root)
entry_fisika.pack()

label_inggris = tk.Label(root, text="Nilai Inggris:")
label_inggris.pack(padx=10, pady=5, fill="x", expand=True)
entry_inggris = tk.Entry(root)
entry_inggris.pack()

button_prediksi = tk.Button(root, text="Hasil Prediksi", command=hitung_prediksi)
button_prediksi.pack()

label_hasil = tk.Label(root, text="")
label_hasil.pack()

root.mainloop()