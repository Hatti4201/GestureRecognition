import pyautogui
import time

print("Press Ctrl+C to stop the script.")
try:
    while True:
        x, y = pyautogui.position()
        # 确保清除行尾的多余字符
        print(f"\rMouse position: ({x}, {y})      ", end="")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nScript stopped.")
