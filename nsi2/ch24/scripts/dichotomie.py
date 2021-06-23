def rech_dicho(lst, elt):
    n = len(lst)
    if n < 2:
        return elt in lst
    elif lst[n // 2] == elt:
        return True
    else:
        return rech_dicho(lst[:n // 2], elt) if lst[n // 2] > elt else rech_dicho(lst[n // 2 + 1:], elt)



