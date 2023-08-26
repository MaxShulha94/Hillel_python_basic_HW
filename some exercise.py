class Bank:

    def __init__(self):
        self._balance: int = 0
        self.account = False

    def open_account(self):
        self._balance = 0
        self.account = True
        return f'You have opened your account! Balance equals {self._balance}'

    def put_money(self, money):
        if self.account == True:
            self._balance += money
            return f'Your balance is {self._balance} UAH'
        else:
            return f'You should open your account first!'

    def watch_balance(self):
        return f'Balance is {self._balance}'

    def take_off_money(self, money):
        if self.account is True and self._balance >= money:
            self._balance -= money
            return f'Success! your balance is {self._balance} now.'
        else:
            return f'Create account or check your balance!'

deposite = Bank()
deposite.open_account()
print(deposite.put_money(100))
print(deposite.watch_balance())
print(deposite.take_off_money(100))