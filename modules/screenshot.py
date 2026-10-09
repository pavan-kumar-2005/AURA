import pyautogui
from datetime import datetime
import os
def take_screenshot():
    os.makedirs("screenshots",exist_ok=True)
    screenshot=pyautogui.screenshot()
    now=datetime.now()
    timestamp=now.strftime("%Y%m%d_%H%M%S")
    filename=f"screenshots/screenshot_{timestamp}.png"
    screenshot.save(filename)
    return f"Screenshot saved as {filename}"