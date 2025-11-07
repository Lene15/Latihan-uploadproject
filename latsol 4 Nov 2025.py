import tkinter as tk
from tkinter import ttk

jendela = tk.Tk()
jendela.title('Aplikasi Data Peserta Didik A1')
jendela.geometry("600x400")
jendela.config(bg="#FFFACD")

def simpan_data():
    nama = entry_nama.get()
    kelas = entry_kelas.get()
    alamat = entry_alamat.get()

    if not nama or not kelas or not alamat:
        label_hasil1.config(text="Semua field harus diisi!", fg="red")

    else:
        data_siswa.append((nama, kelas, alamat))
        label_hasil1.config(text="Data berhasil disimpan!", fg="green")
        entry_nama.delete(0, tk.END)
        entry_kelas.delete(0, tk.END)
        entry_alamat.delete(0, tk.END)

def cari_data():
    nama_dicari = entry_cari_nama.get().strip().lower()
    for item in tree_hal3.get_children():
        tree_hal3.delete(item)

    if not nama_dicari:
        tree_hal3.insert("", tk.END, values=("Masukkan nama untuk mencari!", "", ""))
        return

    hasil_ditemukan = False
    for d in data_siswa:
        if nama_dicari in d[0].lower():  # cocok sebagian (misal ketik 'an' akan muncul 'Andi')
            tree_hal3.insert("", tk.END, values=d)
            hasil_ditemukan = True

    if not hasil_ditemukan:
        tree_hal3.insert("", tk.END, values=("Data tidak ditemukan", "", ""))

def tampilan(frame): # fungsi untuk ganti halaman
    frame.tkraise()

data_siswa = []  # tempat menyimpan data


#HALAMAN 1
hal1=tk.Frame(jendela,bg="#FFFACD")
hal1.place(x=0, y=0, relwidth=1, relheight=1)

judul1 = tk.Label(hal1, text="Form Tambah Peserta Didik A1", bg="#FFFACD", font=("Times New Roman", 18))
judul1.pack(pady=10)

label_judul1 = tk.Label(hal1, text="Nama:", bg="#FFFACD", font=("Times New Roman", 12))
label_judul1.pack()
entry_nama = tk.Entry(hal1)
entry_nama.pack()

label_judul2 = tk.Label(hal1, text="Kelas:", bg="#FFFACD", font=("Times New Roman", 12))
label_judul2.pack()
entry_kelas = tk.Entry(hal1)
entry_kelas.pack()

label_judul3 = tk.Label(hal1, text="Alamat:", bg="#FFFACD", font=("Times New Roman", 12))
label_judul3.pack()
entry_alamat = tk.Entry(hal1)
entry_alamat.pack()

label_hasil1=tk.Label(hal1, text='', bg="#FFFACD")
label_hasil1.pack()


#TOMBOL"AN
tombol_simpan = tk.Button(hal1, text="Simpan Data", command=simpan_data, font=("Times New Roman", 12))
tombol_simpan.pack(pady=5)

tombol_lihat = tk.Button(hal1, text="Lihat Data", command=lambda: tampilan(hal2))
tombol_lihat.pack(pady=3)

tombol_cari = tk.Button(hal1, text="Cari Data", command=lambda: tampilan(hal3))
tombol_cari.pack(pady=3)


#HALAMAN 2
hal2=tk.Frame(jendela,bg="#FFFACD")
hal2.place(x=0, y=0, relwidth=1, relheight=1)

judul2 = tk.Label(hal2, text="Daftar Data Peserta Didik A1", bg="#FFFACD", font=("Times New Roman", 18))
judul2.pack(pady=10)

frame_header = tk.Frame(hal2, bg="skyblue")
frame_header.pack(fill="x")

tk.Label(frame_header, text="Nama", width=20, bg="skyblue", font=("Times New Roman", 12, "bold")).grid(row=0, column=0)
tk.Label(frame_header, text="Kelas", width=20, bg="skyblue", font=("Times New Roman", 12, "bold")).grid(row=0, column=1)
tk.Label(frame_header, text="Alamat", width=20, bg="skyblue", font=("Times New Roman", 12, "bold")).grid(row=0, column=2)

# tabel TreeView
kolom = ("Nama", "Kelas", "Alamat")
tabel = ttk.Treeview(hal2, columns=kolom, show="headings")
for kol in kolom:
    tabel.heading(kol, text=kol)
tabel.pack(fill="both", expand=True)

# fungsi tampilkan data
def tampilkan_data():
    for item in tabel.get_children():
        tabel.delete(item)
    for d in data_siswa:
        tabel.insert("", tk.END, values=d)


tombol_tampil = tk.Button(hal2, text="Tampilkan Data", command=tampilkan_data)
tombol_tampil.pack(pady=5)

tombol_kembali1 = tk.Button(hal2, text="Kembali", command=lambda: tampilan(hal1))
tombol_kembali1.pack()


#HALAMAN 3
hal3 = tk.Frame(jendela, bg="#FFFACD") # Memberi warna background seperti contoh gambar (mirip kuning muda/krim)

tk.Label(hal3, text="Cari Data Siswa", font=("Arial", 18, "bold"), bg="#FFFACD").pack(pady=30)

tk.Label(hal3, text="Masukkan Nama:", bg="#FFFACD").pack(pady=(10, 0))
entry_cari_nama=tk.Entry(hal3, width=30, font=("Arial", 12))
entry_cari_nama.pack(pady=5)

# Tombol Cari
tombol_cari=tk.Button(hal3, text="Cari", command=cari_data, font=("Arial", 10, "bold"), 
                   relief=tk.RAISED, borderwidth=2)
tombol_cari.pack(pady=10)

# 2. Setup Treeview di Halaman 3 (Hasil Pencarian)
columns_hal3 = ('nama', 'kelas', 'nilai')
tree_hal3 = ttk.Treeview(hal3, columns=columns_hal3, show='headings', height=10) 

# 3. Define Headings
tree_hal3.heading('nama', text='Nama')
tree_hal3.heading('kelas', text='Kelas')
tree_hal3.heading('nilai', text='Alamat')

# 4. Configure columns (Meniru lebar dan anchor tabel dari hal2)
tree_hal3.column('nama', width=150, anchor='w') 
tree_hal3.column('kelas', width=70, anchor='center')
tree_hal3.column('nilai', width=150, anchor='w') 

# 5. Pack the Treeview (diberi jarak agar layoutnya terlihat rapi seperti contoh)
tree_hal3.pack(padx=10, pady=20, fill='x')

# Tombol Kembali
btn_kembali_hal3=tk.Button(hal3, text="Kembali", command=lambda: tampilan(hal1))
btn_kembali_hal3.pack(pady=20)

# ==================================
# Final Setup
# ==================================
for frame in (hal1, hal2, hal3): 
    frame.place(x=0,y=0,relwidth=1,relheight=1)

tampilan(hal1)

jendela.mainloop()

