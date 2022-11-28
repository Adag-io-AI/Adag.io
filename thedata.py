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




def getChroma(file):
    y, sr = librosa.load(file, offset=0, duration=1.0)
    y_harm = librosa.effects.harmonic(y=y, margin=4)
    chroma = librosa.feature.chroma_cqt(y=y_harm, sr=sr, fmin=65.4, threshold=.4, n_chroma=12)
    chroma_array = numpy.array(chroma)
    chroma_mean = chroma_array.mean(axis=1)
    #chroma_min = numpy.min(chroma_array)
    #chroma_max = numpy.max(chroma_array)

    feature = chroma_mean
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

numpy.random.seed(99)

permutations = numpy.random.permutation(1248)
features = numpy.array(features)[permutations]
labels = numpy.array(labels)[permutations]

features_train = features[0:749]
labels_train = labels[0:749]

features_val = features[749:998]
labels_val = labels[749:998]

features_test = features[998:1248]
labels_test = labels[998:1248]

####################################################

inputs = keras.Input(shape=(12), name="feature")
x = keras.layers.Dense(300, activation="relu", name="dense_1")(inputs)
x = keras.layers.Dense(200, activation="relu", name="dense_2")(x)
outputs = keras.layers.Dense(48, activation="softmax", name="predictions")(x)

model = keras.Model(inputs=inputs, outputs=outputs)

model.compile(
    # Optimizer
    optimizer=keras.optimizers.Adam(),
    # Loss function to minimize
    loss=keras.losses.SparseCategoricalCrossentropy(),
    # List of metrics to monitor
    metrics=[keras.metrics.SparseCategoricalAccuracy()],
)
model.fit(x=features_train.tolist(),
          y=labels_train.tolist(),
          verbose=1,
          validation_data=(features_val.tolist(), labels_val.tolist()),
          epochs=32
          )

model.save('test_model2.h5')


score = model.evaluate(x=features_test.tolist(),y=labels_test.tolist(), verbose=0)
print('Accuracy : ' + str(score[1]*100) + '%')
