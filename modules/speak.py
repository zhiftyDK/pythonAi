import pyttsx3
def speak(input):
    engine = pyttsx3.init()
    engine.setProperty("rate", 125)
    engine.say(input)
    engine.runAndWait()
