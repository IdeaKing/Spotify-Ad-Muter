# Spotify-Ad-Muter: Mute-ify

A python program that mutes Spotify when an Advertisement is playing. Designed for 64-Bit Windows 7/8.1/10.

Features:
- Mutes only the Spotify Application when the ad is playing.
- Low priority for lower CPU usage.
- Low RAM usage.

Upcoming:
- Complete Ad-Blocking
- U.I.

## Installation Guide

### 1. Use precompiled binaries.

A prebuilt binary has already been built and can be accessed here: https://github.com/IdeaKing/Spotify-Ad-Muter/releases/tag/v1.0.0

### 2. Compile manually

1. Clone repository
2. CD into the main directory
3. Install requirements in virtual environment

        python -m venv venv
        venv/Scripts/activate
        pip install -r requirements.txt
  
4. Compile using pyinstaller

        pyinstaller "mute-ify/mute-ify.py" --onefile -i "mute-ify/mute-ify.ico"  

- Note: If an error occurs uninstall enum34
  
        pip uninstall -y enum34

5. Now the executable should be in the generated "dist" folder.
  
