# 1 Задание
def max_number(a, b):
    if a >= b:
        return a
    elif b >= a:
        return b


# 2 задание
def empty_function():
    pass


# 3 задание
def even_numbers(n):
    random_numbers = []

    for i in range(0, n + 1, 2):
        random_numbers.append(i)
        yield i


# 4 задание
def test_max_number():
    assert max_number(24, 3) == 24, "Ошибка: должно быть число 24"
    assert max_number(17, 36) == 36, "Ошибка: должно быть число 36"
    assert max_number(15, 15) == 15, "Ошибка: должно быть число 15"


for i in even_numbers(12):
    print(i)

print(max_number(33, 34))

test_max_number()
print("Все тесты пройдены")
