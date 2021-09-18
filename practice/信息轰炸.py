#将想说的话放在“信息轰炸.txt”文件中，打开对话框，点一下就行
from pynput.keyboard import Key,Controller
import time
import os
import clipboard



time.sleep(2)
keyboard=Controller()
controlkey=Key.ctrl if os.name=='nt' else Key.cmd

def send_message(msg):
    clipboard.copy(msg)
    with keyboard.pressed(controlkey):
        keyboard.press('v')
    keyboard.press(Key.enter)
    time.sleep(10)
while(1):

 with open('信息轰炸.txt',encoding='utf-8') as f:
        content=f.readlines()
        for x in content:
            if not x.isspace():
                send_message(x.strip())