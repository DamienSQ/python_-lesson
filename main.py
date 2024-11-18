# ДЗ №1
def get_sum_even_number(number):
    sum = 0
    for num in range(0, number + 1, 2):
        sum += num
    return print(sum)


# ДЗ №2
def get_odd_numbers_square(number):
    odd_numbers = [i ** 2 for i in range(0, number + 1) if i % 2 != 0]
    return print(odd_numbers)


# ДЗ №3
count_try = 0
while True:
    user_number = int(input("Введите число: "))
    if user_number >= 0:
        print("Попробуйте снова!")
        count_try += 1
    else:
        print(f"Все верно, количество попыток - {count_try}")
        break

get_sum_even_number(4)
get_odd_numbers_square(7)
