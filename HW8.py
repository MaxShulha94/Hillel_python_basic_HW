# Написати декоратор, котрий задекорує функцію і порахує час виконання самої функції.
import time
def calc_time(func):
    def wrapper(*args):
        start_time = time.time()
        res = func(*args)
        finish_time = time.time()
        duration = finish_time - start_time
        print(duration)
        return res
    return wrapper

@calc_time
def example_func(*args):
    for i in range(*args):
        print(i ** 2)

example_func(100000)

# Вам потрібно обчислити середнє значення квадратів непарних чисел зі списку. Використовуйте функції map, filter
# та reduce.
import functools
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [i for i in numbers if i % 2 != 0]
sq_odd = map(lambda x: x ** 2, odd_numbers)
sum_sq_odd = functools.reduce(lambda x, y: x + y, sq_odd)
res = sum_sq_odd / len(odd_numbers)
print(res)
