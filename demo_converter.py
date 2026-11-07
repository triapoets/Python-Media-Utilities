#!/usr/bin/env python3
"""
DEMO PROGRAM MP4 TO MP3 CONVERTER
Simulasi tanpa perlu ffmpeg/moviepy untuk demo
"""

import os
import sys
import time
from pathlib import Path


def simulate_conversion(input_file, output_file=None, bitrate="192k"):
    """
    Simulasi konversi MP4 ke MP3 (untuk demo)
    """
    # Validasi file input
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' tidak ditemukan!")
        return False

    # Tentukan output file
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '.mp3'

    if not output_file.lower().endswith('.mp3'):
        output_file += '.mp3'

    print(f"\n{'='*60}")
    print(f"Input  : {input_file}")
    print(f"Output : {output_file}")
    print(f"Bitrate: {bitrate}")
    print(f"{'='*60}\n")

    print("🎬 Memuat video...")
    time.sleep(0.5)

    print("🎵 Mengekstrak audio...")
    time.sleep(0.5)

    print("💾 Menyimpan file MP3...")
    time.sleep(0.5)

    # Buat file MP3 dummy
    with open(output_file, 'w') as f:
        f.write(f"[DEMO MP3 FILE]\n")
        f.write(f"Original: {input_file}\n")
        f.write(f"Bitrate: {bitrate}\n")
        f.write(f"This is a demo file\n")

    # Simulasi ukuran file
    input_size = os.path.getsize(input_file) / 1024  # KB
    output_size = os.path.getsize(output_file) / 1024  # KB

    print(f"\n{'='*60}")
    print(f"✅ Konversi berhasil! (DEMO MODE)")
    print(f"   File MP4: {input_size:.2f} KB")
    print(f"   File MP3: {output_size:.2f} KB")
    print(f"   Lokasi  : {output_file}")
    print(f"{'='*60}\n")

    return True


def main():
    print("="*60)
    print("MP4 TO MP3 CONVERTER - DEMO VERSION")
    print("="*60)
    print("NOTE: Ini adalah versi DEMO untuk menunjukkan cara kerja")
    print("File MP3 yang dihasilkan adalah file dummy untuk testing")
    print("="*60)

    # Buat folder demo
    demo_folder = "/root/demo_videos"
    os.makedirs(demo_folder, exist_ok=True)

    # Buat beberapa file MP4 dummy
    print("\n📁 Membuat file MP4 demo...")
    demo_files = [
        "video1.mp4",
        "video2.mp4",
        "tutorial.mp4"
    ]

    for filename in demo_files:
        filepath = os.path.join(demo_folder, filename)
        with open(filepath, 'w') as f:
            f.write(f"[DEMO MP4 FILE: {filename}]\n")
            f.write(f"This is a demo video file\n")
            f.write(f"Duration: 3:45\n")
            f.write(f"Resolution: 1920x1080\n")
        print(f"   ✓ Created: {filename}")

    print(f"\n📂 File demo tersimpan di: {demo_folder}\n")

    # Demo 1: Convert single file
    print("\n" + "="*60)
    print("DEMO 1: Convert Single File")
    print("="*60)
    input("\nTekan Enter untuk melanjutkan...")

    test_file = os.path.join(demo_folder, "video1.mp4")
    simulate_conversion(test_file, bitrate="192k")

    # Demo 2: Convert dengan custom output
    print("\n" + "="*60)
    print("DEMO 2: Convert dengan Custom Output Name")
    print("="*60)
    input("\nTekan Enter untuk melanjutkan...")

    test_file2 = os.path.join(demo_folder, "video2.mp4")
    custom_output = os.path.join(demo_folder, "my_audio.mp3")
    simulate_conversion(test_file2, custom_output, bitrate="320k")

    # Demo 3: Batch convert
    print("\n" + "="*60)
    print("DEMO 3: Batch Convert Multiple Files")
    print("="*60)
    input("\nTekan Enter untuk melanjutkan...")

    mp4_files = [f for f in os.listdir(demo_folder) if f.endswith('.mp4')]
    print(f"\nDitemukan {len(mp4_files)} file MP4:")
    for f in mp4_files:
        print(f"   - {f}")

    print("\nMemulai batch conversion...\n")
    time.sleep(1)

    success = 0
    for i, filename in enumerate(mp4_files, 1):
        print(f"[{i}/{len(mp4_files)}] Processing: {filename}")
        filepath = os.path.join(demo_folder, filename)
        if simulate_conversion(filepath):
            success += 1

    print(f"\n{'='*60}")
    print(f"BATCH CONVERSION SELESAI")
    print(f"Berhasil: {success}/{len(mp4_files)} file")
    print(f"{'='*60}\n")

    # Tampilkan hasil akhir
    print("\n📂 Isi folder demo_videos:")
    print("="*60)
    for item in sorted(os.listdir(demo_folder)):
        filepath = os.path.join(demo_folder, item)
        size = os.path.getsize(filepath) / 1024
        ext = os.path.splitext(item)[1]
        icon = "🎬" if ext == ".mp4" else "🎵"
        print(f"{icon} {item:30} ({size:.2f} KB)")
    print("="*60)

    print("\n✅ Demo selesai!")
    print(f"📁 Semua file ada di: {demo_folder}")
    print("\n💡 Untuk konversi real:")
    print("   1. Install ffmpeg: apt install ffmpeg")
    print("   2. Gunakan: python3 mp4_to_mp3_ffmpeg.py")


if __name__ == "__main__":
    main()
