import pyautogui
from python_imagesearch.imagesearch import *
import time


selectscreenimg = './Resimler/champselect.png'
iconimg = './Resimler/icon.png'
kabulimg = './Resimler/kabulbutton.png'
iptal1img = './Resimler/iptal1.png'
iptal2img = './Resimler/iptal2.png'



def isCancelled(): #oyun iptal oldu mu
    kabul = imagesearch(kabulimg)
    iptal1 = imagesearch(iptal1img)
    iptal2 = imagesearch(iptal2img)

    if kabul[0] == -1 and (iptal1[0] != -1 or iptal2[0] != -1):
        return True
    else:
        return False




def gameAccept(): #kabul butonu arama / kabul etme
    pos = imagesearch_loop(kabulimg, 1)
    pyautogui.click(pos[0], pos[1])
    print("Oyun bulundu")
    




def isChampSelect(): #şampiyon seçim ekranına girdi mi
    slcscreen = imagesearch(selectscreenimg)
    icon = imagesearch(iconimg)

    if not slcscreen[0] == -1 or not icon[0] == -1:
        return True
    else:
        return False

def main():
    run = True
    while(run):
        gameAccept()
        pyautogui.move(0,-300)
        while(True):
            iptal = isCancelled()
            if iptal:
                print("Oyun iptal edildi. Tekrar deneniyor...")
                break

            csResult = isChampSelect()

            if csResult:
                print("Program kapatılıyor...")
                run = False
                break

            time.sleep(1)

main()
            
                
        



