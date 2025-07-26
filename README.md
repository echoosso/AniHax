 # AniHax 🧠 Anime-Inspired Mindset Tool for Pentesters

AniHax is a CLI tool for Linux that brings emotion, energy, and personality into your hacking workflow.  
Instead of just running `nmap` or `burp`, AniHax adds **motivation, identity, and mindset** to your pentests, inspired by anime heroes who never give up.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b2edf788-e59d-4e78-b823-2ab71e378401" />

---

## 🌀 Why AniHax?

In penetration testing, mindset is everything and yet, most tools are soulless.

Anime heroes train hard, fail often, and fight against impossible odd, just like we do.  
They each have **unique powers, personalities, and ambitions**. That’s why AniHax exists:  
A tool that reflects your current phase technically and emotionally.

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

---🧪 Installation
<pre> 
git clone https://github.com/echoosso/AniHax.git
cd AniHax
pip install -r requirements.txt
chmod +x anihax.py

</pre>



✅ Requires: Python 3.x
📦 Install dependencies with:

<pre>pip install -r requirements.txt</pre>

 
Optional: Add to your .bashrc or .zshrc:
<pre>alias anihax="python3 /path/to/anihax.py"</pre>

## 🔁 Example Usage

<pre>
anihax stuck --mode fun
anihax found --mode focus
anihax emotion panic --mode logic
</pre>

---
## 🖼️ Supported Phases:

start, stuck, found, analyze, rooted, recon, ready,
critical, dominated, blocked, pivot, detect, report,
present, retake, firstaccess, silent, timeout

## 🧠 Supported Emotions:

panic, denial, exhausted

## 🇵🇸 Why the Palestinian Flag?

   In every anime, the hero fights against injustice, even alone, even when it’s hard.

The Palestinian flag is part of AniHax because it stands for:

   Resistance against oppression

   The courage to speak truth

   Identity and values, not just function

You’re free to change it,but for me, it stays.
Even behind a terminal, we carry a voice.


