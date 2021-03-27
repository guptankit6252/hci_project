import pyautogui
import speech_recognition as speech
import webbrowser as wb
import re
import requests


def voice_recogniser():

    r = speech.Recognizer()
    r.energy_threshold = 7000

    with speech.Microphone() as source:
        print()
        print("Please Speak:")
        input_audio = r.listen(source)
        print("Processing...")

    try:
        source = r.recognize_google(input_audio).lower()
        print(source)

    except:
        print("Sorry! Could not understand! Try Again")
        action()

    return source


def action():

    source = voice_recogniser()

    if "left" in source:
        left(source)

    elif "scroll up" in source:
        scroll_up()

    elif "scroll down" in source:
        scroll_down()

    elif source == "right click":
        right_click()

    elif "right" in source or "write" in source:
        right(source)

    elif "browser" in source or "visit" in source or "goto" in source or "go to" in source:
        website()

    elif "search" in source or "google" in source or "find" in source:
        search()

    elif "up" in source or "above" in source or "go up" in source:
        up(source)

    elif "down" in source or "below" in source or "go down" in source:
        down(source)

    elif "type" in source:
        type()

    elif "double click" in source or "double" in source:
        double_click()

    elif "left click" in source or "click" in source or "press" in source:
        left_click()

    elif "exit" in source or "quit" in source or "leave" in source or "bye" in source:
        quit()

    elif "help" in source or "assistance" in source:
        help()

    else:
        print("Incorrect Command Spoken. Please Try Again.")
        action()


def left(source):

    if "adjust" in source:
        pyautogui.moveRel(-1, 0, 0.5)

    else:
        if "one" in source or "1" in source:
            pyautogui.moveRel(-11, 0, 0.5)

        elif "two" in source or "2" in source:
            pyautogui.moveRel(-45, 0, 0.5)

        elif "three" in source or "3" in source:
            pyautogui.moveRel(-90, 0, 0.5)

        elif "four" in source or "4" in source:
            pyautogui.moveRel(-180, 0, 0.5)

        elif "five" in source or "5" in source:
            pyautogui.moveRel(-360, 0, 0.5)

        elif "full" in source or "entire" in source or "whole" in source:
            pyautogui.moveTo(-1 * pyautogui.size()[0], pyautogui.position()[1])

        else:
            pyautogui.moveRel(-90, 0, 0.5)

    action()


def right(source):

    if "adjust" in source:
        pyautogui.moveRel(1, 0, 0.5)

    else:
        if "one" in source or "1" in source:
            pyautogui.moveRel(11, 0, 0.5)

        elif "two" in source or "2" in source:
            pyautogui.moveRel(45, 0, 0.5)

        elif "three" in source or "3" in source:
            pyautogui.moveRel(90, 0, 0.5)

        elif "four" in source or "4" in source:
            pyautogui.moveRel(180, 0, 0.5)

        elif "five" in source or "5" in source:
            pyautogui.moveRel(45, 0, 0.5)

        elif "full" in source or "entire" in source or "whole" in source:
            pyautogui.moveTo(pyautogui.size()[0], pyautogui.position()[1])

        else:
            pyautogui.moveRel(90, 0, 0.5)

    action()


def up(source):

    if "adjust" in source:
        pyautogui.moveRel(0, -1, 0.5)

    else:
        if "one" in source or "1" in source:
            pyautogui.moveRel(0, -11, 0.5)

        elif "two" in source or "2" in source:
            pyautogui.moveRel(0, -45, 0.5)

        elif "three" in source or "3" in source:
            pyautogui.moveRel(0, -90, 0.5)

        elif "four" in source or "4" in source:
            pyautogui.moveRel(0, -180, 0.5)

        elif "five" in source or "5" in source:
            pyautogui.moveRel(0, -360, 0.5)

        elif "full" in source or "entire" in source or "whole" in source:
            pyautogui.moveTo(pyautogui.position()[0], 0)

        else:
            pyautogui.moveRel(0, -90, 0.5)

    action()


def down(source):

    if "adjust" in source:
        pyautogui.moveRel(0, 1, 0.5)

    else:
        if "one" in source or "1" in source:
            pyautogui.moveRel(0, 11, 0.5)

        elif "two" in source or "2" in source:
            pyautogui.moveRel(0, 45, 0.5)

        elif "three" in source or "3" in source:
            pyautogui.moveRel(0, 90, 0.5)

        elif "four" in source or "4" in source:
            pyautogui.moveRel(0, 180, 0.5)

        elif "five" in source or "5" in source:
            pyautogui.moveRel(0, 360, 0.5)

        elif "full" in source or "entire" in source or "whole" in source:
            pyautogui.moveTo(pyautogui.position()[0], pyautogui.size()[1])

        else:
            pyautogui.moveRel(0, 90, 0.5)

    action()


def type_text_input():

    r = speech.Recognizer()
    r.energy_threshold = 7000

    with speech.Microphone() as source:
        print()
        print("Please speak the text to be typed. Say \"stop typing\" or \"exit typing\" to exit the type mode.")
        input_audio = r.listen(source)
        print("Processing...")

    try:
        source = r.recognize_google(input_audio).lower()
        print(source)
        return source

    except:
        print("Sorry! Could not understand! Please speak again to type: ")
        type()


def type():

    type_text = type_text_input()

    if "exit typing" in type_text or "stop typing" in type_text or "stop writing" in type_text or "stop writing" in type_text:
        print("Exiting typing")
        action()

    else:
        pyautogui.click(pyautogui.position())
        pyautogui.typewrite(type_text, 1)
        type()


def double_click():

    pyautogui.doubleClick(None, None)
    action()


def left_click():

    pyautogui.click(None, None)
    action()


def right_click():

    pyautogui.rightClick(None, None)
    action()


def scroll_up():
    # print("UP")
    pyautogui.scroll(100)
    action()


def scroll_down():
    # print("DOWN")
    pyautogui.scroll(-100)
    action()


def search_input():

    r = speech.Recognizer()
    r.energy_threshold = 7000

    with speech.Microphone() as source:
        print()
        print("Please speak the text to be searched:")
        input_audio = r.listen(source)
        print("Processing...")

    try:
        source = r.recognize_google(input_audio).lower()
        print(source)
        return source

    except:
        print("Sorry! Could not understand! Try saying the search query again")
        search()


def search():

    query = search_input()
    website = "https://www.google.co.in/search?q=" + query
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    try:
        wb.get(chrome_path).open(website)
        action()
    except:
        print("Sorry. This application requires Chrome to be installed and configured properly. Please install / configure Chrome properly.")
        action()


def website_input():

    r = speech.Recognizer()
    r.energy_threshold = 7000

    with speech.Microphone() as source:
        print()
        print("Please speak the address of the website:")
        input_audio = r.listen(source)
        print("Processing")

    try:
        source = r.recognize_google(input_audio).lower()
        print(source)
        return source

    except:
        print("Sorry! Could not understand! Try saying the website name again")
        website()


def website():

    url = website_input()
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    try:
        wb.get(chrome_path).open(url)
        action()
    except:
        print("Sorry. This application requires Chrome to be installed and configured properly. Please install / configure Chrome properly.")
        action()


def quit():

    print("Thank You!")
    print("Exiting Program...")


def help():

    print("Developed by Rochan\n")
    print("List of available commands:")
    print("Left")
    print("Right")
    print("Up")
    print("Down")
    print("Type")
    print("Double Click")
    print("Left Click")
    print("Right Click")
    print("Scroll Up")
    print("Scroll Down\n")
    print("Browser")
    print("Search\n")
    print("To exit, please say \"Quit\" or \"Exit\"")
    print("To view the list of all available commands, please say \"Help\"")
    print("To view detailed information about each command, please type command_name")
    print("To go back to the main interface, press Q.")
    source = input().lower()

    if source == "right":
        help_right()
    elif source == "left":
        help_left()
    elif source == "up":
        help_up()
    elif source == "down":
        help_down()
    elif source == "type":
        help_type()
    elif source == "double click" or source == "doubleclick":
        help_double_click()
    elif source == "click" or source == "left click" or source == "leftclick":
        help_left_click()
    elif source == "right click" or source == "rightclick":
        help_right_click()
    elif source == "scroll up" or source == "scrollup":
        help_scroll_up()
    elif source == "scroll down" or source == "scrolldown":
        help_scroll_down()
    elif "visit" in source or "website" in source or "browser" in source:
        help_website()
    elif "search" in source or "query" in source or "google" in source:
        help_search()
    elif source == "exit" or source == "quit" or source == "leave":
        help_exit()
    elif source == "q":
        action()
    else:
        print("Incorrect Command Entered. Please Try Again.")
        help()


def help_left():

    print("This command moves the mouse left.")
    print("To move the mouse by 11 pixels to the Left, you can say \"Left One\.")
    print("To move the mouse by 45 pixels to the Left, you can say \"Left Two\".")
    print("To move the mouse by 90 pixels to the Left, you can say \"Left Three\".")
    print("To move the mouse by 180 pixels to the Left, you can say ting\"Left Four\".")
    print("To move the mouse by 360 pixels to the Left, you can say \"Left Five\".")
    print("To adjust the mouse pointer in case it is misaligned, you can say \"Adjust Mouse Left\".")
    print("To go back to the main interface, press Enter.")
    input()
    action()


def help_right():

    print("This command moves the mouse Right.")
    print("To move the mouse by 11 pixels to the Right, you can say \"Right One\".")
    print("To move the mouse by 45 pixels to the Right, you can say \"Right Two\".")
    print("To move the mouse by 90 pixels to the Right, you can say \"Right Three\".")
    print("To move the mouse by 180 pixels to the Right, you can say \"Right Four\".")
    print("To move the mouse by 360 pixels to the Right, you can say \"Right Five\".")
    print("To adjust the mouse pointer in case it is misaligned, you can say \"Adjust Mouse Right\".")
    print("To go back to the main interface, press Enter.")
    input()
    action()


def help_up():

    print("This command moves the mouse Upwards.")
    print("To move the mouse by 11 pixels Upwards, you can say \"Up One\".")
    print("To move the mouse by 45 pixels Upwards, you can say \"Up Two\".")
    print("To move the mouse by 90 pixels Upwards, you can say \"Up Three\".")
    print("To move the mouse by 180 pixels Upwards, you can say \"Up Four\".")
    print("To move the mouse by 360 pixels Upwards, you can say \"Up Five\".")
    print("To adjust the mouse pointer in case it is misaligned, you can say \"Adjust Mouse Up\".")
    print("To go back to the main interface, press Enter.")
    input()
    action()


def help_down():

    print("This command moves the mouse Downwards.")
    print("To move the mouse by 11 pixels Downwards, you can say \"Down One\".")
    print("To move the mouse by 45 pixels Downwards, you can say \"Down Two\".")
    print("To move the mouse by 90 pixels Downwards, you can say \"Down Three\".")
    print("To move the mouse by 180 pixels Downwards, you can say \"Down Four\".")
    print("To move the mouse by 360 pixels Downwards, you can say \"Down Five\".")
    print("To adjust the mouse pointer in case it is misaligned, you can say \"Adjust Mouse Down\".")
    print("To go back to the main interface, press Enter.")
    input()
    action()


def help_type():

    print("This command can be used to type text into a textbox on the screen.")
    print("When the prompt appears, speak the text you want to type.")
    print("To stop typing, you can say \"Stop Typing\".")
    print("To go back to the main interface, press Enter.")
    input()
    action()


def help_double_click():

    print("This command is used to double click the mouse.")
    print("The action will be performed at the current location of the mouse.")
    print("To go back to the main interface, press Enter.")
    input()
    action()


def help_left_click():

    print("This command is used to left click the mouse.")
    print("The action will be performed at the current location of the mouse.")
    print("To go back to the main interface, press Enter.")
    input()
    action()


def help_right_click():

    print("This command is used to right click the mouse.")
    print("The action will be performed at the current location of the mouse.")
    print("To go back to the main interface, press Enter.")
    input()
    action()


def help_scroll_up():

    print("This command is used to scroll the page upward.")
    print("To go back to the main interface, press Enter.")
    input()
    action()


def help_scroll_down():

    print("This command is used to scroll the page downward.")
    print("To go back to the main interface, press Enter.")
    input()
    action()


def help_exit():

    print("To stop the software, you can say \"Exit\" or \"Stop\".")
    print("To go back to the main interface, press Enter.")
    input()
    action()


def help_website():

    print("This command allows you to go to a particular website.")
    print("For this feature to work, Google Chrome must be installed in the default install location.")
    print("To go back to the main interface, press Enter.")
    input()
    action()


def help_search():
    print("You can use this command to search for a particular query on Google")
    print("For this feature to work, Google Chrome must be installed in the default install location.")
    print("To go back to the main interface, press Enter.")
    input()
    action()


if __name__ == '__main__':
    pyautogui.moveTo(pyautogui.size()[0] / 2, pyautogui.size()[1] / 2)
    print("List of available commands:")
    print("Left")
    print("Right")
    print("Up")
    print("Down")
    print("Type")
    print("Double Click")
    print("Left Click")
    print("Right Click")
    print("Scroll Up")
    print("Scroll Down\n")
    print("Browser")
    print("Search\n")
    print("To exit, please say \"Quit\" or \"Exit\"")
    print("To view the list of all available commands, please say \"Help\"")
    print("\nDeveloped by Rochan")
    action()
