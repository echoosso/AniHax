#!/bin/bash
echo "[*] Installing AniHax..."
chmod +x anihax.py
sudo cp anihax.py /usr/local/bin/anihax
echo "alias anihax='python3 /usr/local/bin/anihax'" >> ~/.bashrc
echo "[+] AniHax installed! Reload terminal or run: source ~/.bashrc"
