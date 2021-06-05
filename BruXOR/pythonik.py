
f = open("1.txt")
kod = f.readline()
S = ''
for ele in kod:
    S += (chr(ord(ele)^1))
print(S)
