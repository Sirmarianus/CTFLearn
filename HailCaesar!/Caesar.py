# Tu wbij tekst
L = """2m{y!"%w2'z{&o2UfX~ws%!._s+{ (&@Vwu{ (&@_w%{v{(&0"""
for i in range(96):
    s = ''
    for char in L:
        temp = ord(char)
        temp += i
        if(temp > 126):
            temp -= 95
        s += chr(temp)
    print(i, s)