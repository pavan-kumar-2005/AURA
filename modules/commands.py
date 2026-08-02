
def process_command(command):
    command=command.lower()
    if command=="hello":
        return "Hello, Pavan how can i help you today!"
    elif command=="what is your name":
        return "I am AURA."
    else:
        return "I am not yet integrated with LLM"
    