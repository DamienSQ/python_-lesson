user_number = int(input("Введите целое положительное число: "))

if user_number > 0:
    while user_number >= 0:
        print(user_number)
        user_number -= 1
else:
    print("Число не верно")

