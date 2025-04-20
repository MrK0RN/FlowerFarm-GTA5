from position import GET_POS
import get_color


def GET_FUNC():

    func = 0

    if func == 0:
        n = input()
    else:
        n = func



    print(n)

def func_create(n):
    if n == 0:
        print("Команда не распознана, введите ее еще раз")
        GET_FUNC()
    if n == "!symb" or n == 1:
        a = input()
        func = str("1" + a + "|")
        return func
    if n == "!text" or n == 2:
        a = input()
        func = str("2" + a + "|")
        return func
    if n == "!click" or n == 3:
        kk = GET_POS()
        return kk
    if n == "!stop" or n == 10:
        func = "4//"
        return func
    if n == "colors" or n == 5:
        func = get_color.color_for_check("w")
        return func