import pyautogui as pag #in other IDEs, this will be auto-imported, so this line usually doesnt exist
pag.PAUSE = 0.5 #technically this doesnt count. pause is usually 0.1 but thats too fast for my laptop
while True:
    pag.write('update')
    pag.press('enter')