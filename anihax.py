#!/usr/bin/env python3
import sys
import os
import json
import random
import subprocess

WALLPAPERS = {
    "start": "./img/start.jpg",
    "stuck": "./img/stuck.jpg",
    "found": "./img/found.jpg",
    "analyze": "./img/analyze.jpg",
    "rooted": "./img/rooted.jpg",
    "recon": "./img/recon.jpg",
    "ready": "./img/ready.jpg",
    "critical": "./img/critical.jpg",
    "dominated": "./img/dominated.jpg",
    "blocked": "./img/blocked.jpg",
    "pivot": "./img/pivot.jpg",
    "detect": "./img/detect.jpg",
    "report": "./img/report.jpg",
    "present": "./img/present.jpg",
    "retake": "./img/retake.jpg",
    "firstaccess": "./img/firstaccess.jpg",
    "silent": "./img/silent.jpg",
    "timeout": "./img/timeout.jpg",
    "panic": "~./img/emotions/panic.jpg",
    "denial": "./img/emotions/denial.jpg",
    "exhausted": "./img/emotions/exhausted.jpg"
}

def load_motivations(filepath="motivation.json"):
    if not os.path.exists(filepath):
        print(f"❌ Motivation file '{filepath}' not found.")
        return {}
    with open(filepath, "r") as file:
        return json.load(file)
import os
import subprocess

def set_wallpaper(path):
    path = os.path.abspath(os.path.expanduser(path))
    if not os.path.exists(path):
        print(f"❌ Wallpaper not found: {path}")
        return False

    uri = f"file://{path}"
    desktop_env = os.environ.get("XDG_CURRENT_DESKTOP", "").lower()

    try:
        # GNOME
        if "gnome" in desktop_env:
            subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", uri], check=True)
            subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri-dark", uri], check=True)
            subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-options", "scaled"], check=True)
            print(f"✅ Wallpaper set (GNOME): {os.path.basename(path)}")
            return True

        # XFCE
        elif "xfce" in desktop_env:
            output = subprocess.check_output(["xfconf-query", "--channel", "xfce4-desktop", "--list"]).decode()
            success = False
            for line in output.splitlines():
                if "/last-image" in line or "/image-path" in line:
                    subprocess.run([
                        "xfconf-query", "--channel", "xfce4-desktop",
                        "--property", line.strip(),
                        "--set", path
                    ], check=True)
                    success = True
                if "/image-style" in line:
                    subprocess.run([
                        "xfconf-query", "--channel", "xfce4-desktop",
                        "--property", line.strip(),
                        "--set", "3"  # 3 = scaled
                    ], check=True)
            if success:
                print(f"✅ Wallpaper set (XFCE): {os.path.basename(path)}")
                return True
            else:
                print("⚠️ No image path found in XFCE config.")
                return False

        # KDE / Plasma
        elif "kde" in desktop_env or "plasma" in desktop_env:
            if subprocess.run(["which", "plasma-apply-wallpaperimage"], capture_output=True).returncode == 0:
                subprocess.run(["plasma-apply-wallpaperimage", path], check=True)
                print(f"✅ Wallpaper set (KDE): {os.path.basename(path)}")
                return True
            else:
                print("❌ KDE detected, but 'plasma-apply-wallpaperimage' not found.")
                return False

        # Fallback for i3, bspwm, etc. using feh
        else:
            if subprocess.run(["which", "feh"], capture_output=True).returncode == 0:
                subprocess.run(["feh", "--bg-scale", path], check=True)
                print(f"✅ Wallpaper set (feh fallback): {os.path.basename(path)}")
                return True
            else:
                print("❌ No supported method found. Consider installing 'feh'.")
                return False

    except subprocess.CalledProcessError as e:
        print(f"❌ Error setting wallpaper: {e}")
        return False


def send_notification(quote, phase="AniHax"):
    try:
        subprocess.run(["notify-send", phase, quote])
    except Exception as e:
        print(f"❌ Failed to send notification: {e}")

def get_mode_argument(args):
    if '--mode' in args:
        idx = args.index('--mode')
        if idx + 1 < len(args):
            return args[idx + 1].lower()
    return 'focus'

def main():
    motivations = load_motivations()
    if len(sys.argv) < 2:
        print("Usage: anihax <phase|emotion> [type] [--mode <focus|fun|logic>]")
        return

    mode = get_mode_argument(sys.argv)
    if mode not in motivations["modes"]:
        print(f"❌ Unknown mode '{mode}'. Available modes: {', '.join(motivations['modes'].keys())}")
        return

    category = sys.argv[1].lower()

    if category == "emotion":
        if len(sys.argv) < 3:
            print("Usage: anihax emotion <panic|denial|exhausted> [--mode <focus|fun|logic>]")
            return
        emotion_type = sys.argv[2].lower()
        if emotion_type in WALLPAPERS:
            if set_wallpaper(WALLPAPERS[emotion_type]):
                quote = random.choice(motivations["emotions"].get(emotion_type, ["Stay calm!"]))
                print(quote)
                send_notification(quote, f"AniHax · {emotion_type}")
        else:
            print(f"❌ Unknown emotion '{emotion_type}'. Available emotions: {', '.join(motivations['emotions'].keys())}")
        return

    if category in WALLPAPERS:
        if set_wallpaper(WALLPAPERS[category]):
            quote = random.choice(motivations["phases"].get(category, ["Keep going!"]))
            print(quote)
            send_notification(quote, f"AniHax · {category}")
    else:
        print(f"❌ Unknown phase '{category}'. Available phases: {', '.join(WALLPAPERS.keys())}")

if __name__ == "__main__":
    main()
