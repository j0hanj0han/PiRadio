import vlc
import time
# get the radio you want
playlist = ["http://cdn.nrjaudio.fm/audio1/fr/40102/aac_576.mp3","http://direct.franceinfo.fr/live/franceinfo-midfi.mp3"]
player = vlc.MediaPlayer(playlist[0])

radio = player.play()
time.sleep(15)

    
while True:
    if player.is_playing() == 1:
       print("Lecture en cours")
       time.sleep(5)
    else: 
        print("Pas de son, on relance la lecture")
        radio = player.play()
        time.sleep(5)



# for song in playlist:
#     player = vlc.MediaPlayer(song)
#     player.play()
# player.play()
# # put this function in a button 
# player.pause()
# player.stop

if __name__ == "__main__":
    pass