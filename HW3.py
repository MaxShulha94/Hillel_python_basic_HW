# Програма повинна виконувати прості математичні дії +,-, *, /.. Користувачу пропонується заздалегідь ввести числа
# і математичну операцію над цими числами, програма, відповідно до дії, вираховує і висвітлює результат.

# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter the second number: '))
# action = input('Enter +,-,*,/: ')
# result = int()
# if action == '+':
#     result = num1 + num2
# elif action == '-':
#     result = num1 - num2
# elif action == '*':
#     result = num1 * num2
# else:
#     if num1 and num2 != 0:
#         result = num1 / num2
#     else:
#         print('ZeroDivisionError!')
# print(result)

# Ваша програма повинна перенести останній список елементів із кінця в початок, т.е. останній елемент списку повинен стати
# першим. При цьому послідовність інших елементів не повинна змінюватися.

my_list = list(input('Enter your list: '))
last = my_list[-1]
my_list.insert(0, last)

print(my_list[0:len(my_list)-1:1])