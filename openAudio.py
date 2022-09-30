import os
from platform import platform
import numpy
from tensorflow import keras
import librosa
import librosa.display
import matplotlib.pyplot as plt



#fuck you queenie you prick

#major A piano chord sample
example_file = "dataset/Piano_Major/Grand Piano - Fazioli - major A middle.wav"
#librosa loads the file with y=audio wav, and sr is the sample rate
#duration is just 1 second
y, sr = librosa.load(example_file, offset=0, duration=1.0)

#makes a spectrogram and a chromagram with the audio file
melspectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
#the chromagram is our pitch class profile with all the notes on a scale, there is a threshold 
#that i dont entirely understand the workings of, but most of this stuff is on libros's website
chroma = librosa.feature.chroma_cqt(y=y, sr=sr, fmin=65.4, threshold=.4, n_chroma = 12)


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


#this nonsense doesnt work yet
#makes the array wrong, need to look up how to convert the chromagram to a vector that looks like 
#[0,0,1,0,0,0,1,0,0,1]
#need to normalize the average signal from each row of the chromagram to either a 1 or a 0 with 
#a threshold that gets rid of pitches that we dont want included into the chord, which is what makes
#more elaborate chords more difficult, bc even this audio file is very clear and simple and
#pitches that arent being played are still showing up
chroma_array = numpy.array(chroma)
print(chroma_array)
librosa.util.normalize(chroma_array, norm = 1, threshold = .4, fill = False)
print(chroma_array)