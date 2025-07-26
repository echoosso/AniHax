#!/usr/bin/env python3

import sys
import os
import json
import random
import subprocess

from colorama import Fore, Back, Style, init
init(autoreset=True)

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
    "panic": "./img/emotions/panic.jpg",
    "denial": "./img/emotions/denial.jpg",
    "exhausted": "./img/emotions/exhausted.jpg"
}

def anime_banner_with_flag():
    banner = f"""{Fore.CYAN}
              )   (         )                )  
   (       ( /(   )\ )   ( /(     (       ( /(  
   )\      )\()) (()/(   )\())    )\      )\()) 
((((_)(   ((_)\   /(_)) ((_)\  ((((_)(   ((_)\  
 )\ _ )\   _((_) (_))    _((_)  )\ _ )\  __((_) 
 (_)_\(_) | \| | |_ _|  | || |  (_)_\(_) \ \/ / 
  / _ \   | .` |  | |   | __ |   / _ \    >  <  
 /_/ \_\  |_|\_| |___|  |_||_|  /_/ \_\  /_/\_\ 
                                                


   {Fore.MAGENTA}『 AniHax 』 {Fore.YELLOW}|  Hack Your Mood. Unleash Your Inner Anime Hacker!{Style.RESET_ALL}

{Style.BRIGHT + Back.BLACK}{" " * 34}{Style.RESET_ALL}
{Fore.RED + "  ▲" + Back.BLACK}{" " * 31}{Style.RESET_ALL}
{Back.WHITE}{" " * 34}{Style.RESET_ALL}
{Fore.RED + "  ▲" + Back.WHITE}{" " * 31}{Style.RESET_ALL}
{Back.GREEN}{" " * 34}{Style.RESET_ALL}
{Fore.RED + "  ▲" + Back.GREEN}{" " * 31}{Style.RESET_ALL}

{Fore.RED + Style.BRIGHT}   🇵🇸  FREE PALESTINE  🇵🇸
{Fore.GREEN}   May justice and peace prevail for all people.
{Fore.YELLOW}   ‘The one who helps the oppressed is truly blessed.’
{Style.RESET_ALL}
"""
    print(banner)

def show_help():
    print(f"""{Fore.GREEN}
AniHax - Anime-Inspired Hacker Mindset Tool

Usage: {Fore.CYAN}anihax <phase|emotion> [type] [--mode <focus|fun|logic>]{Fore.RESET}

Phases:
  {Fore.YELLOW}start, stuck, found, analyze, rooted, recon, ready, critical, dominated, blocked,
  pivot, detect, report, present, retake, firstaccess, silent, timeout

Emotions:
  {Fore.MAGENTA}panic, denial, exhausted

Modes (optional):
  {Fore.BLUE}focus{Fore.RESET} (default), {Fore.CYAN}fun{Fore.RESET}, {Fore.YELLOW}logic

Examples:
  {Fore.CYAN}anihax found --mode fun
  anihax emotion panic --mode logic
  anihax report
""")

def load_motivations(filepath="motivation.json"):
    if not os.path.exists(filepath):
        print(f"{Fore.RED}❌ Motivation file '{filepath}' not found.")
        return {}
    with open(filepath, "r") as file:
        return json.load(file)

def set_wallpaper(path):
    path = os.path.abspath(os.path.expanduser(path))
    if not os.path.exists(path):
        print(f"{Fore.RED}❌ Wallpaper not found: {path}")
        return False

    uri = f"file://{path}"
    desktop_env = os.environ.get("XDG_CURRENT_DESKTOP", "").lower()

    try:
        if "gnome" in desktop_env:
            subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", uri], check=True)
            subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri-dark", uri], check=True)
            subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-options", "scaled"], check=True)
            print(f"{Fore.GREEN}✅ Wallpaper set (GNOME): {os.path.basename(path)}")
            return True
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
                        "--set", "3"
                    ], check=True)
            if success:
                print(f"{Fore.GREEN}✅ Wallpaper set (XFCE): {os.path.basename(path)}")
                return True
            else:
                print(f"{Fore.YELLOW}⚠️ No image path found in XFCE config.")
                return False
        elif "kde" in desktop_env or "plasma" in desktop_env:
            if subprocess.run(["which", "plasma-apply-wallpaperimage"], capture_output=True).returncode == 0:
                subprocess.run(["plasma-apply-wallpaperimage", path], check=True)
                print(f"{Fore.GREEN}✅ Wallpaper set (KDE): {os.path.basename(path)}")
                return True
            else:
                print(f"{Fore.RED}❌ KDE detected, but 'plasma-apply-wallpaperimage' not found.")
                return False
        else:
            if subprocess.run(["which", "feh"], capture_output=True).returncode == 0:
                subprocess.run(["feh", "--bg-scale", path], check=True)
                print(f"{Fore.GREEN}✅ Wallpaper set (feh fallback): {os.path.basename(path)}")
                return True
            else:
                print(f"{Fore.RED}❌ No supported method found. Consider installing 'feh'.")
                return False
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}❌ Error setting wallpaper: {e}")
        return False

def send_notification(quote, phase="AniHax"):
    try:
        subprocess.run(["notify-send", phase, quote])
    except Exception as e:
        print(f"{Fore.RED}❌ Failed to send notification: {e}")

def get_mode_argument(args):
    if '--mode' in args:
        idx = args.index('--mode')
        if idx + 1 < len(args):
            return args[idx + 1].lower()
    return 'focus'

def main():
    anime_banner_with_flag()
    motivations = load_motivations()
    if len(sys.argv) < 2:
        show_help()
        return

    if sys.argv[1].lower() in ['-h', '--help', 'help']:
        show_help()
        return

    mode = get_mode_argument(sys.argv)
    if "modes" in motivations and mode not in motivations["modes"]:
        print(f"{Fore.RED}❌ Unknown mode '{mode}'. Available: {', '.join(motivations['modes'].keys())}")
        return

    category = sys.argv[1].lower()

    # EMOTION (panic/denial/exhausted)
    if category == "emotion":
        if len(sys.argv) < 3:
            print(f"{Fore.RED}Usage: anihax emotion <panic|denial|exhausted> [--mode <focus|fun|logic>]")
            return
        emotion_type = sys.argv[2].lower()
        if emotion_type in WALLPAPERS:
            if set_wallpaper(WALLPAPERS[emotion_type]):
                msg = random.choice(motivations["emotions"].get(emotion_type, ["Stay calm!"]))
                print(Fore.MAGENTA + msg)
                send_notification(msg, f"AniHax · {emotion_type}")
        else:
            print(f"{Fore.RED}❌ Unknown emotion '{emotion_type}'. Available: {', '.join(motivations['emotions'].keys())}")
        return

    # PHASE (stuck, found, report, etc.)
    if category in WALLPAPERS:
        if set_wallpaper(WALLPAPERS[category]):
            msg = random.choice(motivations["phases"].get(category, ["Keep going!"]))
            print(Fore.CYAN + msg)
            send_notification(msg, f"AniHax · {category}")
    else:
        print(f"{Fore.RED}❌ Unknown phase '{category}'. Available: {', '.join(WALLPAPERS.keys())}")

if __name__ == "__main__":
    main()
