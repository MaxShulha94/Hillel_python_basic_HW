# 6.Дано список цілих чисел, в якому зустрічаються однакові значення. Напишіть логіку для друку цього списку після
# видалення всіх однакових значень.

# my_list = [45, 67, 23, 45, 111, 67, 12, 55]
# new_list = []
# for i in my_list:
#     if my_list.count(i) == 1:
#         new_list.append(i)
#     else:
#         if i in new_list:
#             continue
#         else:
#             new_list.append(i)
# print(new_list)


# 7. Напишіть програму, яка по даному числу n від 1 до 9 виводить на екран n пінгвінів. Зображення одного пінгвіна має
# розмір 5 × 9 символів, між двома сусідніми пінгвінами також є порожній (з пропусків) стовпець. Дозволяється вивести
# порожній стовпець після останнього пінгвіна. Для спрощення малювання скопіюйте пінгвіна з прикладу в середовище розробки.

# number_of_birds = int(input('Enter the number: '))
# bird = ['   _~_   ', '  (o o)  ', '  / V \  ', ' / (_) \ ', '  ^^ ^^  ']
# res = [i * number_of_birds for i in bird]
# for el in res:
#     print(el)

# 8. Користувач вводить рядок, Ваша задача — сформатувати строку в хештег.

# my_str = input('Enter your string: ')
# symbols = '!,@$?/.\][{}_-=+*^%'
# res = '#'
# my_str = my_str.title().replace(' ', '')
# for i in my_str:
#     if i in symbols:
#         continue
#     else:
#         res += i
# print(res)

#9. Програма випадковим чином обирає число від 1 до 10 і пропонує користувачу його вгадати. Користувач вводить число, а
# програма перевіряє його і, якщо користувач не вгадав, що повідомляє ви введене число більше чи менше від
# згенерованого. Після цього знову просить вгадати. І так, поки користувач не вгадає.

# import random
# win = False
# while win == False:
#     mynumber = int(input('Enter your number: '))
#     lucky_number = random.randrange(1, 11)
#     if mynumber == lucky_number:
#         print('Congratulations!')
#         win = True
#     else:
#         print('Try one more time!, lucky number was ', lucky_number)

# 10. Створити програму, що виводить на екран числа від 1 до 100 при цьому заміняючи:
        #   числа, що діляться на 3, на рядок Fizz
        #   числа, що діляться на 5, на рядок Buzz
        #   числа, що діляться і на 3, і на 5, на рядок FizzBuzz
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 5 == 0:
#         print('Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     else:
#         print(i)





