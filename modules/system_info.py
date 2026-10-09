import psutil
import platform
import requests
def get_battery_status():
    battery=psutil.sensors_battery()
    if battery is None:
        return f"Sorry, I couldn't detect a battery on this device"
    percentage=battery.percent
    if battery.power_plugged:
        return f"Your battery is {percentage}% and it is currently charging."
    else:
        return f"Your battery is {percentage}% and it is not charging."

def get_os_info():
    return platform.system()
def get_ram_info():
    return f"RAM usage is {psutil.virtual_memory().percent}%"
def get_cpu_info():
    return platform.processor()
def get_disk_info():
    return f"DISK usage is {psutil.disk_usage('c:\\').percent}%"
def check_internet():
    try:
        response=requests.get("https://www.google.com",timeout=5)
        if response.status_code==200:
            return "Internet connection is available"
        else:
            return "Internet connection is not available"
    except requests.RequestException:
        return"Internet connection is not available"
def get_cpu_usage():
    return f"CPU usage is {psutil.cpu_percent()}%"
