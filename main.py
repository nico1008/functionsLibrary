from typing import List, Any


def list_check(a):
    for elem in a:
        if elem < 5:
            print(elem);


def list_con(b, c):
    result = b+c
    print(result)

def swap(a_1, b_2):
    t=a_1
    a_1=b_2
    b_2=t
    print("1 =", a_1, ";   2 =", b_2)

def

print("начало")

print("проверка массива")
print(list_check([23, 32, 23, 34, 54, 4, 2, 62, 6, 26, 2, 62, 62, 62]))

print("соединение 2 массивов ")
print(list_con([21, 123, 1, 3, 1, 23, 3, 1, 5, 3, 15], [431, 4576, 25, 27, 27, 42, 64, 25]))

print("перемена местами ")
print(swap(132,34634))
