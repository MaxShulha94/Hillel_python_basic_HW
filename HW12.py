# -*- coding: utf-8 -*-
# 1)Завдання: Клас "Книжковий Магазин"


class Book:

    def __init__(self, book_name: str, author: str, year: int):
        self.book_name = book_name
        self.author = author
        self.year = year


    def __str__(self):
        return f'"{self.book_name}", written by {self.author} in {self.year}'

class Book_Store:

    def __init__(self):
        self.book_list = {}

    def add_book(self,  book):
        self.book_list[book.book_name] = book
        return f'"{book.book_name}" is added to our list!'

    def remove_book(self, book):
        if book.book_name in self.book_list:
            self.book_list.pop(book.book_name)
            return f'"{book.book_name} was deleted from list!'
        else:
            return f'We dont have such book!'

    def __str__(self):
        tmp = ''
        for book_name in self.book_list:
            tmp += f'{self.book_list[book_name]}.\n'
        return f'We have here:\n{tmp}'

first_book = Book("Hamlet", "William Shakespeare", 1608)
second_book = Book("The Moon and Sixpence", "William Somerset Maugham", 1919)
store = Book_Store()
print(first_book)
store.add_book(first_book)
print(store.add_book(second_book))
print(store.remove_book(first_book))
print(store)


# 2) Додаткове з @property

class User:

    def __init__(self, name: str, surname: str, age: int ):
        self._name = name
        self._surname = surname
        self._age = age

    @property
    def name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    @property
    def surname(self):
        return self._surname

    def set_surname(self, surname):
        self._surname = surname

    @property
    def age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    @property
    def get_full_name(self):
        return f'Name: {self._name}\nSurname: {self._surname}\nAge: {self._age}'

human1 = User('Niccolo', 'Machiavelli', 11)
print(human1.get_full_name)