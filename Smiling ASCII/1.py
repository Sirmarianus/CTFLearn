f = open("ASCII.txt")
S = ''
for line in f:
    S += chr(int(line))
print(S)
