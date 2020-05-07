import pyautogui
from python_imagesearch.imagesearch import *
import time

chatimg = './Resimler/chat.png'

lane = int(input("Select a lane:\n\n1: TOP \n2: JUNGLE \n3: MID \n4: ADC \n5: SUPPORT\n6: BOT PRE\n"))
if lane == 1:
    lane = "top"
if lane == 2:
    lane = "jung"
if lane == 3:
    lane = "mid"
if lane == 4:
    lane = "adc"
if lane == 5:
    lane = "sup"
if lane == 6:
    lane = "bot pre"

import match_accepter_v2

def ChatClick():
    chatpos = imagesearch_loop(chatimg, 0.1)
    pyautogui.click(chatpos[0]+90, chatpos[1]+20)
    
ChatClick()

for i in range(4):
    pyautogui.write('{}'.format(lane))
    pyautogui.press('enter')
        
