"""
gtts文字转语音
"""
import fileinput
import os

import librosa
from gtts import gTTS

for line in fileinput.input(os.path.abspath("tag.txt"), inplace=True):
    file_name = "hoolink_" + str(fileinput.lineno()) + ".wav"
    text = file_name + line.rstrip()
    tts = gTTS(text=line.rstrip(), lang='zh-cn')
    tts.save(file_name)
    print(text)

    # 采样率转16K
    y, sr = librosa.load(file_name, sr=None)
    y_16k = librosa.resample(y, sr, 16000)
    librosa.output.write_wav(file_name, y_16k, 16000)
