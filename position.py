import pyautogui as pg
import time

def get_position():
    ammm = pg.position()
    print(ammm)
    return ammm

def GET_POS():
    print("В течении 5 секунд наведите курсор на место клика, уберете, когда программа выдаст \"Готово!\"")
    time.sleep(3)
    ammm = pg.position()
    print(ammm)
    ammm = "|" + str(ammm.x) + "||" + str(ammm.y) + "|"
    return ammm

GET_POS()
#ammm = "3" + "x" + str(ammm[0]) + "y" + str(ammm[1]) + "|"