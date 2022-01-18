from gtts import gTTS
import os

file = open('test.txt', 'r')
myText = file.read().replace("\n", " ")


output = gTTS(myText, lang='en', slow=False)

output.save('output.mp3')
file.close()
os.system('start output.mp3')
