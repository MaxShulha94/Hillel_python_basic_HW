# 1) Написати лямбда-функцію, що перевірить, чи є число парним і викликати її.
res = lambda a: print(True) if a % 2 == 0 else print(False)
res(5)

# 2)Написати рекурсивну функцію для пошуку максимального елемента в списку

def recursion_func(numbers: list):
    rec_numbers = recursion_func(numbers[1:])
    if numbers[0] > rec_numbers:
        return numbers[0]
    else:
        return rec_numbers

print(recursion_func(numbers = [3, 8, 1, 6, 10, 5] ))

# 3) Дано список кортежів, кожен з яких містить два значення: назва фільму (рядок) і рейтинг (дійсне число). Напишіть
# функцію(ї),  що поверне найбільш і найменш популярні з списку.

def most_popular(movies: list):
    rating_list = []
    movie_list = []
    for movie, rating in movies:
        rating_list.append(rating)
        movie_list.append(movie)
    max_value = max(rating_list)
    min_value = min(rating_list)
    max_rating_index = int()
    min_rating_index = int()
    for i in rating_list:
        if i == max_value:
            max_rating_index = rating_list.index(i)
        elif i == min_value:
            min_rating_index = rating_list.index(i)
    return f'Most popular: {movie_list[max_rating_index]} - {rating_list[max_rating_index]}\nLess popular:' \
           f' {movie_list[min_rating_index]} - {rating_list[min_rating_index]}'

print(most_popular(movies=[('Captain Marvel', 7.0), ('Aladdin', 7.4),  ('Avengers: Endgame', 8.7)]))


# Напишіть програму, яка друкує наступний день для певної дати як у вихідних даних у форматі рррр-мм-дд. Напишіть окремі
# функції для обробки даних, які вводить користувач і використайте їх у програмі.

from datetime import datetime, timedelta
def format_date(today_date: str):
    new_date = datetime.strptime(today_date, '%d %m %Y').date()
    return new_date


def tomorrow_date(new_date):
    tomorrow = new_date + timedelta(days=1)
    return tomorrow
res = format_date('31 8 2019')
print(res)
print(tomorrow_date(res))


