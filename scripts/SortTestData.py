
import os
import csv
from pydub import AudioSegment as audiosegment
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav

source = ("../../../Desktop/fma_small")
csvFileLocal = ("../../../Desktop/fma_small/tracksordered.csv")
sourceFolders = os.listdir(source)
destination = ("../tests/Spectograms")
holder = "holder.wav"

folder = os.listdir("../tests/Source MP3s")

genres = ["Hip-Hop", "Pop", "Rock", "Jazz", "Classical", "Country"]

            

def specgram(source, genre, destination, filename):
    file = audiosegment.from_mp3(source)

    #check if mp3 is mono audio
    if file.channels != 1:
        file = file.set_channels(1)

    #save new mono file as a wav file
    file.export(holder, format="wav")


    frequency_rate, data = wav.read(holder, 'r')
    fig = plt.figure(figsize = (19,12))
    pxx, frequency, bins, im = plt.specgram(x=data, Fs = frequency_rate, cmap = 'plasma', NFFT = 1024)
    plt.ylim([0, 8000])
    location = destination + '/' + genre + '/' + filename
    plt.savefig(location)
    plt.close()

    os.remove(holder)

i = 0

for root, dirs, files in os.walk(source):
    for filename in files:
        if os.path.splitext(filename)[1] == ".mp3":
            trackNum = os.path.splitext(filename)[0]

            print(i)
            i = i + 1

            with open(csvFileLocal, 'r') as csvfile:
                my_content = csv.reader(csvfile, delimiter=',')
                for row in my_content:

                    if trackNum in row:
                        location = os.path.join(root, filename)
                        print(location)
                        try:
                            specgram(location, row[1], destination, trackNum) 
                            print("specsaved")      
                        except:
                            print("error")

            


print("done")

                    







