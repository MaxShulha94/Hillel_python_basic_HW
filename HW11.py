# coding: utf-8
class Product1:

    def __init__(self, name, price, quantity):

        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Product name: {self.name}, cost: {self.price} UAH, quantity: {self.quantity} '


class Product2:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Product name: {self.name}, cost: {self.price} UAH, quantity: {self.quantity} '


class Product3:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Product name: {self.name}, cost: {self.price} UAH, quantity: {self.quantity}'


class Warehouse:
    def __init__(self):
        self.storage = {}
        self.total_profit = 0

    def add_to_storage(self, product):
        self.storage[product.name] = product
        return f'{product.name} is added'

    def remove_from_storage(self, product):
        if product.name in self.storage:
            removed_product = self.storage.pop(product.name)
            return f'{removed_product.name} is removed'
        else:
            return f'{product.name} not found in storage'

    def get_item_value(self, product):
        return f'We have {product.quantity} {product.name} which costs {product.price * product.quantity} UAH'

    def get_total_value(self):
        total = 0
        for product in self.storage.values():
            total += product.price * product.quantity
        return f'All our goods costs {total}'

    def sale(self, sale_name, sale_quantity):
        if sale_name in self.storage:
            product = self.storage[sale_name]
            if product.quantity >= sale_quantity:
                product.quantity -= sale_quantity
                profit = sale_quantity * product.price
                self.total_profit += profit
                return f'{sale_quantity} {sale_name} is sold, we got {profit} UAH'
            else:
                return f'Not enough {sale_name} in storage'
        else:
            return f'{sale_name} not found in storage'

    def see_total_profit(self):
        return f'Our budget is {self.total_profit} UAH'

    def __str__(self):
        tmp = ''
        for product in self.storage:
            tmp += f' {self.storage[product]}. \n'
        return f'Warehouse  contains:\n{tmp} '

    def save_info_to_file(self):
        data = f'Total profit: {self.total_profit}\n'
        for product_name, product in self.storage.items():
            data += f'{product_name}: Price: {product.price}, Quantity left in warehouse: {product.quantity}\n'

        file_handler = File_Writer('warehouse_info.txt')
        file_handler.save_to_file(data)




class File_Writer:

    def __init__(self, filename):
        self.filename = filename

    def save_to_file(self, data):
        with open(self.filename, 'w') as file:
            file.write(data)


guitars = Product1('Gibson', 100, 10)
synth = Product2('Yamaha', 150, 10)
drums = Product3('Tama', 200, 10)

a = Warehouse()
a.add_to_storage(guitars)
a.add_to_storage(drums)
print(a.sale( 'Tama', 1))

print(a.get_total_value())
print(a.see_total_profit())
a.sale('Gibson', 5)
print(a.see_total_profit())
a.save_info_to_file()