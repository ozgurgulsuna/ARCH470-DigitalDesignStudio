import os
 
# specify your path of directory
path = r"G:\RENDER ALL\FURKAN\STAGE-2"

directories = os.listdir( path )

import pyautogui
import time
from pynput import keyboard
exitflag=0
def on_press(key):
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    #print('Key pressed: ' + k)
    if k=="+":
        global exitflag
        exitflag=1

listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
#listener.join()  # remove if main thread is polling self.keys
b=0
time.sleep(5)
k=0
for i in range(900,1200):
    for file in directories:
        if file=="final_render_2_"+str(i)+"_.jpg":
            b=1
    if b:
        b=0
        continue
    print(i)
    k=k+1
    continue

for i in range(900,1200):
    for file in directories:
        if file=="final_render_2_"+str(i)+"_.jpg":
            b=1
    if b:
        b=0
        continue
    print("working on",i,"and",k,"items left")
    #continue
    
    if exitflag==1:
        break
    pyautogui.click(x=350, y=400,button='left',clicks=2) #SLIDER
    pyautogui.write(str(i))
    pyautogui.press('enter')
    time.sleep(3)
    if exitflag==1:
        break
    pyautogui.click(x=1859, y=964,button='left')
    time.sleep(45)
    if exitflag==1:
        break
    pyautogui.click(x=-1095, y=67,button='left')
    time.sleep(10)
    if exitflag==1:
        break
    pyautogui.click(x=-1485, y=67,button='left')
    time.sleep(3)
    if exitflag==1:
        break
    pyautogui.write("final_render_2_"+str(i)+"_")
    pyautogui.press('enter')
    time.sleep(3)
    if exitflag==1:
        break
    pyautogui.click(x=-25, y=14,button='left')
    time.sleep(3)
    k=k-1
#while(1):
#    time.sleep(1)
#    x, y = pyautogui.position()
#    print(x,y)

#pyautogui.write(str(i))
#pyautogui.press('enter')
#pyautogui.click(x=100, y=200,button='left',clicks=2) 

