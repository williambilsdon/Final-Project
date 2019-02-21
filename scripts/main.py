
import os
from pydub import AudioSegment as audiosegment

#set file locations

source = "/Users/williambilsdon/Desktop/FMP/Music/Test/Classic/Summer_Symphony_Ball.mp3"
dest = "/Users/williambilsdon/Desktop/FMP/Music/Test/Classic/SummerSymphonyBall.wav"


file = audiosegment.from_mp3(source)

#check if mp3 is mono audio
if file.channels != 1:
	file = file.set_channels(1)

#save new mono file as a wav file
file.export(dest, format="wav")

print(file.channels)

import matplotlib.pyplot as plt
from scipy.io import wavfile as wav

frequency_rate, data = wav.read(dest, 'r')
fig = plt.figure(figsize = (19,12))
pxx, frequency, bins, im = plt.specgram(x=data, Fs = frequency_rate, cmap = 'plasma', NFFT = 1024)
plt.ylim([0, 12000])
plt.savefig('spectogram5.png')

#Clear wav file after spectogram generated
os.remove(dest)

print("finished")




