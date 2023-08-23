# Створити клас Годзіла. При створенні Годзіли вказується об'єм шлунку (параметром конструктора ).
class Godzilla:

    def __init__(self, stomach_vol: int, *human_vol: int):
        self.stomach_vol = stomach_vol
        self.human_vol = sum(human_vol)

    def eat_human(self):
        free_space = self.stomach_vol - self.human_vol
        if free_space < self.stomach_vol * 0.1:
            return f'Im not hungry!'
        else:
            return f'Free space in my stomach equals {free_space}'
g1 = Godzilla(100, 12)
print(g1.eat_human())

