password = "password"

while True:
    user_input = input("Введите пароль: ")
    if user_input == password:
        print("Доброе пожаловать")
        break
    else:
        print("Пароль не верный, попробуйте снова")