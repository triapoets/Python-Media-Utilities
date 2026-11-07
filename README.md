# Python Media Utilities

Collection of Python utilities for media file processing and management.

## 🛠️ Tools

### 1. File Finder (`file_finder.py`)
Program untuk mencari file berdasarkan extension dalam folder.

**Cara Pakai:**
```bash
# Mode interactive
python3 file_finder.py

# Mode command line
python3 file_finder.py /path/folder txt
```

**Fitur:**
- Pencarian recursive (termasuk subfolder)
- Support berbagai extension
- Menampilkan path lengkap file

---

### 2. MP4 to MP3 Converter - MoviePy Version (`mp4_to_mp3_converter.py`)
Convert file MP4 ke MP3 menggunakan library MoviePy.

**Requirements:**
```bash
pip install moviepy
```

**Cara Pakai:**
```bash
# Single file
python3 mp4_to_mp3_converter.py video.mp4

# Dengan custom output
python3 mp4_to_mp3_converter.py video.mp4 output.mp3 320k
```

---

### 3. MP4 to MP3 Converter - FFmpeg Version (`mp4_to_mp3_ffmpeg.py`) ⭐ RECOMMENDED
Convert file MP4 ke MP3 menggunakan FFmpeg.

**Requirements:**
```bash
apt install ffmpeg
```

**Cara Pakai:**
```bash
# Single file
python3 mp4_to_mp3_ffmpeg.py video.mp4

# Batch convert folder
python3 mp4_to_mp3_ffmpeg.py /path/to/videos/

# Custom bitrate
python3 mp4_to_mp3_ffmpeg.py video.mp4 output.mp3 320k
```

**Pilihan Bitrate:**
- `128k` - Kualitas standar
- `192k` - Kualitas baik (default)
- `256k` - Kualitas tinggi
- `320k` - Kualitas maksimal

---

### 4. Demo Converter (`demo_converter.py`)
Program demo untuk testing converter tanpa perlu dependency.

**Cara Pakai:**
```bash
python3 demo_converter.py
```

**Fitur:**
- Tidak perlu install library tambahan
- Membuat file dummy untuk testing
- Menunjukkan alur kerja program

---

## 📥 Download via FileZilla

**Server Info:**
- **IP Address:** 192.168.1.86
- **Protocol:** SFTP
- **Port:** 22
- **Username:** root
- **Path:** `/root/python_projects/`

**Langkah:**
1. Buka FileZilla
2. Connect ke server (Host: 192.168.1.86, Port: 22)
3. Navigate ke `/root/python_projects/`
4. Download file yang diinginkan

---

## 📝 Notes

- Semua program sudah ditest dan berfungsi dengan baik
- File asli tetap ada di `/root/` (ini adalah copy)
- Untuk penggunaan production, gunakan versi FFmpeg untuk converter

---

**Created:** 2026-11-06
**Location:** /root/python_projects/
# Test auto-sync
