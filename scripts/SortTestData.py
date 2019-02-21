
import os
import eyed3

from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TRCK, TALB, USLT, error


source = ("../../../Desktop/fma_small")
sourceFolders = os.listdir(source)
destination = ("../tests/Source MP3s")

folder = os.listdir("../tests/Source MP3s")

genres = ["Hip-Hop", "Pop", "Rock", "Jazz", "Classical", "Country"]

for root, dirs, files in os.walk(source):
    for filename in files:
        if os.path.splitext(filename)[1] == ".mp3":
            file = os.path.join(root, filename)
            #os.chmod(file, S_IWOTH)
            #mp3 = MP3File(file)

            #song = eyed3.load(file)
            song = MP3(file, ID3=ID3)

            if song.tags.genre in genres:
                print("yes")
                #os.rename(file, destination + mp3.genre)
                #shutil.copyfile(file, destination + mp3.genre)

print("done")
            




