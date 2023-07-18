# 2. З допомогою Python порахувати наступні вирази для a=1, b=5, c=4:
def calc(a=1, b=5, c=4):
    x1, x2 = int(), int()
    x1 = -b + (b**2 - 4 * a * c) ** 0.5 / 2 * a
    x2 = -b - (b**2 - 4 * a * c) ** 0.5 / 2 * a
    print(f'x1 = {x1}, \nx2 = {x2}')
calc()


# 3. Написати програму, що за допомогою функції input() запитує ім'я користувача і потім виводить вітання на екран.

name = input('Enter your name: ')
print(f'Hello, {name}!')

# 4. Написати програму, що за допомогою функції input() запитує кількість гривень і потім виводить еквіваленте число
# доларів США (курс довільний -- можна підгледіти на будь-яку дату у вашому банку або у НБУ).

hryvna = int(input('Введіть кількість гривень: '))
exchange_rate = int(input('Введіть курс долару: '))
res = hryvna / exchange_rate
print(res)

# Завдання 5.
#
# Написати програму, що перетворює значення рядкової змінної з формату snake_case в формат CapitalizedWords
# (a.k.a. Capitalized camelCase). Значення змінної отримуйте з input(). Для простоти вважаємо, що значення змінної
# завжди складається з 3-х слів. Наприклад: 'employee_first_name' -> 'EmployeeFirstName'.
snake_string = str(input())
camel_string = snake_string.title().replace('_', '')
print(camel_string)

# Завдання 6.
#
# Даний рядок вигляду 'Taras Shevchenko*1814-03-09*1861-03-10', тобто вказане ім'я, прізвище та дати народження та
# смерті. Написати програму, що отримуючи такий рядок через input() виводить на екран окремими рядками ім'я та прізвище
# людини та її вік в роках. Для простоти при розрахунку віку можете ігнорувати число місяця та місяць.

person_name_and_date = input()
new_name_ind = person_name_and_date.find('*')
new_name = person_name_and_date[:new_name_ind]
date_ind = person_name_and_date.find('*')
date1 = person_name_and_date[date_ind + 1:date_ind + 5]
cut_str = person_name_and_date[date_ind + 5:]
date_ind2 = cut_str.find('*')
date2 = cut_str[date_ind2 + 1:date_ind2 + 5]
res = int(date2) - int(date1)
print(f'Name: {new_name}\nAge: {res}')

#Завдання 7. Написати програму, що вираховує суму усіх цифр трьохзначного числа введеного корисувачем через input().

numbers = input('Enter three numbers: ')
sum_numbers = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
print(sum_numbers)