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

## 📚 Documentation

Additional setup guides and documentation available in the [`docs/`](docs/) folder:

- **[WSL2 Setup Guide](docs/WSL2_SETUP_GUIDE.md)** - Setup development environment on WSL2
- **[Sync Guide](docs/SYNC_GUIDE.md)** - Git auto-sync configuration
- **[Claude Desktop Proxy Setup](docs/CLAUDE_DESKTOP_PROXY_SETUP.md)** - SSH tunnel setup for Claude Desktop

---

## 🚀 Getting Started

1. Clone this repository:
```bash
git clone git@github.com:triapoets/Python-Media-Utilities.git
cd Python-Media-Utilities
```

2. Install dependencies (if needed):
```bash
# For moviepy version
pip install moviepy

# For ffmpeg version (recommended)
apt install ffmpeg  # Linux
# or
brew install ffmpeg  # macOS
```

3. Run the tools as described in each section above.

---

## 📝 License

Free to use and modify.

---

**Repository:** https://github.com/triapoets/Python-Media-Utilities
