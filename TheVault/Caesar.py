# Tu wbij tekst
L = 'TeW}vr$ -dy!)p^vpeyvp^A v+/PK'
for i in range(96):
    s = ''
    for char in L:
        temp = ord(char)
        temp += i
        if(temp > 126):
            temp -= 95
        s += chr(temp)
    print(i, s)