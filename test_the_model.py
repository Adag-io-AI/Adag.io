import os
from keras.models import load_model
import pathlib
import h5py
import numpy
import tensorflow as tf
from tensorflow import keras
import librosa
import librosa.display
model = load_model('test_model1.h5')

dataset = 'dataset'
data_dir = pathlib.Path(dataset)

features = []
labels = []
chords = []
# This works and fills chords with the names of every folder
for name in os.listdir(dataset):
    chords.append(name)


def getChroma(file):
    y, sr = librosa.load(file, offset=0, duration=1.0)
    y_harm = librosa.effects.harmonic(y=y, margin=4)
    chroma = librosa.feature.chroma_cqt(y=y_harm, sr=sr, fmin=65.4, threshold=.4, n_chroma=12)
    chroma_array = numpy.array(chroma)
    chroma_mean = chroma_array.mean(axis=1)
        # chroma_min = numpy.min(chroma_array)
        # chroma_max = numpy.max(chroma_array)

    feature = chroma_mean
    print(feature)
    return feature

file_path = "dataset/D# Minor/20 d# - real guitar.wav"
feature = getChroma(file_path)
y = model.predict(feature.reshape(1,12))
ind = numpy.argmax(y)
print(chords[ind])