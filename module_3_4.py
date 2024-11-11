# Галкин Андрей
# Задача "Однокоренные":



def single_root_words(root_word, *other_words):
    same_words = []

    for i in other_words:
        root_word_1 = root_word.upper()
        i_1 = i.upper()
        if i_1.count(root_word_1) != 0:
            same_words.append(i)
        elif root_word_1.count(i_1) != 0:
            same_words.append(i)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)