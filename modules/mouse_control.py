import pyautogui
def move_mouse_center():
    width, height=pyautogui.size()
    x=width//2
    y=height//2
    pyautogui.moveTo(x,y)
    return "Mouse moved to the center."
def click_mouse():
    pyautogui.click()
    return "Mouse clicked."
def double_click():
    pyautogui.doubleClick()
    return "Mouse double clicked."
def get_mouse_position():
    position=pyautogui.position()
    return f"Mouse is at x={position.x},y={position.y}"
def move_mouse(x,y):
    pyautogui.moveTo(x,y)
    return f"Mouse move to x={x},y={y}"
