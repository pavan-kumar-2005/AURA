from modules.speak import speak
from modules.commands import process_command
from modules.listen import listen
from modules.information import get_time,get_date,get_current_greeting

print("=" * 40)
print("             AURA v0.1")
print("Artificial Unified Responsive Assisstent")
print("=" * 40)
print("Hello, I am AURA")
speak("Hello, I am AURA")
speak(get_current_greeting())
print("Initializing AURA...")
print("Loading core modules...")
print("Hello! I am AURA. How can I help you today?")
speak(" How can I help you today?")
while True:
    text=listen()
    if text=='exit':
        print("GoodBye sunny! Have a great day")
        speak("GoodBye sunny! Have a great day")
        break
    print("you said:",text)
    response=process_command(text)
    print("AURA:",response)
    speak(response)
print("System Ready.")