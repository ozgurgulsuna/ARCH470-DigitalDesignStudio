import pyautogui
import time
from pynput import keyboard

def on_press(key):
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    #print('Key pressed: ' + k)
    if k=="+":
        exit()

listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
#listener.join()  # remove if main thread is polling self.keys

time.sleep(10)
for i in range(600,950):
    pyautogui.click(x=310, y=473,button='left',clicks=2)
    pyautogui.write(str(i))
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=1859, y=964,button='left')
    time.sleep(30)
    pyautogui.click(x=-1102, y=75,button='left')
    time.sleep(7)
    pyautogui.click(x=-1490, y=75,button='left')
    time.sleep(2)
    pyautogui.write("final_render_2_"+str(i)+"_")
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(x=-31, y=23,button='left')
    time.sleep(2)
#while(1):
#    time.sleep(1)
#    x, y = pyautogui.position()
#    print(x,y)

#pyautogui.write(str(i))
#pyautogui.press('enter')
#pyautogui.click(x=100, y=200,button='left',clicks=2) 

