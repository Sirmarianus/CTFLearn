
f = open("1.txt")
kod = f.readline()
S = ''
print(kod)
for ele in kod:
    print(ord(ele))
    S += (chr(ord(ele)^1))
print(S)
