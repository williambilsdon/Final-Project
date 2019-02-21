
import os
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH

source = ("../../../Desktop/fma_small")
sourceFolders = os.listdir(source)
destination = ("../tests/Source MP3s")

folder = os.listdir("../tests/Source MP3s")

genres = ["Hip-Hop", "Pop", "Rock", "Jazz", "Classical", "Country"]

for root, dirs, files in os.walk(source):
    for filename in files:
        if os.path.splitext(filename)[1] == ".mp3":
            file = os.path.join(root, filename)
            mp3 = MP3File(file)
            if mp3.genre in genres:
                os.rename(file, destination + mp3.genre)
            




