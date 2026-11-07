# Setup Claude Desktop dengan 9routerproxy via SSH Tunnel

Setup ini untuk **PC yang menjalankan Claude Desktop App**, bukan untuk PC ini.

## Informasi 9routerproxy
- **IP**: 192.168.1.83
- **SSH Port**: 22
- **Username**: root

---

## Langkah Setup di PC Claude Desktop

### 1. Generate SSH Key (jika belum ada)

**Windows (PowerShell):**
```powershell
ssh-keygen -t ed25519 -C "claude-desktop"
```

**Linux/Mac:**
```bash
ssh-keygen -t ed25519 -C "claude-desktop"
```

Tekan Enter 3x (terima default, tanpa passphrase untuk kemudahan)

### 2. Copy SSH Public Key ke 9routerproxy

**Windows (PowerShell):**
```powershell
type $env:USERPROFILE\.ssh\id_ed25519.pub | ssh root@192.168.1.83 "cat >> ~/.ssh/authorized_keys"
```

**Linux/Mac:**
```bash
ssh-copy-id root@192.168.1.83
```

Masukkan password root 9routerproxy ketika diminta.

### 3. Test SSH Connection

```bash
ssh root@192.168.1.83 "echo 'SSH OK'"
```

Jika muncul "SSH OK", berarti berhasil!

---

## Opsi A: Manual SSH Tunnel (Cepat untuk Testing)

### Windows (PowerShell/CMD)

```powershell
ssh -D 1080 -C -N root@192.168.1.83
```

### Linux/Mac

```bash
ssh -D 1080 -C -N root@192.168.1.83
```

**Biarkan terminal ini tetap terbuka!** Tunnel akan aktif selama terminal berjalan.

---

## Opsi B: Auto-Start SSH Tunnel (Recommended)

### Windows - Task Scheduler

1. Buat file `start-claude-tunnel.bat`:

```batch
@echo off
:loop
ssh -D 1080 -C -N -o ServerAliveInterval=60 -o ServerAliveCountMax=3 root@192.168.1.83
timeout /t 10
goto loop
```

2. Buat Task Scheduler:
   - Open Task Scheduler
   - Create Basic Task → "Claude Proxy Tunnel"
   - Trigger: "At log on"
   - Action: Start program → Browse ke `start-claude-tunnel.bat`
   - ✅ Run whether user is logged on or not

### Linux - systemd service

1. Buat file `/etc/systemd/system/claude-proxy.service`:

```ini
[Unit]
Description=SSH Tunnel for Claude Desktop
After=network.target

[Service]
Type=simple
User=YOUR_USERNAME
ExecStart=/usr/bin/ssh -D 1080 -C -N \
    -o ServerAliveInterval=60 \
    -o ServerAliveCountMax=3 \
    root@192.168.1.83
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

2. Enable dan start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable claude-proxy.service
sudo systemctl start claude-proxy.service
sudo systemctl status claude-proxy.service
```

### Mac - launchd

1. Buat file `~/Library/LaunchAgents/com.claude.proxy.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.claude.proxy</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/ssh</string>
        <string>-D</string>
        <string>1080</string>
        <string>-C</string>
        <string>-N</string>
        <string>-o</string>
        <string>ServerAliveInterval=60</string>
        <string>root@192.168.1.83</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
</dict>
</plist>
```

2. Load service:

```bash
launchctl load ~/Library/LaunchAgents/com.claude.proxy.plist
launchctl start com.claude.proxy
```

---

## Setup Claude Desktop App

Setelah tunnel aktif:

### 1. Via System Proxy

**Windows:**
```
Settings → Network & Internet → Proxy
- Manual proxy setup: ON
- Proxy server: socks5://localhost:1080
```

**Linux:**
```
Settings → Network → Network Proxy
- Method: Manual
- SOCKS Host: localhost
- Port: 1080
```

**Mac:**
```
System Preferences → Network → Advanced → Proxies
- ✅ SOCKS Proxy
- Server: localhost:1080
```

### 2. Via Environment Variable (Alternative)

**Windows (PowerShell):**
```powershell
$env:ALL_PROXY="socks5://localhost:1080"
# Lalu jalankan Claude Desktop dari terminal ini
```

**Linux/Mac:**
```bash
export ALL_PROXY=socks5://localhost:1080
# Lalu jalankan Claude Desktop dari terminal ini
```

---

## Verifikasi

### 1. Cek tunnel aktif

**Windows:**
```powershell
netstat -ano | findstr "1080"
```

**Linux/Mac:**
```bash
netstat -tuln | grep 1080
# atau
lsof -i :1080
```

### 2. Test SOCKS proxy

```bash
curl --socks5 localhost:1080 https://api.anthropic.com/health
```

### 3. Test di Claude Desktop

Buka Claude Desktop → coba chat → jika berhasil connect, proxy bekerja!

---

## Troubleshooting

### Tunnel tidak stabil
Tambahkan keepalive options:
```bash
ssh -D 1080 -C -N \
    -o ServerAliveInterval=30 \
    -o ServerAliveCountMax=3 \
    -o TCPKeepAlive=yes \
    root@192.168.1.83
```

### Permission denied
Pastikan SSH key sudah ter-copy:
```bash
ssh root@192.168.1.83 "cat ~/.ssh/authorized_keys"
```

### Claude Desktop tidak bisa connect
1. Restart tunnel
2. Restart Claude Desktop
3. Clear Claude cache
4. Cek firewall tidak block port 1080

---

## Stop Tunnel

**Manual tunnel:** Tekan `Ctrl+C` di terminal

**Windows Task Scheduler:** Disable task

**Linux systemd:**
```bash
sudo systemctl stop claude-proxy.service
```

**Mac launchd:**
```bash
launchctl stop com.claude.proxy
launchctl unload ~/Library/LaunchAgents/com.claude.proxy.plist
```

---

## Summary

✅ **Yang sudah di-setup:**
- SSH tunnel: PC Claude Desktop → 9routerproxy (192.168.1.83)
- SOCKS5 proxy di: `localhost:1080`

📋 **Untuk gunakan Claude Desktop:**
1. Pastikan tunnel aktif (cek `netstat`)
2. Set system proxy atau environment variable
3. Jalankan Claude Desktop
4. Profit! 🎉
