import pyautogui as auto
import time
import pyperclip as clip

auto.PAUSE = 1

def autoRemi():
   text = 'Oi.'
   auto.click(x=1116, y=634)
   clip.copy(text)
   auto.hotkey('ctrl','v')
   auto.press('enter')

auto.alert(text = 'O respondedor de chat do Remi tumático vai começar.')
while True:
   autoRemi()
   time.sleep(600)
