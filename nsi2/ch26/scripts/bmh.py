def create_jump_table(pat: str) -> dict:
    table = dict()
    for i in range(len(pat) - 1):
        table[pat[i]] = len(pat) - i - 1
    return table


def bmh(txt: str, pat: str) -> int:
    global nb_opel
    table = create_jump_table(pat)
    n = len(pat)
    p = len(txt)
    i = n - 1

    while i < p:
        j = 0
        print(text)
        print(" " * i + "^")
        print(" " * (i + 1 - n) + pat)
        print()
        nb_opel += 1
        while txt[i - j] == pat[n - 1 - j]:
            print(text, i)
            print(" " * (i - j) + "=")
            print(" " * (i + 1 - n) + pat)
            print()
            j += 1
            if j == n:
                return i - j + 1
            nb_opel += 1
        print(text)
        print(" " * (i - j) + "\u2260")
        print(" " * (i + 1 - n) + pat)
        print()
        if txt[i] not in table:
            i += n
        else:
            i += table[txt[i]]
    return -1





nb_opel = 0
text = 'JENESAISVRAIMENTPASQUOIECRIREDANSCETEXTE'
pattern = 'TEXTE'
print(bmh(text, pattern), nb_opel)
print(nb_opel)