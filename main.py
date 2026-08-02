from modules.speak import speak
from modules.commands import process_command
from modules.listen import listen
print("=" * 40)
print("             AURA v0.1")
print("Artificial Unified Responsive Assisstent")
print("=" * 40)
print("Hello, I am AURA")
print("Initializing AURA...")
print("Loading core modules...")
print("Hello! I am AURA. How can I help you today?")
speak("Hello! I am AURA. How can I help you today?")
while True:
    text=listen()
    if text=='exit':
        print("GoodBye Pavan! Have a great day")
        speak("GoodBye Pavan! Have a great day")
        break
    print("you said:",text)
    response=process_command(text)
    print("AURA:",response)
    speak(response)
print("System Ready.")






