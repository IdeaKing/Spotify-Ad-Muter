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

### 1 Use precompile binaries.

A prebuilt binary has already been built and can be accessed here:

### 2 Compile manually

1. Clone repository
2. CD into the main directory
3. Install requirements

        pip install -r requirements.txt
  
4. Compile using pyinstaller

        pyinstaller "mute-ify/mute-ify.py" --onefile -i "mute-ify/mute-ify.ico"  

- Note: If an error occurs:
  
        pyinstaller "src/main.py" --onefile -i "src/mute-ify.ico"
  
  
