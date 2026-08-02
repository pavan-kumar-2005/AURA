from modules.listen import listen
from modules.speak import speak
speak("hello pavan")
text=listen()
print(text)
speak("you said"+ text)