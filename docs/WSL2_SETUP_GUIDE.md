# WSL2 Installation & Setup Guide

## Langkah 1: Install WSL2

### Cara Tercepat (Windows 10 version 2004+ atau Windows 11):
Buka **PowerShell sebagai Administrator**, lalu jalankan:

```powershell
wsl --install
```

Perintah ini akan:
- Enable WSL feature
- Install Virtual Machine Platform
- Download dan install Ubuntu (default distro)
- Set WSL2 sebagai default

**Restart komputer** setelah selesai.

---

### Cara Manual (jika command di atas gagal):

#### Step 1: Enable WSL
```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

#### Step 2: Enable Virtual Machine Platform
```powershell
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

#### Step 3: Restart komputer

#### Step 4: Download WSL2 Kernel Update
Download dari: https://aka.ms/wsl2kernel
Install file `.msi` yang sudah di-download

#### Step 5: Set WSL2 sebagai default
```powershell
wsl --set-default-version 2
```

#### Step 6: Install Linux Distro
Buka **Microsoft Store**, cari dan install:
- **Ubuntu** (recommended untuk pemula)
- Ubuntu 22.04 LTS
- Debian
- Kali Linux
- dsb.

---

## Langkah 2: Setup Ubuntu di WSL2

### Pertama Kali Buka Ubuntu:
1. Buka aplikasi "Ubuntu" dari Start Menu
2. Tunggu instalasi selesai (1-2 menit)
3. Buat username dan password (bebas, tidak harus sama dengan Windows)

```bash
# Contoh:
Enter new UNIX username: triapoets
New password: ********
```

### Update System
```bash
sudo apt update && sudo apt upgrade -y
```

### Install Essential Tools
```bash
sudo apt install -y \
  git \
  curl \
  wget \
  vim \
  nano \
  build-essential \
  python3 \
  python3-pip \
  nodejs \
  npm
```

---

## Langkah 3: Install Windows Terminal (Optional tapi Recommended)

### Via PowerShell:
```powershell
winget install Microsoft.WindowsTerminal
```

### Via Microsoft Store:
Cari "Windows Terminal" dan install

### Set Ubuntu sebagai Default:
1. Buka Windows Terminal
2. Settings (Ctrl+,)
3. Startup → Default profile → pilih "Ubuntu"

---

## Langkah 4: Setup Git di WSL2

```bash
# Configure Git
git config --global user.name "triapoets"
git config --global user.email "your-email@example.com"

# Copy SSH key dari Linux server (jika ada)
# Atau generate baru:
ssh-keygen -t ed25519 -C "your-email@example.com"

# Tampilkan public key untuk add ke GitHub
cat ~/.ssh/id_ed25519.pub
```

---

## Langkah 5: Clone Project dari GitHub

```bash
# Buat folder untuk projects
mkdir -p ~/projects
cd ~/projects

# Clone repository
git clone https://github.com/triapoets/Mp4-to-Mp3.git
cd Mp4-to-Mp3

# Install dependencies (jika ada)
pip3 install -r requirements.txt  # untuk Python projects
```

---

## Akses File antara Windows dan WSL2

### Dari WSL2 ke Windows:
```bash
# Windows C:\ ada di /mnt/c/
cd /mnt/c/Users/YourName/Documents
ls -la
```

### Dari Windows ke WSL2:
- Buka File Explorer
- Ketik di address bar: `\\wsl$\Ubuntu\home\triapoets\`
- Atau: `\\wsl$\Ubuntu\home\triapoets\projects\Mp4-to-Mp3\`

**Tips:** Pin folder WSL ke Quick Access untuk akses cepat

---

## Command Berguna WSL2

### PowerShell (Windows):
```powershell
# List semua distro yang terinstall
wsl --list --verbose

# Masuk ke WSL
wsl

# Masuk ke distro tertentu
wsl -d Ubuntu

# Shutdown WSL
wsl --shutdown

# Unregister/hapus distro
wsl --unregister Ubuntu

# Update WSL
wsl --update

# Set distro sebagai default
wsl --set-default Ubuntu

# Export distro (backup)
wsl --export Ubuntu D:\backup\ubuntu.tar

# Import distro (restore)
wsl --import Ubuntu D:\WSL\Ubuntu D:\backup\ubuntu.tar
```

### Bash (WSL):
```bash
# Lihat versi WSL
wsl.exe --version

# Buka Windows Explorer di current directory
explorer.exe .

# Jalankan aplikasi Windows dari WSL
notepad.exe file.txt
code .  # Buka VS Code

# Shutdown WSL dari dalam
wsl.exe --shutdown
```

---

## Setup VS Code dengan WSL2

### Install VS Code Extension:
1. Install VS Code di Windows
2. Install extension: **WSL** (by Microsoft)
3. Di WSL terminal, jalankan:
```bash
code .
```
4. VS Code akan otomatis connect ke WSL

---

## Auto-Sync Setup di WSL2

Setelah clone project, setup auto-sync seperti di Linux:

```bash
cd ~/projects/Mp4-to-Mp3

# Install inotify-tools
sudo apt install -y inotify-tools

# Jalankan auto-sync
nohup ./auto_sync.sh > auto_sync.log 2>&1 &

# Atau tambahkan ke startup (buka setiap kali WSL start)
echo "cd ~/projects/Mp4-to-Mp3 && nohup ./auto_sync.sh > auto_sync.log 2>&1 &" >> ~/.bashrc
```

---

## Tips & Tricks

### 1. Auto-start WSL Service
Buat file `wsl-startup.bat`:
```batch
@echo off
wsl -d Ubuntu -e bash -c "cd ~/projects/Mp4-to-Mp3 && nohup ./auto_sync.sh > auto_sync.log 2>&1 &"
```
Taruh di `shell:startup` (Win+R → ketik `shell:startup`)

### 2. Performance Tips
```bash
# Di WSL, edit /etc/wsl.conf
sudo nano /etc/wsl.conf

# Tambahkan:
[boot]
systemd=true

[network]
generateResolvConf = false
```

### 3. Memory Limit (jika WSL pakai RAM terlalu banyak)
Buat file `.wslconfig` di `C:\Users\YourName\.wslconfig`:
```ini
[wsl2]
memory=4GB
processors=2
swap=2GB
```

---

## Troubleshooting

### WSL2 tidak bisa internet:
```bash
# Reset DNS
sudo rm /etc/resolv.conf
sudo bash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'
sudo bash -c 'echo "nameserver 8.8.4.4" >> /etc/resolv.conf'
```

### Error "WslRegisterDistribution failed":
```powershell
# Restart WSL service
wsl --shutdown
# Tunggu 8 detik, lalu buka lagi
```

### Permission denied saat akses file Windows:
```bash
# Mount ulang dengan metadata
sudo umount /mnt/c
sudo mount -t drvfs C: /mnt/c -o metadata
```

---

## Keuntungan WSL2 vs Git Bash

| Feature | Git Bash | WSL2 |
|---------|----------|------|
| **Performance** | Lambat | Native Linux speed |
| **Compatibility** | Terbatas | 100% Linux tools |
| **Package Manager** | Tidak ada | apt, yum, pacman, dll |
| **Docker** | Perlu Docker Desktop | Native Docker |
| **File System** | Windows (lambat) | Linux (cepat) |
| **Development** | Basic | Full Linux dev environment |
| **SSH/Networking** | Terbatas | Full control |
| **Systemd** | Tidak | Ya (WSL 0.67.6+) |

---

## Next Steps

Setelah WSL2 setup:
1. Clone project: `git clone https://github.com/triapoets/Mp4-to-Mp3.git`
2. Setup auto-sync (sudah ada script-nya di project)
3. Install Python/Node.js dependencies
4. Mulai development seperti di Linux native!

---

**Catatan:** 
- Simpan file project di WSL filesystem (`~/projects/`), bukan di `/mnt/c/` untuk performance maksimal
- Gunakan Windows Terminal untuk experience terbaik
- WSL2 butuh virtualization enabled di BIOS
