alphabet = sorted(list('azertyuiopmlkjhgfdsqwxcvbn '))


def create_jump_table(pattern: str) -> dict:
    table = dict()
    for letter in alphabet:
        i = len(pattern) - 1
        while i >= 0 and pattern[i] != letter:
            i -= 1
        table[letter] = len(pattern) - i - 1
    return table


def boyer_moore2(pattern: str, text: str) -> int:
    jump_table = create_jump_table(pattern)
    cursor = len(pattern) - 1
    while cursor < len(text):
        k = 0
        while k < len(pattern) and text[cursor - k] == pattern[-1 - k]:
            k += 1
        if k == len(pattern):
            return cursor - k + 1
        cursor += jump_table[text[cursor]]
    return -1


def boyer_moore(pattern: str, text: str) -> int:
    jump_table = create_jump_table(pattern)
    cursor = len(pattern) - 1
    while cursor < len(text):
        if text[cursor] != pattern[-1]:
            cursor += jump_table[text[cursor]]
        else:
            k = 1
            while k < len(pattern) and text[cursor - k] == pattern[-1 - k]:
                k += 1
            if k == len(pattern):
                return cursor - k + 1
            else:
                cursor += jump_table[text[cursor]]
    return -1


sample = "salu les glutens"
find = "lut"
a = boyer_moore(find, sample)
print(a, sample[a:])


a = boyer_moore2(find, sample)
print(a, sample[a:])
