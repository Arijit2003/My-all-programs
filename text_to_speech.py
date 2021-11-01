from gtts import gTTS
import os
text1=input("Enter text to speech:")
language="en"
sound=gTTS(text=text1,lang=language,slow=False)
sound.save("play.mp3")
os.system("start play.mp3")
