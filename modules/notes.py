import os
from modules.listen import listen
from modules.speak import speak

def save_note():
    speak("What would you like me to write?")
    note =listen()
    with open("notes.txt",'a') as file:
        file.write(note + "\n")
    # speak("Your note has been saved successfully.")
    return "Your note has been saved successfully."

def read_note():
    try:
        with open("notes.txt",'r') as file:
            notes=file.read()
            return notes
    except:
        return "File not exist."

def delete_note():
    try:
        os.remove("notes.txt")
        return "All notes have been deleted."
    except:
        return "There ar no notes to delet."