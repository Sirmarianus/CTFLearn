import binascii

f = open('CTFLearn.pdf', 'rb')
f1 = open('CTFLearn.txt', 'rb')
f2 = open('Result.txt', 'a')

for line in f:
    for char in line:
        s = f1.read(1)
        temp = (chr(ord(char)^ord(s)))
        f2.write(temp)

f.close()
f1.close()
f2.close()
