f = open('input.txt')

tab = []
tab.append(0)

for line in f:
    for char in line:
        i = ord(char)
        if (i == 43):
            tab[len(tab)-1] += 1
        elif (i == 46):
            tab.append(tab[len(tab)-1])
        elif (i == 45):
            tab[len(tab)-1] -= 1
        elif (i == 62):
            tab.append(tab.pop(0))
        elif (i == 64):
            temp = tab[len(tab)-1]
            tab[len(tab)-1] = tab[len(tab)-2]
            tab[len(tab)-2] = temp
        elif (i == 60):
            tab.insert(0, tab.pop())
for ele in tab:
    print(chr(ele), end='')