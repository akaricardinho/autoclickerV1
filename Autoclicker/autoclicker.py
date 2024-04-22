#Libraraysaa
from tkinter import *
import time 
import pyautogui as pgui
import threading

Autoclicker = False

#Functions
def startAutoClicker():
    global Autoclicker
    Autoclicker = True
    buttonStart.config(text="Stop AutoClicker", command=stopAutoClicker)
    keyEntry.config(state="disabled")
    cooldownEntry.config(state="disabled")
    hotkey = keyEntry.get()
    cooldown = int(cooldownEntry.get())

    def autoClickerThread():
        while Autoclicker:
            pgui.press(hotkey)
            time.sleep(cooldown)

    threading.Thread(target=autoClickerThread).start()

def stopAutoClicker():
    global Autoclicker
    Autoclicker = False
    print(Autoclicker, "AutoClicker Stopped")
    buttonStart.config(text=("Start AutoClicker"), command=startAutoClicker)
    keyEntry.config(state="normal")
    cooldownEntry.config(state="normal")

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


buttonStart = Button(window, text="Start Autoclicker", command=startAutoClicker)
buttonStart.grid(column=1, row=2, pady=50)


window.resizable(False,False)
window.mainloop()

