#!/usr/bin/env python3
"""
Program untuk convert file MP4 ke MP3
Versi menggunakan ffmpeg-python atau subprocess
"""

import os
import sys
import subprocess
from pathlib import Path


def check_ffmpeg():
    """Cek apakah ffmpeg terinstall"""
    try:
        subprocess.run(['ffmpeg', '-version'],
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE,
                      check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def convert_mp4_to_mp3(input_file, output_file=None, bitrate="192k"):
    """
    Convert file MP4 ke MP3 menggunakan ffmpeg

    Args:
        input_file: Path ke file MP4 input
        output_file: Path ke file MP3 output (optional)
        bitrate: Bitrate audio (default: 192k)

    Returns:
        True jika berhasil, False jika gagal
    """
    # Cek ffmpeg
    if not check_ffmpeg():
        print("❌ Error: ffmpeg tidak ditemukan!")
        print("Install dengan: apt install ffmpeg")
        return False

    # Validasi file input
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' tidak ditemukan!")
        return False

    if not input_file.lower().endswith('.mp4'):
        print(f"Error: File harus berformat .mp4!")
        return False

    # Tentukan output file jika tidak disebutkan
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '.mp3'

    # Pastikan output file berakhiran .mp3
    if not output_file.lower().endswith('.mp3'):
        output_file += '.mp3'

    try:
        print(f"\n{'='*60}")
        print(f"Input  : {input_file}")
        print(f"Output : {output_file}")
        print(f"Bitrate: {bitrate}")
        print(f"{'='*60}\n")

        print("🎵 Mengkonversi MP4 ke MP3...")

        # Command ffmpeg untuk extract audio
        command = [
            'ffmpeg',
            '-i', input_file,           # Input file
            '-vn',                       # Disable video
            '-acodec', 'libmp3lame',    # Audio codec MP3
            '-b:a', bitrate,            # Bitrate
            '-y',                        # Overwrite output
            output_file                  # Output file
        ]

        # Jalankan ffmpeg
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            print(f"❌ Error ffmpeg: {result.stderr}")
            return False

        # Cek ukuran file
        if os.path.exists(output_file):
            input_size = os.path.getsize(input_file) / (1024 * 1024)  # MB
            output_size = os.path.getsize(output_file) / (1024 * 1024)  # MB

            print(f"\n{'='*60}")
            print(f"✅ Konversi berhasil!")
            print(f"   File MP4: {input_size:.2f} MB")
            print(f"   File MP3: {output_size:.2f} MB")
            print(f"   Lokasi  : {output_file}")
            print(f"{'='*60}\n")

            return True
        else:
            print("❌ Error: File output tidak terbuat")
            return False

    except Exception as e:
        print(f"\n❌ Error saat konversi: {str(e)}\n")
        return False


def convert_folder(folder_path, output_folder=None, bitrate="192k"):
    """
    Convert semua file MP4 dalam folder ke MP3

    Args:
        folder_path: Path ke folder yang berisi file MP4
        output_folder: Folder output (default: sama dengan input)
        bitrate: Bitrate audio
    """
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' tidak ditemukan!")
        return

    # Cari semua file MP4
    mp4_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.mp4'):
                mp4_files.append(os.path.join(root, file))

    if not mp4_files:
        print(f"Tidak ada file MP4 ditemukan di '{folder_path}'")
        return

    print(f"\nDitemukan {len(mp4_files)} file MP4\n")

    success_count = 0
    fail_count = 0

    for i, mp4_file in enumerate(mp4_files, 1):
        print(f"\n[{i}/{len(mp4_files)}] Processing: {os.path.basename(mp4_file)}")

        # Tentukan output file
        if output_folder:
            os.makedirs(output_folder, exist_ok=True)
            output_file = os.path.join(
                output_folder,
                os.path.splitext(os.path.basename(mp4_file))[0] + '.mp3'
            )
        else:
            output_file = None

        if convert_mp4_to_mp3(mp4_file, output_file, bitrate):
            success_count += 1
        else:
            fail_count += 1

    print(f"\n{'='*60}")
    print(f"SELESAI")
    print(f"Berhasil: {success_count} file")
    print(f"Gagal   : {fail_count} file")
    print(f"{'='*60}\n")


def main():
    """Main function"""
    print("="*60)
    print("MP4 TO MP3 CONVERTER (FFMPEG VERSION)")
    print("="*60)

    if len(sys.argv) < 2:
        # Interactive mode
        print("\nPilih mode:")
        print("1. Convert satu file")
        print("2. Convert semua file dalam folder")
        choice = input("\nPilihan (1/2): ").strip()

        if choice == "1":
            input_file = input("Masukkan path file MP4: ").strip()
            output_file = input("Output file (kosongkan untuk auto): ").strip()
            bitrate = input("Bitrate (default: 192k): ").strip() or "192k"

            if output_file == "":
                output_file = None

            convert_mp4_to_mp3(input_file, output_file, bitrate)

        elif choice == "2":
            folder_path = input("Masukkan path folder: ").strip()
            output_folder = input("Output folder (kosongkan untuk sama dengan input): ").strip()
            bitrate = input("Bitrate (default: 192k): ").strip() or "192k"

            if output_folder == "":
                output_folder = None

            convert_folder(folder_path, output_folder, bitrate)
        else:
            print("Pilihan tidak valid!")

    else:
        # Command line mode
        input_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
        bitrate = sys.argv[3] if len(sys.argv) > 3 else "192k"

        if os.path.isfile(input_path):
            convert_mp4_to_mp3(input_path, output_path, bitrate)
        elif os.path.isdir(input_path):
            convert_folder(input_path, output_path, bitrate)
        else:
            print(f"Error: '{input_path}' bukan file atau folder yang valid!")


if __name__ == "__main__":
    main()
