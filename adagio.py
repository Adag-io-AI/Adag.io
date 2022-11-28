import os
from keras.models import load_model
import pathlib
import h5py
import numpy
import librosa
import librosa.display
import tkinter
import pyaudio
# import wave
import time
import threading


# def print_chord():

class audio_input(object):
    def __init__(self):
        self.FORMAT = pyaudio.paFloat32
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024 * 16
        self.p = None
        self.stream = None

    def start_listening(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  output=False,
                                  stream_callback=self.get_chroma,
                                  frames_per_buffer=self.CHUNK)

    def stop_listening(self):
        self.stream.close()
        self.p.terminate()

    def get_chroma(self, in_data, frame_count, time_info, flag):
        audio_array = numpy.frombuffer(in_data, dtype=numpy.float32)
        # print(audio_array)
        y_harm = librosa.effects.harmonic(y=audio_array, margin=4)
        chroma = librosa.feature.chroma_cqt(y=y_harm, sr=self.RATE, fmin=65.4, threshold=.4, n_chroma=12)
        chroma_array = numpy.array(chroma)
        chroma_mean = chroma_array.mean(axis=1)
        if chroma_mean.mean(axis=0) < .1:
            return None, pyaudio.paContinue
        y = model.predict(chroma_mean.reshape(1, 12))
        ind = numpy.argmax(y)
        change_chord(chords[ind])
        print(chords[ind])
        # return chroma_mean
        time.sleep(.5)
        return None, pyaudio.paContinue

    def loop(self):
        while (
        self.stream.is_active()):  # if using button you can set self.stream to 0 (self.stream = 0), otherwise you can use a stop condition
            time.sleep(2.0)


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


def stopping(audio):
    text.configure(text="Press to start", font=("Arial Bold", 18))
    change_chord("")
    audio.stop_listening()
    start.configure(text="start", command=starting)


def starting():
    text.configure(text="Starting...", font=("Arial Bold", 18))
    audio = audio_input()
    start.configure(text="stop", command=lambda: stopping(audio))
    audio.start_listening()
    audio.loop()


def change_chord(txt):
    labelText.set(txt)


model = load_model('test_model2.h5')
dataset = 'dataset'
data_dir = pathlib.Path(dataset)
chords = []
for name in os.listdir(dataset):
    chords.append(name)

box = tkinter.Tk()
box.geometry('400x200')
box.title("Adag.io")
text = tkinter.Label(box, text="Press to start", font=("Arial Bold", 18))
text.grid(column=5, row=0)
start = tkinter.Button(box, text="start", command=threading.Thread(target=starting).start)
start.grid(column=5, row=5)
labelText = tkinter.StringVar()
chord = tkinter.Label(box, font=("Arial Bold", 12), textvariable=labelText)
chord.grid(column=6, row=5)
piano = tkinter.Label(box, text=" .......................................................... \n"
                                "::.....G###?...?###5.....^^....:B###7...J###Y...!###B:....:^\n"
                                "::     #@@@?   ?@@@P     ::    .&@@@7   Y@@@5   !@@@&.    .^\n"
                                "::     #@@@?   ?@@@P     ::    .&@@@7   Y@@@Y   !@@@&:    .^\n"
                                "::     #@@@?   ?@@@P     ::    .&@@@7   Y@@@Y   !@@@&:    .^\n"
                                "::     #@@@?   ?@@@P     ::    .&@@@7   Y@@@Y   !@@@&:    .^\n"
                                "::     #@@@?   ?@@@P     ::    .&@@@7   Y@@@Y   !@@@&:    .^\n"
                                "::     #@@@?   ?@@@P     ::    .&@@@7   Y@@@5   !@@@@:    .^\n"
                                "::     J5P5~   ~5P57     ::    .Y5P5^   !5P5!   ^555Y.    .^\n"
                                "::       ^       ^       ::       ^       ^       :.      .^\n"
                                "::       ^       ^       ::      .^       ^       ::      .^\n"
                                "::       ^       ^       ::      .^       ^       ::      .^\n"
                                "::       ^       ^       ::      .^       ^       ::      .^\n"
                                ":: ......~.......~...... :^ ......~ ......~...... ^: .....:^\n"
                                " .................................:.........................",
                      font=("Consolas", 6))
piano.grid(column=5, row=8)

box.mainloop()
