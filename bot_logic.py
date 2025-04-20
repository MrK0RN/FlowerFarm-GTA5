import time

import screener_check
import move
import keyboard

strategy = screener_check.Screener()

strategy.load_map_as_scrshot()
#strategy.rewrite()

flower_num = 100
Ier = 0

def check_side(x, y):
    print("#check_side is working")
    res = {}
    strategy.forward_tracker(10, 3, strategy.flower_color)
    if strategy.results.keys():
        res[strategy.area_procent_get(x, y, strategy.flower_color)] = [0, (x, y)]
        res[strategy.area_procent_get(x-3, y, strategy.flower_color)] = [-1, (x-3, y)]
        res[strategy.area_procent_get(x+3, y, strategy.flower_color)] = [1, (x+3, y)]
    h = res.keys()
    print(res)
    return res[max(h)]

def check_on_run(secs):
    keyboard.press("w")
    print("check_on_run is working")
    keyboard.press("shift")
    l = time.time()
    while not(strategy.button_check()):
        if time.time() - l > secs:
            keyboard.release("shift")
        steps = 0
        print(">>")
        strategy.forward_tracker(10, 3, strategy.flower_color)
        if (steps == 1000):
            print("did not found")
            keyboard.release("w")
            break
        strategy.clear_results()
    keyboard.release("w")


def action():
    strategy.forward_tracker(2, 3, strategy.flower_color)
    f = 2
    g = 0
    while len(strategy.results.keys()) == 0:
        if (g == 30):
            f += 2
            g = 0
        move.turn()
        strategy.forward_tracker(f, 2, strategy.flower_color)
        g += 1
        print("turning...")
    if len(strategy.results.keys()) != 0:
        #xy = strategy.results[min(strategy.results.keys())]
        #resus = check_side(xy[0], xy[1])
        #while resus[0] != 0:
            #move.turn_snake(resus[0])
            #resus = check_side(resus[1][0], resus[1][1])
        move.turn()
        move.turn()

        check_on_run(min(strategy.results.keys())//3)
        move.press("e")
        time.sleep(8)
        strategy.clear_results()

for i in range(flower_num):
    action()