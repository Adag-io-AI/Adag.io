import os
from keras.models import load_model
import pathlib
import h5py
import numpy
import tensorflow as tf
from tensorflow import keras
import librosa
import librosa.display
import tkinter
import pyaudio
import wave

class audio_input(object):
    def __init__(self):
        self.FORMAT = pyaudio.paFloat32
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024
        self.p = None
        self.stream = None

    def start_listening(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  output=False,
                                  stream_callback=self.callback,
                                  frames_per_buffer=self.CHUNK)

    def stop(self):
        self.stream.close()
        self.p.terminate()

    def get_chroma(self, in_data, frame_count, time_info, flag):
        audio_array = numpy.frombuffer(in_data, dtype=numpy.float32)
        y_harm = librosa.effects.harmonic(y=audio_array, margin=4)
        chroma = librosa.feature.chroma_cqt(y=y_harm, sr=sr, fmin=65.4, threshold=.4, n_chroma=12)
        chroma_array = numpy.array(chroma)
        chroma_mean = chroma_array.mean(axis=1)
        y = model.predict(chroma_mean.reshape(1, 12))
        ind = numpy.argmax(y)
        print(chords[ind])
        #return chroma_mean

        return None, pyaudio.paContinue

def getChroma(file):
    y, sr = librosa.load(file, offset=0, duration=1.0)
    y_harm = librosa.effects.harmonic(y=y, margin=4)
    chroma = librosa.feature.chroma_cqt(y=y_harm, sr=sr, fmin=65.4, threshold=.4, n_chroma=12)
    chroma_array = numpy.array(chroma)
    chroma_mean = chroma_array.mean(axis=1)
        # chroma_min = numpy.min(chroma_array)
        # chroma_max = numpy.max(chroma_array)

    feature = chroma_mean

    # print(feature)
    return feature
def exit():
    text.configure(text="Press to start", font=("Arial Bold", 18))
    start.configure(text="start", command=starting)

def starting():
    text.configure(text="Starting...", font=("Arial Bold", 18))
    start.configure(text="stop", command=exit)

CHUNK = 1024
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 1
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
model = load_model('test_model2.h5')
dataset = 'dataset'
data_dir = pathlib.Path(dataset)
chords = []
for name in os.listdir(dataset):
    chords.append(name)

box = tkinter.Tk()
box.geometry('350x200')
box.title("Adag.io")
text = tkinter.Label(box, text="Press to start", font=("Arial Bold", 18))
text.grid(column=5, row=0)
start = tkinter.Button(box, text="start", command=starting)
start.grid(column=5, row=5)
box.mainloop()












file_path = "song_samples/karate(A Major).wav"
feature = getChroma(file_path)
y = model.predict(feature.reshape(1,12))
ind = numpy.argmax(y)
print(chords[ind])