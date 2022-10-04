import os
from platform import platform
import numpy
from tensorflow import keras
import librosa
import librosa.display
import matplotlib.pyplot as plt





#major A piano chord sample
example_file = "dataset/Piano_Major/Grand Piano - Fazioli - major A middle.wav"
#librosa loads the file with y=audio wav, and sr is the sample rate
#duration is just 1 second
y, sr = librosa.load(example_file, offset=0, duration=1.0)

#makes a spectrogram and a chromagram with the audio file
melspectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
#the chromagram is our pitch class profile with all the notes on a scale, there is a threshold 
#that i dont entirely understand the workings of, but most of this stuff is on libros's website
y_harm = librosa.effects.harmonic(y=y, margin=4)
chroma = librosa.feature.chroma_cqt(y=y_harm, sr=sr, fmin=65.4, threshold=.4, n_chroma = 12)


#pyplot.imshow(chromagram, interpolation='nearest', aspect='auto') 
#pyplot.show()

#this is just formatting to put the two graphs onto a print statement
#dont have to use this to print the data either
#might have to use something else anyway for realtime interaction
fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
img = librosa.display.specshow(melspectrogram, y_axis='hz', x_axis='time', ax=ax[0])
ax[0].set(title='melspectrogram')
ax[0].label_outer()
img = librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', ax=ax[1])
ax[1].set(title='chromagram')
fig.colorbar(img, ax=ax)
plt.show()


#means out array to 0s and 1s based on a threshold of .1 average
chroma_array = numpy.array(chroma)
#print(chroma_array)
chroma_average = chroma_array.mean(axis=1)
chroma_average[chroma_average<.1] = 0
chroma_average[chroma_average>=.1] = 1
print(chroma_average)