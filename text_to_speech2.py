import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
#print(voices[0].id)
engine.setProperty("rate",150)
engine.say("Hello how are you")
engine.runAndWait()