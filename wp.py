import pyautogui as spam
import time

limit = input("kaç kere yazılcağını gir")
msg = input("Bu Kod Python la otomatik yazılmıştır.")

i = 0 

time.sleep(10)

while i<int(limit):
    spam.typewrite(msg)
    spam.press("Enter")

    i+=1