import pyautogui , time

while True:
    n1 = input(str("Qual biblioteca você quer instalar: "))
    print("y = yes, n = no")
    n2 = input(str("Voce Tem certeza que quer instalar? : "))
    if n2 == "y":
            pyautogui.hotkey("win" , "r")
            time.sleep(1)
            pyautogui.write("cmd")
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(2)
            pyautogui.write("pip install " + n1)
            pyautogui.press("enter")

