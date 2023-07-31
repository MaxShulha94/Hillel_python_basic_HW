# Дано два словники, в яких ключами є малі букви латинського алфавіту, а значеннями - цілі числа. В першому словнику
# можуть зустрічатися ключі чи значення, які присутні в другому словнику, або навпаки. Наприклад, вміст словників може
# бути наступний: a = {'x' : 1, 'y' : 2, 'z' : 3}, b = {'w' : 10, 'x' : 11, 'y' : 2}. Надрукуйте спільні ключі для обох
# словників в одному рядку через пропуск.

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}
res = {print(key, end=' ') for key in a if key in b}

# Напишіть програму, яка підраховує і роздруковує кількість появ кожного символу у введеному рядку.

my_string = input('Enter your string: ')
my_dict = {}
for i in my_string:
    my_dict[i] = my_string.count(i)
print(my_dict)


# Вводиться число n, за яким слідують n рядків тексту. Напишіть програму, яка друкує всі слова, що зустрічаються в
# тексті, по одному на рядок, і їхню кількість входжень у текст. Слова повинні бути відсортовані в порядку спадання
# відповідно до їх кількості, і всі слова при однаковому числі входжень у текст повинні бути надруковані в
# лексикографічному порядку. Вказівка. Після того, як ви створите словник усіх слів, вам захочеться впорядкувати його
# по частоті слова. Бажаного можна домогтися, якщо створити список, елементами якого будуть кортежі з двох елементів:
# частота зустрічальності слова і саме слово. Наприклад, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тоді стандартне сортування
# буде сортувати список кортежів, при цьому кортежі порівнюються по першому елементу, а якщо ці елементи
# рівні - то по другому.

num_str = int(input('Enter the number of strings: '))
text = [input('Enter thr string: ') for i in range(num_str)]
text = ' '.join(text).split()
list_tuple = []

for i in text:
     list_tuple.append((i, text.count(i)))
list_tuple = list(set(list_tuple))
for i in range(len(list_tuple)):
    for j in range(0, len(list_tuple)-i-1):
        if list_tuple[j][1] < list_tuple[j + 1][1] or (list_tuple[j][1] == list_tuple[j + 1][1] and list_tuple[j][0] >
                list_tuple[j + 1][0]):
            list_tuple[j], list_tuple[j + 1] = list_tuple[j + 1], list_tuple[j]
for i in range(1, len(list_tuple)):
    j = i
    while j > 0 and list_tuple[j][1] == list_tuple[j-1][1] and list_tuple[j][0] < list_tuple[j-1][0]:
        list_tuple[j], list_tuple[j-1] = list_tuple[j-1], list_tuple[j]
        j -= 1
for word, count in list_tuple:
    print(f'{word} {count}')






