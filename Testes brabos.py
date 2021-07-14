import pyautogui as auto
import time
import pyperclip as clip

auto.PAUSE = 1


auto.hotkey('ctrl','t')
link = 'https://www.twitch.tv/alanzoka'
clip.copy(link)
auto.hotkey('ctrl','v')
auto.press('enter')
time.sleep(5)
auto.click(x,y, clicks=k)

