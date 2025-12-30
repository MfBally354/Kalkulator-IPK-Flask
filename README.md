# 🎓 Kalkulator IPK

<div align="center">

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1de7d4a9-a732-449e-8e0b-c7594e50792b" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1afc8806-4037-4f32-9ef1-527190f8b3a6" />


**Aplikasi web sederhana untuk menghitung Indeks Prestasi Kumulatif (IPK) dengan fitur penyimpanan riwayat perhitungan**

[Demo](#demo) • [Fitur](#fitur) • [Instalasi](#instalasi) • [Penggunaan](#penggunaan) • [Struktur Project](#struktur-project)

</div>

---

## 📸 Demo

<div align="center">
  <img src="https://via.placeholder.com/800x400/667eea/ffffff?text=Kalkulator+IPK+Screenshot" alt="Screenshot Aplikasi" width="80%">
</div>

> **Catatan:** Ganti placeholder di atas dengan screenshot aplikasi Anda yang sebenarnya

---

## ✨ Fitur

- 🧮 **Perhitungan IPK Akurat** - Sistem konversi nilai lengkap (A sampai E)
- 📊 **Multi Mata Kuliah** - Tambah atau hapus mata kuliah secara dinamis
- 💾 **Penyimpanan Otomatis** - Semua perhitungan tersimpan dalam file JSON
- 📜 **Riwayat Lengkap** - Lihat detail semua perhitungan sebelumnya
- 🎨 **UI Modern** - Desain responsif dan user-friendly
- 🚀 **Ringan & Cepat** - Dibangun dengan Flask yang efisien
- 📱 **Responsive Design** - Tampil sempurna di desktop, tablet, dan mobile

---

## 🛠️ Tech Stack

- **Backend:** Python 3.8+, Flask 3.0.0
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Storage:** JSON File System
- **Styling:** Custom CSS dengan gradient modern

---

## 📋 Prerequisites

Pastikan sistem Anda sudah terinstall:

- Python 3.8 atau lebih tinggi
- pip (Python package manager)
- Virtual environment (opsional tapi direkomendasikan)

---

## 🚀 Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/username/kalkulator-ipk.git
cd kalkulator-ipk
```

### 2. Buat Virtual Environment

```bash
# Linux/MacOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi

```bash
python app.py
```

Aplikasi akan berjalan di `http://localhost:5000`

---

## 💻 Penggunaan

### Menghitung IPK

1. Buka aplikasi di browser
2. Klik tombol **"+ Tambah Mata Kuliah"** untuk menambah mata kuliah
3. Isi data:
   - **Nama Mata Kuliah** (contoh: Matematika Diskrit)
   - **SKS** (1-6)
   - **Nilai** (A, A-, B+, B, B-, C+, C, D, E)
4. Klik **"Hitung IPK"**
5. Hasil akan muncul beserta predikat kelulusan

### Melihat Riwayat

1. Klik tab **"Riwayat"** di navigasi
2. Lihat semua perhitungan yang pernah dilakukan
3. Detail mencakup timestamp, daftar mata kuliah, dan IPK

### Menghapus Riwayat

- Klik tombol **"Hapus Semua"** di halaman Riwayat
- Konfirmasi penghapusan

---

## 📁 Struktur Project

```
kalkulator-ipk/
│
├── app.py                      # File utama Flask aplikasi
├── requirements.txt            # Dependencies Python
├── ipk_data.json              # File penyimpanan data (auto-generated)
├── README.md                  # Dokumentasi project
│
├── static/                    # Folder asset statis
│   ├── css/
│   │   └── style.css         # File styling
│   └── js/
│       └── script.js         # JavaScript (opsional)
│
└── templates/                 # Folder template HTML
    ├── index.html            # Halaman kalkulator
    └── history.html          # Halaman riwayat
```

---

## 🎯 Sistem Konversi Nilai

| Huruf | Angka | Keterangan |
|-------|-------|------------|
| A     | 4.0   | Istimewa   |
| A-    | 3.7   | Sangat Baik|
| B+    | 3.3   | Baik Sekali|
| B     | 3.0   | Baik       |
| B-    | 2.7   | Cukup Baik |
| C+    | 2.3   | Lebih Cukup|
| C     | 2.0   | Cukup      |
| D     | 1.0   | Kurang     |
| E     | 0.0   | Gagal      |

---

## 📊 Predikat Kelulusan

- **IPK ≥ 3.5** → Cumlaude 🌟
- **IPK ≥ 3.0** → Sangat Memuaskan 👏
- **IPK ≥ 2.5** → Memuaskan 👍
- **IPK < 2.5** → Perlu Ditingkatkan 💪

---

## 🔧 Konfigurasi

### Mengubah Port

Edit file `app.py`:

```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)  # Ganti port di sini
```

### Mengubah File Storage

Edit konstanta di `app.py`:

```python
DATA_FILE = 'data_ipk_saya.json'  # Nama file custom
```

---

## 🐛 Troubleshooting

### Error: Module not found

```bash
# Pastikan virtual environment aktif
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install ulang dependencies
pip install -r requirements.txt
```

### Port sudah digunakan

```bash
# Linux/Mac: Kill process di port 5000
lsof -ti:5000 | xargs kill -9

# Windows: Ganti port di app.py
```

### Data tidak tersimpan

- Pastikan aplikasi memiliki permission write di direktori project
- Check apakah file `ipk_data.json` ter-generate

---

## 🤝 Kontribusi

Kontribusi sangat diterima! Berikut cara berkontribusi:

1. Fork repository ini
2. Buat branch fitur baru (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -m 'Menambah fitur X'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

---

## 📝 To-Do List

- [ ] Tambah export ke PDF
- [ ] Implementasi database (SQLite/PostgreSQL)
- [ ] Fitur grafik visualisasi IPK per semester
- [ ] Authentication & multi-user support
- [ ] Dark mode toggle
- [ ] API documentation dengan Swagger

---

## 📄 License

Project ini dilisensikan di bawah [MIT License](LICENSE).

---

## 👨‍💻 Author

**Nama Anda**

- GitHub: [@username](https://github.com/MfBally354)
- Email: iqbalguntur313@gmail.com

---

## 🙏 Acknowledgments

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Official Docs](https://docs.python.org/)

---

<div align="center">

**⭐ Jika project ini bermanfaat, jangan lupa kasih star! ⭐**

Made with ❤️ using Flask

</div>
