import re


def get_user_text():
    text = input("Введите текст: ").strip().lower()
    new_text = re.sub('[!?,.@$]', ' ', text).split()
    return new_text


def get_word_count(text: str):
    return print(f"В тексте {len(text)} слов/слово")


def get_long_word(text: str):
    longs_word = ""

    for word in text:
        if len(word) > len(longs_word):
            longs_word = word

    return print(f"Самое длинное слово - {longs_word}")


def get_vowels(text: str):
    count_vowels = 0
    join_text = ' '.join(text)

    for char in join_text:
        if char in ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'):
            count_vowels += 1

    return print(f"количество гласных - {count_vowels}")


def get_repetition_word(text: str):
    counts = {}

    for word in text:
        if counts.get(word):
            counts[word] += 1
        else:
            counts[word] = 1

    for count_key, count_value in counts.items():
        print(f"Слово \"{count_key}\" встречается {count_value} раз/раза")


user_text = get_user_text()

get_word_count(user_text)
get_long_word(user_text)
get_vowels(user_text)
get_repetition_word(user_text)
