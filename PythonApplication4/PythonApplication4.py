#-*- coding:cp1251 -*-
import math
import random
#4.�������� ���� �����������.
#� ������� ��������� ���� ���� ������, �������� ������� �� ����� ���������.
#���������: +, -, /, *, ���������� � �������, ������, ��������� �����, ��������� � ����� ����� ����������.
#����� � ������� �������� ������� ��������, ������� ��������� ��� ��������. ��� ���������� �������� 0.
#� ������� ��������.

do = input("������ �������������� ��������: ")
while do != "exit":
    if do == "+":
        number1 = float(input("������ 1 ��������: "))
        number2 = float(input("������ 2 ��������: "))
        print(number1 + number2)
    elif do == "-":
        number1 = float(input("������ 1 ��������: "))
        number2 = float(input("������ 2 ��������: "))
        print(number1 - number2)
    elif do == "/":
        number1 = float(input("������ 1 ��������: "))
        number2 = float(input("������ 2 ��������: "))
        if number2 != 0:
            print(number1 / number2)
        else:
            print("�� 0 ������ ������")
    elif do == "*":
        number1 = float(input("������ 1 ��������: "))
        number2 = float(input("������ 2 ��������: "))
        print(number1 * number2)
    elif do == "pow":
        number1 = float(input("������ 1 ��������: "))
        number2 = float(input("������ 2 ��������: "))
        print(pow(number1, number2))
    elif do == "module":
        number1 = float(input("������ ��������: "))
        print(abs(number1))
    elif do == "0":  #�������� ��������� �����, ���� ������ �� ����
        print(random.randint(0, 1000))
    elif do == "div":
        number1 = float(input("������ 1 ��������: "))
        number2 = float(input("������ 2 ��������: "))
        if number2 != 0:
            print(number1 // number2)
        else:
            print("�� 0 ������ ������")
    elif do == "mod":
        number1 = float(input("������ 1 ��������: "))
        number2 = float(input("������ 2 ��������: "))
        print(number1 % number2)
    elif do == "f":
        number1 = int(input("������  ��������: "))
        print(math.factorial(number1))
    elif do == "arccos":
        number1 = float(input("������ ��������: "))
        number11 = number1*math.pi/180
        print(math.acos(number11))
    do = input("������� �������� ��� ������� exit, ��� �� ���������: ")

