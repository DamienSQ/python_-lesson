words_list = ["street", "coca-cola", "music", "game", "fun"]

def change_item_list(list: list):
    list[0], list[-1] = list[-1], list[0]
    return print(list)

change_item_list(words_list)