from modules.system_control import open_application,open_website,close_item,search_web
from modules.information import get_time,get_date,get_user_greeting
from modules.weather import get_weather
from modules.news import get_news
from modules.system_info import get_battery_status,get_os_info,get_ram_info,get_cpu_info,get_disk_info,check_internet,get_cpu_usage
from modules.notes import save_note,read_note,delete_note
from modules.music import play_music
from modules.screenshot import take_screenshot
from modules.password import generate_password
from modules.mouse_control import move_mouse_center,click_mouse,double_click,get_mouse_position,move_mouse
from modules.ai_brain import ask_ai
def process_command(command):
    command=command.lower()
    if command=="hello":
        return "Hello, sunny how can i help you today!"
    elif command=="what is your name":
        return "I am AURA."
    elif command.startswith("open "):
        app_n=command[5:]
        open_application(command)
        open_website(command)
        return "opening "+app_n
    elif command.startswith("close "):
        app_n=command[6:]
        close_item(command)
        return close_item(command)
    elif command.startswith("search "):
        return search_web(command)
    elif "time" in command:
        return get_time()
    elif "date" in command:
        return get_date()
    elif command.startswith("good"):
        return get_user_greeting(command)
    elif "weather" in command:
        words=command.split()
        if "in" in words:
            index=words.index("in")
            city=" ".join(words[index+1:])
            return get_weather(city)
        else:
            return "Please tell me the city name"
    elif "new" in command:
        return get_news()
    elif "battery" in command:
        return get_battery_status()
    elif "take a note" in command:
        return save_note()
    elif "read note" in command:
        return read_note()
    elif "delete note" in command:
        return delete_note()
    elif "which os" in command:
        return get_os_info()
    elif "ram" in command:
        return get_ram_info()
    elif "processor" in command:
        return get_cpu_info()
    elif "disk" in command:
        return get_disk_info()
    elif "internet" in command:
        return check_internet()
    elif "cpu usage" in command:
        return get_cpu_usage()
    elif command.startswith("play "):
        return play_music(command)
    elif "screenshot" in command:
        return take_screenshot()
    elif "generate password" in command:
        return generate_password()
    elif "move mouse to centre" in command:
        return move_mouse_center()
    elif command=="click":
        return click_mouse()
    elif command=="double click":
        return double_click()
    elif "mouse position" in command:
        return get_mouse_position()
    elif command.startswith("move mouse to"):
        parts=command.split()
        x=int(parts[-2])
        y=int(parts[-1])
        return move_mouse(x,y)
        
    else:
        return ask_ai(command)




    