import soundfile as sf
import csv
import numpy as np
import matplotlib.pyplot as plt
don, samplerate = sf.read("don.wav")
print(samplerate)
# first = sf.read('don.wav', stop=100)
last = sf.read('don.wav', start=-100)
print(last)
# print(don.shape)
plt.plot(don)
plt.show()
