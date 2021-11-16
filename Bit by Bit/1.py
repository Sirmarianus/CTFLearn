s = 'binaryrefinery'
x = list('|&&>|^^^&&||~')

table = []

for char in s:
    temp = (pow(ord(char), 3))
    table.append(temp)
    #table.append(f'{temp:08b}')

out = table[0]
for i in range(len(x)):
    for j in range(i, len(x)):
        if(x[j] == '>'):
            out = out >> table[j+1]
        elif(x[j] == '^'):
            out = out ^ table[j+1]
        elif(x[j] == '|'):
            out = out | table[j+1]
        elif(x[j] == '&'):
            out = out & table[j+1]
        elif(x[j] == '~'):
            out = ~out
print(out)