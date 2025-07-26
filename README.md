 AniHax 🧠🎌 — Anime-Inspired Mindset Tool for Pentesters

AniHax is a CLI tool for Linux that brings emotion, energy, and personality into your hacking workflow.  
Instead of just running `nmap` or `burp`, AniHax adds **motivation, identity, and mindset** to your pentests — inspired by anime heroes who never give up.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b2edf788-e59d-4e78-b823-2ab71e378401" />

---

## 🌀 Why AniHax?

In penetration testing, mindset is everything — and yet, most tools are soulless.

Anime heroes train hard, fail often, and fight against impossible odds — just like we do.  
They each have **unique powers, personalities, and ambitions**. That’s why AniHax exists:  
A tool that reflects your current phase — technically and emotionally.

AniHax changes your:

- 💻 Wallpaper (based on pentest phase or emotion)
- 💬 Mindset quote (from `motivation.json`)
- 🔔 Notification (if supported)
- 🎌 Terminal banner (with anime + Palestine design)

---

## ✨ Features

- ✅ Anime/Hacker ASCII banner on start
- 🎌 Integrated **Palestinian flag** as a symbol of justice & identity
- 🧠 Phase- and emotion-based wallpaper switching
- 📢 Native Linux notifications (`notify-send`)
- ⚙️ Supports GNOME, XFCE, KDE, i3 (via `feh`)
- 💬 Custom motivational quotes via `motivation.json`
- 🧩 Modes: `focus`, `fun`, `logic`

---

## 🔁 Example Usage

```bash
./anihax.py stuck --mode fun
./anihax.py found --mode focus
./anihax.py emotion panic --mode logic
