import pyautogui as auto
import time
import pyperclip as pcp

auto.PAUSE = 1

def autoRemi():
   text = 'Oi.'
   auto.click(x=1116, y=634)
   pcp.copy(text)
   auto.hotkey('ctrl','v')
   auto.press('enter')

auto.alert('O respondedor de chat do Remi automático vai começar')

while True:
   autoRemi()
   time.sleep(600)
   if auto.press('backspace') == 1:
      break

