spisok = [1.1, 1.2, 3.1, 5, 10.01]
def FindDif(arg):
    i = 0
    NewSpisok = []
    while i < len(spisok):
        if spisok[i] % 1 == 0:
            i = i + 1
        else:
            NewSpisok.append(round(spisok[i] % 1, 2))
            i = i + 1
    res = max(NewSpisok) - min(NewSpisok)
    return res
print(FindDif(spisok))