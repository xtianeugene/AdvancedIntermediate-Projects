import pyautogui

def capture(filename="screenshot.png"):
    pyautogui.screenshot(filename)
    print("Saved", filename)

if __name__ == "__main__":
    capture()