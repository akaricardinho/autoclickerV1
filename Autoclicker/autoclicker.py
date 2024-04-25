#Librarays
from tkinter import *
import time 
import pyautogui as pgui
import threading

KeyAutoclicker = False
MouseAutoclicker = False


#Functions
def startAutoClicker1():

    global KeyAutoclicker
    KeyAutoclicker = True
    buttonStartKey.config(text="Stop AutoClicker", command=stopAutoClicker1)
    keyEntry.config(state="disabled")
    cooldownEntry.config(state="disabled")
    hotkey = keyEntry.get()
    cooldown = float(cooldownEntry.get())

    def autoClickerThread():
        while KeyAutoclicker:
            pgui.keyDown(hotkey)
            time.sleep(cooldown)
            pgui.keyUp(hotkey)

    threading.Thread(target=autoClickerThread).start()

def stopAutoClicker1():
    global KeyAutoclicker
    KeyAutoclicker = False
    print(KeyAutoclicker, "AutoClicker Stopped")
    buttonStartKey.config(text=("Start AutoClicker"), command=startAutoClicker1)
    keyEntry.config(state="normal")
    cooldownEntry.config(state="normal")

def startAutoClicker2():
    print("clicked")

#Main Window
window = Tk()
window.title("AutoClickerV1")
window.geometry("250x250")

labelKey = Label(window, text="Hotkey", foreground="blue")
labelKey.grid(column=0, row=0, pady=5)
keyEntry = Entry(window)
keyEntry.grid(column=1, row=0)

labelCooldown = Label(window, text="Cooldown", foreground="blue", )
labelCooldown.grid(column=0, row=1, pady=5)
cooldownEntry = Entry(window)
cooldownEntry.grid(column=1, row=1)


buttonStartKey = Button(window, text="Start Key Autoclicker", command=startAutoClicker1)
buttonStartKey.grid(column=1, row=2, pady=50)

buttonStartMouse = Button(window, text="Start Mouse Autoclicker", command=startAutoClicker2)
buttonStartMouse.grid(column=1, row=3)


#buttonStart = Button(window, text="Start Mouse Autoclicker", command=startMouseAutoClicker)
#buttonStart.grid(column=1, row=3)


window.resizable(False,False)
window.mainloop()

