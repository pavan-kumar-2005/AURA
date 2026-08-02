import speech_recognition as sr
recognizer=sr.Recognizer()
def listen():
    with sr.Microphone() as source:
        print("Listening....")
        audio=recognizer.listen(source)
        try:
            text=recognizer.recognize_google(audio)
            return text
        except:
            print("Sorry, I couldn't understand")
            return ""