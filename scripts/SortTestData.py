import os
from pydub import AudioSegment as audiosegment
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav

from ImageSlicer import imageSlice

source = ("../gtzan")
sourceFolders = os.listdir(source)
destination = ("../training data")
holder = "holder.wav"





def specgram(trackDest, genre, trackSource):
    file = audiosegment.from_mp3(trackSource)

    #check if mp3 is mono audio
    if file.channels != 1:
        file = file.set_channels(1)

    #save new mono file as a wav file
    file.export(holder, format="wav")


    frequency_rate, data = wav.read(holder, 'r')
    fig, ax = plt.subplots(1)
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    ax.axis('off')
    pxx, frequency, bins, im = plt.specgram(x=data, Fs = frequency_rate, cmap = 'plasma', NFFT = 1024)
    plt.ylim([0, 10000])
    ax.axis('off')
    fig.savefig(trackDest, dpi=500, frameon='false')
    plt.close()

    os.remove(holder)

    imageSlice(trackDest)

    os.remove(trackDest)

for root, dirs, files in os.walk(source):
    for filename in files:
        trackNum = os.path.splitext(filename)[0]
        #print(trackNum)
        splitName = trackNum.split(".")

        trackDest = destination + '/' + splitName[0] + '_' + splitName[1] + '.png'
        trackSource = source + '/' + splitName[0] + '/' + filename

        #print(trackSource)

        specgram(trackDest, splitName, trackSource)



print("done")
