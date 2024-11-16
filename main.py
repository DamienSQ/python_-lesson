import re

user_text = input("Введите текст: ").strip().lower()


def get_word_count(text: str):
    new_text = re.sub('[!?,.@$]', ' ', text).split()
    return print(f"В тексте {len(new_text)} слов/слово")


def get_long_word(text: str):
    new_text = re.sub('[!?,.@$]', ' ', text).split()
    longs_word = ""

    for text in new_text:
        if len(text) > len(longs_word):
            longs_word = text

    return print(f"Самое длинное слово - {longs_word}")


def get_vowels(text: str):
    count_vowels = 0

    for char in text:
        if char in ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'):
            count_vowels += 1

    return print(f"количество гласных - {count_vowels}")


def get_repetition_word(text: str):
    new_text = re.sub('[!?,.@$]', ' ', text).split()
    counts = {}

    for word in new_text:
        if counts.get(word):
            counts[word] += 1
        else:
            counts[word] = 1

    for count_key, coint_value in counts.items():
        print(f"Слово \"{count_key}\" встречается {coint_value} раз/раза")


get_word_count(user_text)
get_long_word(user_text)
get_vowels(user_text)
get_repetition_word(user_text)
