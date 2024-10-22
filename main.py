try:
    number_one = int(input("Введите первое число: "))
    number_two = int(input("Введите второе число: "))
    result = number_one + number_two
except ValueError:
    print("Ошибка: Введено не число!")
else:
    print(f"Результат сложения: {result}")

try:
    number_one = int(input("Введите первое число: "))
    number_two = int(input("ВВедите второе число: "))
    result = number_one - number_two
except ValueError:
    print("Ошибка: Введено не число!")
else:
    print(f"Результат вычитания: {result}")

try:
    number_one = int(input("Введите первое число: "))
    number_two = int(input("ВВедите второе число: "))
    result = number_one * number_two
except ValueError:
    print("Ошибка: Введено не число!")
else:
    print(f"Результат умножения: {result}")

try:
    number_one = int(input("Введите первое число: "))
    number_two = int(input("ВВедите второе число: "))
    result = number_one / number_two
except ValueError:
    print("Ошибка: Введено не число!")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
else:
    print(f"Результат деления: {result}")
