# Припустимо, що у нас є дві множини, які містять моделі деяких автомобілів:
#
# car1 = {"Toyota", "Sedan", "Automatic", "Black"}
# car2 = {"Honda", "SUV", "Manual", "White"}
# Напишіть логіку, яка повертає множину, що містить спільні моделі обох множин.



car1 = {"Toyota", "Sedan", "Automatic", "Black"}
car2 = {"Honda", "SUV", "Manual", "White"}
res = car1.intersection(car2)
print(res)