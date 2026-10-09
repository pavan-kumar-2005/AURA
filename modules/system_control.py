import os
import webbrowser
import psutil
from datetime import datetime
apps = {
    "notepad": {
        "open": "notepad.exe",
        "close": "Notepad.exe"
    },
    "calculator": {
        "open": "calc.exe",
        "close": "CalculatorApp.exe"
    },
    "paint": {
        "open": "mspaint.exe",
        "close": "mspaint.exe"
    },
    "wordpad": {
        "open": "write.exe",
        "close": "write.exe"
    },
    "command prompt": {
        "open": "cmd.exe",
        "close": "cmd.exe"
    },
    "powershell": {
        "open": "powershell.exe",
        "close": "powershell.exe"
    },
    "file explorer": {
        "open": "explorer.exe",
        "close": "explorer.exe"
    },
    "task manager": {
        "open": "taskmgr.exe",
        "close": "Taskmgr.exe"
    },
    "control panel": {
        "open": "control.exe",
        "close": "control.exe"
    },
    "device manager": {
        "open": "devmgmt.msc",
        "close": "mmc.exe"
    },
    "registry editor": {
        "open": "regedit.exe",
        "close": "regedit.exe"
    },
    "services": {
        "open": "services.msc",
        "close": "mmc.exe"
    },
    "system configuration": {
        "open": "msconfig.exe",
        "close": "msconfig.exe"
    },
    "disk management": {
        "open": "diskmgmt.msc",
        "close": "mmc.exe"
    },
    "character map": {
        "open": "charmap.exe",
        "close": "charmap.exe"
    },
    "snipping tool": {
        "open": "snippingtool.exe",
        "close": "SnippingTool.exe"
    },
    "magnifier": {
        "open": "magnify.exe",
        "close": "Magnify.exe"
    },
    "on screen keyboard": {
        "open": "osk.exe",
        "close": "osk.exe"
    },
    "remote desktop": {
        "open": "mstsc.exe",
        "close": "mstsc.exe"
    },
    "chrome": {
        "open": "chrome.exe",
        "close": "chrome.exe"
    },
    "edge": {
        "open": "msedge.exe",
        "close": "msedge.exe"
    },
    "opera": {
        "open": "opera.exe",
        "close": "opera.exe"
    },
    "visual studio code": {
        "open": "code",
        "close": "Code.exe"
    },
    "vscode": {
        "open": "code",
        "close": "Code.exe"
    },
    "discord": {
        "open": "discord.exe",
        "close": "Discord.exe"
    },
    "telegram": {
        "open": "telegram.exe",
        "close": "Telegram.exe"
    },
    "zoom": {
        "open": "zoom.exe",
        "close": "Zoom.exe"
    }
}
websites = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "github": "https://github.com",
    "chatgpt": "https://chatgpt.com",
    "gmail": "https://mail.google.com",
    "linkedin": "https://www.linkedin.com",
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "twitter": "https://x.com",
    "reddit": "https://www.reddit.com",
    "stackoverflow": "https://stackoverflow.com",
    "leetcode": "https://leetcode.com",
    "hackerrank": "https://www.hackerrank.com",
    "geeksforgeeks": "https://www.geeksforgeeks.org",
    "w3schools": "https://www.w3schools.com",
    "coursera": "https://www.coursera.org",
    "udemy": "https://www.udemy.com",
    "netflix": "https://www.netflix.com",
    "amazon": "https://www.amazon.in",
    "flipkart": "https://www.flipkart.com",
    "spotify": "https://open.spotify.com",
    "whatsapp": "https://web.whatsapp.com",
    "amazon prime": "https://www.primevideo.com"
}
def extract_name(command):
    words=command.split()
    return " ".join(words[1:])
    
def open_application(app_name):
    name=extract_name(app_name)
    exe=apps.get(name)
    if exe:
         os.startfile(exe["open"])
    else:
        return "Application not found"
def open_website(web_name):
    name=extract_name(web_name)
    exe=websites.get(name)
    if exe:
        webbrowser.open(exe)
    else:
        return "Website not found"

def close_item(command):
    name=extract_name(command)
    exe=apps.get(name)
    if exe:
        target=exe["close"]
        closed=False
        for process in psutil.process_iter():
            # print(process.name())
            # if "chrome" in process.name().lower():
            #     print(process.name())
            if process.name().lower()==target.lower():
                process.terminate()
                closed=True
                # return "Application closed"
        if closed:
            return "Application closed"
        else:
            return "Application is not running"
    else:
        return "Application not found"

search_engines = {
    "google": "https://www.google.com/search?q=",
    "youtube": "https://www.youtube.com/results?search_query=",
    "github": "https://github.com/search?q=",
    "stackoverflow": "https://stackoverflow.com/search?q=",
    "geeksforgeeks": "https://www.geeksforgeeks.org/?s=",
    "wikipedia": "https://en.wikipedia.org/wiki/Special:Search?search="
}
def search_web(command):
    words=command.split()
    platform=words[-1]
    query=" ".join(words[1:-2])
    search=search_engines.get(platform)
    if search:
        url=search+query
        webbrowser.open(url)
        return "Searching " + query + " on " + platform
    else:
        return " Search engine not found"


