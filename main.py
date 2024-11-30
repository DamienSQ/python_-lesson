numbers_one = [1, 3, 5, 7]
numbers_two = [2, 4, 6, 8, 2, 4]


def creat_new_list(numbers_one: list, numbers_two: list):
    new_list = []
    for num_one in numbers_one:
        for num_two in numbers_two:
            new_list.append(num_one + num_two)

    return print(new_list)


creat_new_list(numbers_one, numbers_two)
