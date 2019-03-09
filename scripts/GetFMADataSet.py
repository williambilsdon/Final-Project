import csv
import os
from pydub import AudioSegment as audiosegment
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
import cv2

holder = "holder.wav"
csvLocation = '../../tracks.csv'
origin = '../../fma_medium'
csvFile = csv.reader(open(csvLocation, 'r'))
data = [row for row in csv.reader(csvLocation)]
trackDest = ("../wholepngs/training data")
trackValDest = ('../wholepngs/validation data')
sliceDest= ("../slices/training data")
sliceValDest = ('../slices/validation data')

genreValues = ['rock', 'classical', 'country', 'jazz', 'reggae', 'disco', 'pop', 'hiphop', 'metal', 'blues']

def imageSlice(source, sliceDest):

    imageX = 3200
    numSlices = 10
    xStride = imageX / numSlices

    if os.path.splitext(source)[1] != '.DS_Store':
        xPos = 0
        newX = int(xPos) + int(xStride)
                #print(destination)
                #os.makedirs(destination)

        filename = os.path.splitext(source)[0]

        for i in range(0,10):
            location = source
            original = cv2.imread(location)
            slice = original[0:2400, int(xPos):int(newX)]

            name = filename.split('/')

            cv2.imwrite((sliceDest + '/' + name[4] + '_' + str(i) + '.png'), slice)

            #print(sliceDest + '/' + name[3] + '_' + str(i) + '.png')

            xPos += xStride
            newX += xStride

def specgram(trackDest, trackSource, sliceDest):
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

    imageSlice(trackDest, sliceDest)

error = 0
csvIDs = []
for row in csvFile:
    split = list(row[0])

    while len(split) < 6:
        split.insert(0, '0')

        idExt = split

        idExt = ''.join(idExt)


    for root, dirs, files in os.walk(origin):
        for filename in files:
            trackNum = os.path.splitext(filename)[0]

            if trackNum == idExt:
                genre = row[40].lower()

                if genre == 'hip-hop':
                    genre = 'hiphop'

                if genre in genreValues:
                    source = root + '/' + filename
                    trackDestination = trackDest + '/' + genre + '/' + genre + '_fma' + trackNum +'.png'
                    sliceDestination = sliceDest + '/' + genre

                    try:
                        specgram(trackDestination, source, sliceDestination)
                    except:
                        error += 1
                        print(error)
