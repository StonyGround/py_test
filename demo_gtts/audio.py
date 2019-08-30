import os
import wave
import librosa

path = os.path.abspath("hoolink_24.wav")
# with wave.open(path, "rb") as f:
y, sr = librosa.load(path, sr=None)
# librosa.resample(y, sr, 16000)
print(sr)
print(y.shape)
