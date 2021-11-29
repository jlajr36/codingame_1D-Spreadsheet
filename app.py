import sys, math, os

#Make current dir working directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

file = open("test2.txt","r")
lines = file.readlines()

n = int(lines.pop(0))
values = []

for inx in range(n):
    _line = lines[inx].strip()
    operation, arg_1, arg_2 = _line.split()

    if operation == "VALUE":
        values.append(int(arg_1))
        print(values[inx])

    if operation == "ADD":
        num1 = 0
        num2 = 0
        if "$" in arg_1:
            num1 = values[int(arg_1[1])]
        else:
            num1 = int(arg_1)
        if "$" in arg_2:
            num2 = values[int(arg_2[1])]
        else:
            num2 = int(arg_2)
        adin = num1 + num2
        print(adin)
        values.append(adin)

    if operation == "SUB":
        num1 = 0
        num2 = 0
        if "$" in arg_1:
            num1 = values[int(arg_1[1])]
        else:
            num1 = int(arg_1)
        if "$" in arg_2:
            num2 = values[int(arg_2[1])]
        else:
            num2 = int(arg_2)
        dif = num1 - num2
        print(dif)
        values.append(dif)

    if operation == "MULT":
        num1 = 0
        num2 = 0
        if "$" in arg_1:
            num1 = values[int(arg_1[1])]
        else:
            num1 = int(arg_1)
        if "$" in arg_2:
            num2 = values[int(arg_2[1])]
        else:
            num2 = int(arg_2)
        pro = num1 * num2
        print(pro)
        values.append(pro)