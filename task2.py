from queue import Empty

from pkg_resources import empty_provider

spisok = [1, 2, 3, 4, 5, 6, 7]
def NewList (arg):
    i = 0
    j = len(arg) - 1
    NewSpisok = []
    if len(arg) % 2 != 0:
        while i != len(arg) // 2 + 1:
            NewSpisok.insert(i, arg[i] * arg[-(i + 1)])
            i = i + 1
    else:
        while i != len(arg) // 2:
            NewSpisok.insert(i, arg[i] * arg[-(i + 1)])
            i = i + 1
    return NewSpisok
print(NewList(spisok))



