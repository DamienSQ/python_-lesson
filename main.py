try:
    number_one = int(input("Введите первое число: "))
    number_two = int(input("ВВедите второе число: "))
    result = number_one / number_two
except ValueError:
    print("Ошибка: Введено не число!")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
else:
    print(result)
finally:
    print("Программа завершена")
