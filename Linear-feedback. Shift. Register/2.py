key = '00000101'
xor = '01101101'
f = open('binary')
out = ''

for i in range(40):
    char = f.read(8)
    new_char = ''
    for j in range(8):
        new_char += str(int(char[j])^int(key[j]))
    out += chr(int(new_char, 2))

    x = 2
    for j in range(8):
        rox = int(xor[j])
        yek = int(key[j])
        if (rox == 1):
            if (x == 2):
                x = yek
            else:
                x = x^yek
    temp = list(key)
    temp.insert(0, str(x))
    temp.pop(8)
    key = ''
    key = key.join(temp)
    temp.clear()
    print(key)
f.close()
print(out)
f = open('OUT', 'w')
f.write(out)