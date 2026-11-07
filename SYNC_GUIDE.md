# Python MP4 to MP3 Converter & File Finder

Project tools untuk pencarian file dan konversi MP4 ke MP3.

## Setup Sync antara Linux dan Windows

### 1. Di Linux (sudah setup):
```bash
cd /root/python_projects
git remote add origin git@github.com:triapoets/Mp4-to-Mp3.git
git push -u origin master
```

### 2. Di Windows (clone):
```bash
git clone https://github.com/triapoets/Mp4-to-Mp3.git
cd Mp4-to-Mp3
```

### 3. Workflow sync:
```bash
# Setelah edit di salah satu OS:
git add .
git commit -m "Update files"
git push

# Di OS lain:
git pull
```

## Files dalam project:
- `file_finder.py` - Tool pencarian file
- `mp4_to_mp3_converter.py` - Converter MP4 ke MP3
- `mp4_to_mp3_ffmpeg.py` - Converter menggunakan ffmpeg
- `demo_converter.py` - Demo converter

## Requirements:
```bash
pip install -r requirements.txt
```

## Notes:
- Project ini sudah di-setup dengan Git untuk sync multi-platform
- Gunakan virtual environment untuk dependencies
- File .mp4 dan .mp3 di-ignore untuk menghemat space repo
