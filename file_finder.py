#!/usr/bin/env python3
"""
Program sederhana untuk mencari file berdasarkan extension dalam folder
"""

import os
import sys
from pathlib import Path


def find_files_by_extension(folder_path, extension):
    """
    Mencari semua file dengan extension tertentu dalam folder

    Args:
        folder_path: Path ke folder yang akan dicari
        extension: Extension file yang dicari (contoh: 'txt', '.txt', 'pdf')

    Returns:
        List of file paths yang ditemukan
    """
    # Pastikan extension dimulai dengan titik
    if not extension.startswith('.'):
        extension = '.' + extension

    # Validasi folder
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' tidak ditemukan!")
        return []

    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' bukan sebuah folder!")
        return []

    # Cari file
    found_files = []
    print(f"\nMencari file dengan extension '{extension}' di: {folder_path}\n")

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(extension):
                full_path = os.path.join(root, file)
                found_files.append(full_path)
                print(f"✓ {full_path}")

    return found_files


def main():
    """Main function"""
    print("=" * 60)
    print("FILE FINDER - Pencari File Berdasarkan Extension")
    print("=" * 60)

    # Input dari user
    if len(sys.argv) == 3:
        # Jika dijalankan dengan argument
        folder_path = sys.argv[1]
        extension = sys.argv[2]
    else:
        # Interactive mode
        folder_path = input("\nMasukkan path folder: ").strip()
        extension = input("Masukkan extension file (contoh: txt, pdf, py): ").strip()

    # Cari file
    found_files = find_files_by_extension(folder_path, extension)

    # Tampilkan hasil
    print("\n" + "=" * 60)
    if found_files:
        print(f"Ditemukan {len(found_files)} file dengan extension '{extension}'")
    else:
        print(f"Tidak ada file dengan extension '{extension}' yang ditemukan")
    print("=" * 60)


if __name__ == "__main__":
    main()
