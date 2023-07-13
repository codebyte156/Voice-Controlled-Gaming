import speech_recognition as sr
import os
import pyautogui
import time

text = "XD"



#Here -------------------------------------------------------------------------------

i = 0
while i != 1:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Give Command: ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except:
            print("Sorry, Please speak again")


    if text == "upar":
        pyautogui.press("up")
        print("You said: UP")


    if text == "nichey":
        pyautogui.press("down")
        print("You said: DOWN")


    if text == "daai":
        pyautogui.press("right")
        print("You said: Right")


    if text == "baayi":
        pyautogui.press("left")
        print("You said: Left")


    if text == "you":
        pyautogui.press("up")
        print("You said: UP")


    if text == "down":
        pyautogui.press("down")
        print("You said: DOWN")


    if text == "up":
        pyautogui.press("up")
        print("You said: UP")


    if text == "a":
        pyautogui.press("a")
        print("You said: A")


    if text == "b":
        pyautogui.press("B")
        print("You said: B")

    if text == "c":
        pyautogui.press("c")
        print("You said: c")


    if text == "d":
        pyautogui.press("d")
        print("You said: d")

    if text == "e":
        pyautogui.press("e")
        print("You said: e")


    if text == "1":
        pyautogui.press("1")
        print("You said: 1")



    if text == "1":
        pyautogui.press("1")
        print("You said: 1")


    if text == "2":
        pyautogui.press("2")
        print("You said: 2")


    if text == "3":
        pyautogui.press("3")
        print("You said: 3")


    if text == "doun":
        pyautogui.press("up")
        print("You said: UP")


    if text == "dwon":
        pyautogui.press("up")
        print("You said: UP")

    if text == "left":
        pyautogui.press("left")
        print("You said: LEFT")


    if text == "right":
        pyautogui.press("right")
        print("You said: right")
    
    if text == "tab":
        pyautogui.press("tab")
        print("You said: TAB")
    

    

#Done XD -------------------------------------------------------------------------------









