import re

# Задача 1 Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это множество в строку,
# сворачивая соседние по числовому ряду числа в диапазоны.

print()
print('Программа 1 задачи:')
print()

listNumbers1 = [1, 4, 5, 2, 3, 9, 8, 11, 0]
listNumbers2 = [1, 4, 3, 2]
listNumbers3 = [1, 4]

def listToSet(array: list):
    array.sort()
    stringNumbers = ''
    print(f'Заданный лист: {array}')
    counter = -1
    first = 0
    last = 0
    for i in range(len(array)):
        counter += 1
        if i == len(array) - 1 or array[i + 1] - array[i] > 1:
            last = array[i]
            first = array[i - counter]
            if first == last:
                stringNumbers += (f'{first}')
            else:
                stringNumbers += (f'{first}-{last}')
            counter = -1
            stringNumbers += ', '
    if stringNumbers[len(stringNumbers) - 2] == ',':
        stringNumbers = stringNumbers[:-2]
    print(f'Результат: {stringNumbers}')

listToSet(listNumbers1)
listToSet(listNumbers2)
listToSet(listNumbers3)

# Задача 2 Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.    A4B3C2XYZD4E3F3A6B28

print()
print('Программа 2 задачи:')
print()

text = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'
textWithIncorrectCharacters = 'Skoifjыфашозао1010'
emptyText = ''

def encoding(string):
    regex = '^[A-Z]+$'
    if re.match(regex, string):
        result = ''
        prevChar = ''
        count = 1
        if not string:
            return 'Nothing to encode'

        for char in string:
            if char != prevChar:
                if prevChar:
                    if count != 1:
                        result += prevChar + str(count)
                    else:
                        result += prevChar
                count = 1
                prevChar = char
            else:
                count += 1
        else:
            result += prevChar + str(count)
            return result
    elif string == '':
        return 'Ошибка: Введена пустая строка!'
    else:
        return 'Ошибка: Введены некорректные данные!'

print(f'Оригинальный текст задания: {text}')
print(encoding(text))
print(f'Текст с некорректными символами: {textWithIncorrectCharacters}')
print(encoding(textWithIncorrectCharacters))
print(f'Пустой текст: {emptyText}')
print(encoding(emptyText))