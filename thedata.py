import os
from platform import platform
import numpy
from tensorflow import keras
import librosa
import librosa.display
import matplotlib.pyplot as plt



def getFeatures(file):
    y, sr = librosa.load(file, offset=0, duration=1.0)
    y_harm = librosa.effects.harmonic(y=y, margin=4)
    chroma = librosa.feature.chroma_cqt(y=y_harm, sr=sr, fmin=65.4, threshold=.4, n_chroma = 12)
    chroma_array = numpy.array(chroma)
    chroma_mean = chroma_array.mean(axis=1)
    chroma_min = numpy.min(chroma_array)
    chroma_max = numpy.max(chroma_array)

    feature = numpy.concatenate((chroma_mean,chroma_min,chroma_max))
    return feature


dataset = 'dataset'
features = []
labels = []
folders = ["Piano_Major","Piano_Minor"]
majorRoots = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
minorRoots = ["A#m","Am","Bm","C#m","Cm","D#m","Dm","Em","F#m","Fm","G#m","Gm"]    

for type in folders: 
    x = 0
    for root in os.listdir(dataset+"/"+type):
        filename = dataset+"/"+type+"/"+root

        features.append(getFeatures(filename))
        if type=="Piano_Major":
            label = majorRoots[x]
        else:
            label = minorRoots[x]
        x += 1
        labels.append(label)
        

#the collection of features has been made
#now we shuffle them to be used as training for the model

permu = numpy.random.permutation(300)
features = numpy.array(features)[permu]
labels = numpy.array(labels)[permu]

fTrain = features[0:180]
lTrain = labels[0:180]

fVal = features[180:240]
lVal = labels[180:240]

fTest = features[240:300]
lTest = labels[240:300]