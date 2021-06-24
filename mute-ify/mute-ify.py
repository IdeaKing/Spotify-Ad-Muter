"""
Created on 6/17/2021 for Father's Day 2021.

Code by Thomas Chia (IdeaKing)

Mute-ify mutes music playing on Spotify when an advertisement is playing.
"""
from pycaw.pycaw import AudioUtilities
from SwSpotify import spotify, SpotifyNotRunning 

def adjust_volume(mute):
    sessions = AudioUtilities.GetAllSessions()

    for session in sessions:
        volume = session.SimpleAudioVolume
        try:
            if session.Process.name() == "Spotify.exe":
                if mute == True:
                    volume.SetMute(1, None)
                else:
                    volume.SetMute(0, None)
        except:
            pass

def grab_playing():
    try:
        current_song = spotify.song()
        return current_song
    except SpotifyNotRunning as e:    
        return e

def mute_ify():
    while True:
        counter = 0
        current_song = grab_playing()

        if current_song == "Advertisement":
            adjust_volume(mute = True)
        else:
            adjust_volume(mute = False)    
        
print("Mute-ify is running.")
mute_ify()
