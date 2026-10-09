from datetime import datetime

def get_time():
    now=datetime.now()
    return "The current time is " + now.strftime("%I:%M:%p")

def get_date():
    now=datetime.now()
    date=now.strftime("%A, %d %B %Y")
    return "Today is "+ date

def get_current_greeting():
    now=datetime.now()
    hour=now.hour
    if 5<=hour<12:
        return "Good Morning, Sunny!"
    elif 12<=hour<17:
        return "Good Afternoon,Sunny!"
    elif 17<=hour<21:
        return "Good evening, Sunny!"
    else:
        return "Good Night, Sunny!."

def get_user_greeting(command):
    if "morning" in command:
        return "Good Morning, Sunny! Have a wonderful day."

    elif "afternoon" in command:
        return "Good Afternoon, Sunny!"
    
    elif "evening" in command:
        return "Good Evening, Sunny!"
    
    elif "night" in command:
        return "Good Night, Sunny! Take care."
    
    else:
        return "Hello, Sunny!"

