import sys, math, os

#Make current dir working directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

file = open("test8.txt","r")
lines = file.readlines()
n = int(lines.pop(0))
tab_data = lines
tab_value = ["?" for i in range(n)]

def value(arg):
    if arg[0] == "$":
        if tab_value[int(arg[1:])] != "?":
            return int(tab_value[int(arg[1:])])
        else:
            return int(calc(int(arg[1:])))
    else:
        return int(arg)

def calc(i):
    ope, arg1, arg2 = tab_data[i].split()
    if ope == "VALUE":
        tab_value[i] = value(arg1)
    elif ope == "ADD":
        tab_value[i] = value(arg1) + value(arg2)
    elif ope == "SUB":
        tab_value[i] = value(arg1) - value(arg2)
    elif ope == "MULT":
        tab_value[i] = value(arg1) * value(arg2)
    return tab_value[i];

for i in range(n):
    print(calc(i))