Num = 234
def ToBinar(arg):
    res = ""
    while arg != 0:
        res = f"{arg % 2}" + res 
        arg = arg // 2
    return res
print(ToBinar(Num))
