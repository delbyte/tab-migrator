import pyautogui as pag
import time
import pyperclip

migrator = open("migrator.txt", "w")
alltabs = []

def navigate():
    # to navigate tabs
    pag.hotkey('ctrl', 'tab')

def copy():
    # to copy the url of the tab
    pag.hotkey('alt', 'd')

    pag.hotkey('ctrl', 'c')

def paste():
    #to paste the url in the text file
    temp = pyperclip.paste()
    alltabs.append(temp)

def tabnum():
    ###to find the number of tabs in the browser window
    pag.hotkey('ctrl', 't')

    #chrome tab inspector
    pyperclip.copy('')
    inspect = "chrome://inspect/#pages"
    pag.typewrite(inspect)
    pag.press('enter')
    time.sleep(0.3)

    #console access to get num tabs into clipboard
    #todo- ensure this doesn't fail due to the allow pasting thingy
    pag.hotkey('ctrl', 'shift', 'i')
    time.sleep(0.3)
    time.sleep(0.3)
    finder = "copy(document.getElementById(\"pages-list\").childElementCount)"
    time.sleep(0.3)
    pag.typewrite(finder)
    pag.press('enter')
    time.sleep(2)

    #close tab
    pag.hotkey('ctrl', 'w')


#main func

time.sleep(2)

#shift to the browser
pag.hotkey('alt', 'tab')

#find number of tabs
tabnum()

num = int(pyperclip.paste())

for i in range(num-1):
    time.sleep(0.2)
    navigate()
    time.sleep(0.2)
    copy()
    time.sleep(0.2)
    paste()

for n in alltabs:
    migrator.write(str(n)+'\n')

migrator.close()
#todo- get the number of tabs for the loop of copying
#todo- paste in the txt file by using a list and appending





