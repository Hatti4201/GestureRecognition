import paths
import subprocess
import time
import pyautogui
import coordinates

def launch_and_select_mode(software_path, mode):
    """
    启动 Gesture EVK 软件并选择动态或静态手势模式。
    :param software_path: Gesture EVK 软件路径
    :param mode: '动态' 或 '静态'
    """
    try:
        # 启动 Gesture EVK 软件
        process = subprocess.Popen([software_path], shell=True)
        print("Gesture EVK is active, loading... \n软件已启动，等待程序准备...")
        time.sleep(5)  # 等待软件加载完毕

        # 根据选择的模式进行操作
        if mode == 'D':
            print("Dynamic gesture mode is configuring \n正在配置动态手势模式...")
            # 点击并选择下拉菜单中的 "GESTURE_VL53L8"
            pyautogui.moveTo(*coordinates.button1)  # 根据实际位置调整坐标
            pyautogui.click()
            time.sleep(0.1)
            
            pyautogui.moveTo(*coordinates.button2)  # 根据实际位置调整坐标
            pyautogui.click()
            time.sleep(0.1)


            # 点击 "Start ranging" 按钮
            pyautogui.moveTo(*coordinates.button3)  # 根据实际位置调整坐标
            pyautogui.click()
            time.sleep(2)

            # 打开 "Gesture Detection" 模块
            pyautogui.moveTo(*coordinates.button4)  # 左下角加号图标位置，根据实际位置调整坐标
            pyautogui.click()
            time.sleep(0.1)

            pyautogui.moveTo(*coordinates.button5)  # 左下角加号图标位置，根据实际位置调整坐标
            pyautogui.click()
            time.sleep(0.1)
            
            print("The dynamic gesture mode has been configured and activated.已配置并打开动态手势模式。")
        
        elif mode == 'S':
            print("configuring static gesture mode\n正在配置静态手势模式...")
            # 点击并选择下拉菜单中的 "GESTURE_VL53L8"
            pyautogui.moveTo(*coordinates.button11)  # 根据实际位置调整坐标
            pyautogui.click()
            time.sleep(0.1)
            
            pyautogui.moveTo(*coordinates.button12)  # 根据实际位置调整坐标
            pyautogui.click()
            time.sleep(0.1)


            # 点击 "Start ranging" 按钮
            pyautogui.moveTo(*coordinates.button13)  # 根据实际位置调整坐标
            pyautogui.click()
            time.sleep(2)

            # 打开 "Gesture Detection" 模块
            pyautogui.moveTo(*coordinates.button14)  # 左下角加号图标位置，根据实际位置调整坐标
            pyautogui.click()
            time.sleep(0.1)

            pyautogui.moveTo(*coordinates.button15)  # 左下角加号图标位置，根据实际位置调整坐标
            pyautogui.click()
            time.sleep(0.1)
            
            print("The static gesture mode has been configured and activated.\n已配置并打开静态手势模式。")
        
        else:
            print("invalid mode, please type in D or S \n无效模式。请输入 '动态' 或 '静态'。")

    except Exception as e:
        print(f"操作时出错: {e}")

if __name__ == '__main__':
    software_path = paths.software_path
    mode = input("choose the mode(D\S) \n请输入模式:").strip()
    launch_and_select_mode(software_path, mode)

