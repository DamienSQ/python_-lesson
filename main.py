age = int(input("Введите ваш возраст: "))
citizen_country = input("Вы являетесь гражданином страны? да/нет ")
disqualified = input("Есть ли у вас судимости? да/нет ")

if age >= 18 and citizen_country.lower() == "да" and disqualified.lower() == "нет":
    print("Вы можете голосовать на выборах")
else:
    print("Вы не можете голосовать на выборах")

