import pyautogui as pag

from strategy import prepare_colors
from get_color import Screen
import time

class WIN:

    pag.FAILSAFE = False

    def __init__(self):
        self.work = True
        self.conditions, self.coords, self.coords_aim, self.coords_bet = prepare_colors()
        self.cur_col = {}
        self.winning = False
        self.screen = Screen()


    def current_colors(self):
        self.screen.rewrite()
        for i in range(len(self.coords)):
            self.cur_col[i] = (self.screen.check_color(self.coords[i][0], self.coords[i][1]))

    def work_stop(self):
        self.work = False

    def actions(self):
        print("Я сработала ____________________")
        pag.moveTo(int(self.coords_aim[0]), int(self.coords_aim[1]), 1)
        time.sleep(0.5)
        pag.moveTo(int(self.coords_bet[0]), int(self.coords_bet[1]), 2)

    def check_win(self):
        self.current_colors()
        print(self.cur_col)
        self.win = True
        self.w = 0
        for i in range(len(self.cur_col)):
            #print("aaa " + str(self.cur_col[i]))
            #print("bbb " + str(self.conditions[i]))
            if self.cur_col[i].count(self.conditions[i]) == 0:
                self.win = False
            if self.conditions[i].count(self.cur_col[i]) > 0:
                self.w+=1
                print("Совпало: "+ str(i+1))
        if (self.win == True) or (self.w == 6):
            print("Победа!############################################################################")
            self.winning = True
            self.actions()
            self.winning = False

    def antibot(self):
        if not(self.winning):
            print("AntiBot: active")
            print("Нет")
            pag.FAILSAFE = False
            for i in self.coords:
                pag.moveTo(i[0], i[1], 0.1)
                pag.click()
        else:
            print("AntiBot: inactive")
            print("Есть полное ")
