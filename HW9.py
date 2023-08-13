# -*- coding: utf-8 -*-
# Задача що була на занятті.
my_file = 'my_file.txt'
max_len = str()
with open(my_file, 'r+', encoding='utf-8') as file:

    my_file = file.readlines()

    for line in my_file:
        max_len = my_file[0].strip()
        if len(max_len) < len(line.strip()):
            max_len = line.strip()
        else: continue
    print(max_len)


# Context manager

rev_file = 'reversed_month.txt'
my_file = 'month.txt'
list_of_month = []
with open(my_file, 'r') as my_file:
    my_file = my_file.readlines()
    for line in my_file:
        line = line.strip()
        list_of_month.append(line)
    print(f'There are {len(list_of_month)} words in month.txt')

with open(rev_file, 'w') as rev_file:
    for line in reversed(list_of_month):
        rev_file.write(line + '\n')


# ДЗ 19. Реалізуйте генератор, який буде генерувати "решітку" заданого розміру N x N.

def grid(a: int, b: int):
    while b != 0:
        yield a * '#'
        b -= 1

funk = grid(a=3,b=3)
for num in funk:
    print(num)

