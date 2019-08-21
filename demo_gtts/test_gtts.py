from gtts import gTTS
import os

for line in open(os.path.abspath("tag.txt")):
    text = line.split()
    tts = gTTS(text=text[1], lang='zh-cn')
    tts.save(text[0])
    print("命令[" + text[1] + "]转换完成")
