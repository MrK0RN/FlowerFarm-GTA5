import config
import help_funcs
import position

def write_strategy():
    f = open("fonbet.txt", "a")
    #Сначала определим буллиды по порядку на одной стороне
    print("Сначала определим буллиды по порядку на одной стороне, потом на другой, последовательно наведите на точки буллидов, следуйте инструкции")
    for i1 in range(2):
        for i in range(config.bullid//2):
            input("Готовы? Нажмите Enter")
            s = "|1||"+str(i1)+"||"+str(i)+"|"+position.GET_POS()+"$"
            f.write(s)
    #Потом зададим Стратегию при которой голосуем
    print("зададим Стратегию при которой голосуем\nНапример:  |WLW||LLI|  ---  Означает, что счет будет 1: Попал-Не попал-Попал 2: Не попал-Не попал-Еще не ударил\n\nW - Попал\nL - Не попал\nI - Еще не ударил")
    strat = input()
    s = "|2|"+strat+"$"
    f.write(s)

    print("Теперь определим в место, где находиться та ставка, которую вы хотите ставить")
    input("Готовы? Нажмите Enter")
    s = "|3|" + position.GET_POS() + "$"
    f.write(s)

    print("Теперь определим в место, где находиться тот, исход который вы планируете")
    input("Готовы? Нажмите Enter")
    s = "|4|" + position.GET_POS() + ""
    f.write(s)

    #Далее Определим точку которую голосуем
    print()
    f.close()

def prepare_colors():
    f = open("fonbet.txt", "r")
    s = f.read()
    f.close()
    res = s.split("$")
    strat = ""
    print(res)
    for i in res:
        if i[1] == "2":
            strat = i
    g = help_funcs.take_body(strat)
    g.pop(0)
    strat_list = []
    print(g)

    for i in g:
        for i1 in i:
            if i1 == "W":
                strat_list.append(config.win)
            elif i1 == "L":
                strat_list.append(config.miss)
            elif i1 == "I":
                strat_list.append(config.inactive)
            else:
                print("Неправильно создали стратегию")
    print(strat_list)

    print("Strategy is maid")

    coords = []
    z = []
    for i in res:
        if i[1] == "1":
            z = help_funcs.take_body(i)
            coords.append([int(float(z[3])//1), int(float(z[4])//1)])

    print(type(coords[0][0]))
    coords_aim = []
    coords_bet = []
    for i in res:
        if i[1] == "3":
            z = help_funcs.take_body(i)
            z.pop(0)
            print(z)
            coords_aim = z
        elif i[1] == "4":
            z = help_funcs.take_body(i)
            z.pop(0)
            print(z)
            coords_bet = z


    print("Coords initialization is maid")

    return strat_list, coords, coords_aim, coords_bet

