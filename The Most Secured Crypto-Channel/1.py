# f2 is not needed
f1 = open('transmission1.txt')
#f2 = open('transmission2.txt')
f3 = open('transmission3.txt')


l1 = list(f1.readline())
#l2 = list(f2.readline())
l3 = list(f3.readline())
l11 = []
#l22 = []

for i in range(len(l3)):
    if (ord(l3[i]) == 118):
        l11.append(l1[i])
        #l22.append(l2[i])
s = ''
for char in l11:
    if(char == '-' or char == '/'): # why tf is '-' 0 ?
        s += '0'
    else:
        s += '1'
print(s)
f4 = open('OUT', "w")
f4.write(s)