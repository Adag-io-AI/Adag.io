import os
import pathlib
from platform import platform
import numpy
import tensorflow as tf
from tensorflow import keras
import librosa
import librosa.display
import matplotlib.pyplot as plt
from keras import layers
from keras import models


seed = 99
tf.random.set_seed(seed)
numpy.random.seed(seed)

def getChroma(file):
    y, sr = librosa.load(file, offset=0, duration=1.0)
    y_harm = librosa.effects.harmonic(y=y, margin=4)
    chroma = librosa.feature.chroma_cqt(y=y_harm, sr=sr, fmin=65.4, threshold=.4, n_chroma=12)
    chroma_array = numpy.array(chroma)
    # trying to use 2d array now
    #chroma_mean = chroma_array.mean(axis=1)
    #chroma_min = numpy.min(chroma_array)
    #chroma_max = numpy.max(chroma_array)

    feature = chroma_array
    print(feature)
    return feature


dataset = 'dataset'
data_dir = pathlib.Path(dataset)

features = []
labels = []
chords = []
# This works and fills chords with the names of every folder
for name in os.listdir(dataset):
    chords.append(name)

for chord in chords:
    print("Calculating features for chord : " + chord)
    for file in os.listdir(dataset+"/"+chord):
        file_path = dataset+"/"+chord+"/"+file

        features.append(getChroma(file_path))
        label = chords.index(chord)
        labels.append(label)

print(labels)

permutations = numpy.random.permutation(288)
features = numpy.array(features)[permutations]
labels = numpy.array(labels)[permutations]

features_train = features[0:180]
labels_train = labels[0:180]

features_val = features[180:240]
labels_val = labels[180:240]

features_test = features[240:288]
labels_test = labels[240:288]

####################################################

#inputs = keras.Input(shape=(12,44), name="feature")
#x = keras.layers.Dense(288, activation="relu", name="dense_1")(inputs)
#x = keras.layers.Dense(288, activation="relu", name="dense_2")(x)
#outputs = keras.layers.Dense(48, activation="softmax", name="predictions")(x)

#model = keras.Model(inputs=inputs, outputs=outputs)


#iffy statement
input_shape = features_test[1].shape[1:]
print('Input shape:', input_shape)
num_labels = len(chords)
norm_layer = layers.Normalization()
# Fit the state of the layer to the spectrograms
# with `Normalization.adapt`.
norm_layer.adapt(data=features_train.map(map_func=lambda spec, label: spec))

model = models.Sequential([
    layers.Input(shape=input_shape),
    # Downsample the input.
    layers.Resizing(32, 32),
    # Normalize.
    norm_layer,
    layers.Conv2D(32, 3, activation='relu'),
    layers.Conv2D(64, 3, activation='relu'),
    layers.MaxPooling2D(),
    layers.Dropout(0.25),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(num_labels),
])

model.summary()

model.compile(
    optimizer=tf.keras.optimizers.Adam(),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy'],
)
model.fit(x=features_train.tolist(),y=labels_train.tolist(),verbose=1,validation_data=(features_val.tolist() , labels_val.tolist()), epochs=64)


score = model.evaluate(x=features_test.tolist(),y=labels_test.tolist(), verbose=0)
print('Accuracy : ' + str(score[1]*100) + '%')


#majorRoots = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
#minorRoots = ["A#m", "Am", "Bm", "C#m", "Cm", "D#m", "Dm", "Em", "F#m", "Fm", "G#m", "Gm"]

#for type in folders:
#    x = 0
#    for root in os.listdir(dataset + "/" + type):
#        filename = dataset + "/" + type + "/" + root
#
#        features.append(getFeatures(filename))
#        if type == "Piano_Major":
#            label = majorRoots[x]
#        else:
#            label = minorRoots[x]
#        x += 1
#        labels.append(label)

# the collection of features has been made
# now we shuffle them to be used as training for the model

#permu = numpy.random.permutation(300)
#features = numpy.array(features)[permu]
#labels = numpy.array(labels)[permu]

#fTrain = features[0:180]
#lTrain = labels[0:180]

#fVal = features[180:240]
#lVal = labels[180:240]

#fTest = features[240:300]
#lTest = labels[240:300]
