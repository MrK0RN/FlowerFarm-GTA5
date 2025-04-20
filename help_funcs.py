import os

def is_strat_created():
    if os.path.getsize("fonbet.txt") > 1:
        return True
    else:
        return False

def create_space():
    try:
        os.chdir("clicker")
        my_file = open("fonbet.txt", "a")
        my_file.write("")
        my_file.close()
    except Exception:
        os.mkdir("clicker")
        os.chdir("clicker")
        my_file = open("fonbet.txt", "w+")
        my_file.write("")
        my_file.close()

def take_body(s):
    r = 0
    k = ""
    res = []
    for i in s:
        if i == "|":
            r+=1
        if r%2 == 1:
            if i != "|":
                k+=i
        else:
            res.append(k)
            k=""
    return res

