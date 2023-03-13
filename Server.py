import os
from time import sleep
import socket
import webbrowser
import pyautogui
import mouse

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.43.196', 7842))
server.listen(1)
os.system('color 02')
print('Start...')
print('Waiting for connection...')
print('                  #Connected devices#')

while True:
    user, adres = server.accept()
    print('!connected:', adres)
    while True:
        data_1 = user.recv(1024).decode("utf-8").lower()
        print(data_1)

        if data_1 == "r":
            pyautogui.move(20, 0, duration=0.1)

        elif data_1 == "down":
            pyautogui.move(0, 20, duration=0.1)

        elif data_1 == "up":
            pyautogui.move(0, -20, duration=0.1)

        elif data_1 == "l":
            pyautogui.move(-20, 0, duration=0.1)

        elif data_1 == "→":
            pyautogui.move(100, 0, duration=0.1)

        elif data_1 == "↓":
            pyautogui.move(0, 100, duration=0.2)

        elif data_1 == "↑":
            pyautogui.move(0, -100, duration=0.2)

        elif data_1 == "←":
            pyautogui.move(-100, 0, duration=0.2)

        elif data_1 == "↗":
            pyautogui.move(100, -100, duration=0.2)

        elif data_1 == "↙":
            pyautogui.move(-100, 100, duration=0.2)

        elif data_1 == "↖":
            pyautogui.move(-100, -100, duration=0.2)

        elif data_1 == "↘":
            pyautogui.move(100, 100, duration=0.2)



        elif data_1 == "lkm":
            mouse.click(button='left')

        elif data_1 == "pkm":
            mouse.click(button='right')


        elif data_1 == "△ - true":
            pyautogui.keyDown('Up')

        elif data_1 == "△ - false":
            pyautogui.keyUp('Up')

        elif data_1 == "◁ - true":
            pyautogui.keyDown('left')

        elif data_1 == "◁ - false":
            pyautogui.keyUp('left')

        elif data_1 == "▽ - true":
            pyautogui.keyDown('down')

        elif data_1 == "▽ - false":
            pyautogui.keyUp('down')

        elif data_1 == "▷ - false":
            pyautogui.keyUp('right')

        elif data_1 == "▷ - true":
            pyautogui.keyDown('right')





        elif data_1 == "spase - true":
            pyautogui.keyDown('space')

        elif data_1 == "spase - false":
            pyautogui.keyUp('space')

        elif data_1 == "0":
            pyautogui.press("0")

        elif data_1 == "+":
            pyautogui.press("+")

        elif data_1 == "-":
            pyautogui.press("-")

        elif data_1 == "1":
            pyautogui.press("1")

        elif data_1 == "2":
            pyautogui.press("2")

        elif data_1 == "3":
            pyautogui.press("3")

        elif data_1 == "4":
            pyautogui.press("4")

        elif data_1 == "5":
            pyautogui.press("5")

        elif data_1 == "6":
            pyautogui.press("6")

        elif data_1 == "7":
            pyautogui.press("7")

        elif data_1 == "8":
            pyautogui.press("8")

        elif data_1 == "9":
            pyautogui.press("9")

        elif data_1 == "shift - true":
            pyautogui.keyDown("shift")

        elif data_1 == "shift - false":
            pyautogui.keyUp("shift")

        elif data_1 == "f1":
            pyautogui.press("F1")

        elif data_1 == "f2":
            pyautogui.press("F2")

        elif data_1 == "f3":
            pyautogui.press("F3")

        elif data_1 == "f4":
            pyautogui.press("F4")

        elif data_1 == "f5":
            pyautogui.press("F5")

        elif data_1 == "f6":
            pyautogui.press("F6")

        elif data_1 == "f7":
            pyautogui.press("F7")

        elif data_1 == "f8":
            pyautogui.press("F8")

        elif data_1 == "f9":
            pyautogui.press("F9")

        elif data_1 == "f10":
            pyautogui.press("F10")

        elif data_1 == "f11":
            pyautogui.press("F11")

        elif data_1 == "f12":
            pyautogui.press("F12")

        elif data_1 == "tab - true":
            pyautogui.keyDown("tab")

        elif data_1 == "tab - false":
            pyautogui.keyUp("tab")

        elif data_1 == "ctrl":
            pyautogui.press("ctrl")

        elif data_1 == "caps lock":
            pyautogui.press("caps lock")

        elif data_1 == "esc":
            pyautogui.press("ESC")

        elif data_1 == "enter":
            pyautogui.press("enter")

        elif data_1 == "del":
            pyautogui.press("delete")

        elif data_1 == "alt - true":
            pyautogui.keyDown("alt")

        elif data_1 == "alt - false":
            pyautogui.keyUp("alt")

        elif data_1 == "+lkm - true":
            pyautogui.mouseDown(button='left')

        elif data_1 == "+lkm - false":
            pyautogui.mouseUp(button='left')

        elif data_1 == "+pkm - true":
            pyautogui.mouseDown(button='right')

        elif data_1 == "+pkm - false":
            pyautogui.mouseUp(button='right')

        #3

        elif data_1 == "spotify":
            webbrowser.open("https://open.spotify.com/collection/tracks")

        elif data_1 == "game":
            os.startfile("C:/Users/студент.BestLaptop-ПК/AppData/Roaming/.minecraft/TLauncher.exe")

        elif data_1 == "":
            quit()
