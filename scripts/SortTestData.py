import os
from pydub import AudioSegment as audiosegment
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav

source = ("../gtzan")
sourceFolders = os.listdir(source)
destination = ("../tests")
holder = "holder.wav"



genres = ["Hip-Hop", "Pop", "Rock", "Jazz", "Classical", "Country"]



def specgram(trackDest, genre, trackSource):
    file = audiosegment.from_mp3(trackSource)

    #check if mp3 is mono audio
    if file.channels != 1:
        file = file.set_channels(1)

    #save new mono file as a wav file
    file.export(holder, format="wav")


    frequency_rate, data = wav.read(holder, 'r')
    fig = plt.figure(figsize = (19,12))
    pxx, frequency, bins, im = plt.specgram(x=data, Fs = frequency_rate, cmap = 'plasma', NFFT = 1024)
    plt.ylim([0, 8000])
    plt.savefig(trackDest)
    plt.close()

    os.remove(holder)

classical = 0
country = 0
jazz = 0

for root, dirs, files in os.walk(source):
    for filename in files:
        trackNum = os.path.splitext(filename)[0]
        #print(trackNum)
        genre = trackNum.split(".")

        trackDest = destination + '/' + genre[0] + '/' + trackNum + '.png'
        trackSource = source + '/' + genre[0] + '/' + filename

        #print(trackSource)

        specgram(trackDest, genre, trackSource)



print("done")
