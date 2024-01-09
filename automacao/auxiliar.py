import pyautogui
import time

#o time é para eu ter tempo de parar o mouse onde eu quero para descobrir o x e o y o xy= a posiçao do mouse
time.sleep(5)
print(pyautogui.position())
#o print para me mostrar no terminal a posiçao xy
pyautogui.scroll(-500)