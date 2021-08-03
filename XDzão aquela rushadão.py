import pyautogui
import time
import pyperclip
import pandas as pd


pyautogui.PAUSE = 1
time.sleep(1)
pyautogui.press('winleft')
pyautogui.write('brave')
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('ctrl','t')
link = 'https://drive.google.com/drive/folders/1wRTFw0sUVBjRr4hW5U9LF7DjLixRyxym'
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(2)
pyautogui.moveTo(363, 432)
pyautogui.click(button='right')
pyautogui.click(606, 641)
time.sleep(10)
pyautogui.alert('O downlod irá iniciar')
tabela = pd.read_excel(r'C:\Users\Ivo Lucas\Desktop\Vendas - Dez.xlsx')
#display(tabela)
faturamento = tabela['Valor Final'].sum()
qtProdutos = tabela['Quantidade'].sum()


