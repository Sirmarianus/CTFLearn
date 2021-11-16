def xor_binary(x, y):
    ss = ''
    for j in range(8):
        ss += str(int(x[j])^int(y[j]))
    return ss

f = open('binary')

s = list('CTFlearn{')
print(s)

for i in range(9):
    x = f.read(8)
    print('-----------------------')
    print(x, end='')
    print('  ->  ', end='')
    x_int = int(x, 2)
    print(x_int, end='')
    print('  ->  ', end='')
    print(chr(x_int))


    y = f'{ord(s[i]):08b}'
    print(y, end='')
    print('  ->  ', end='')
    y_int = int(y, 2)
    print(y_int, end='')
    print('  ->  ', end='')
    print(chr(y_int))

    ss = xor_binary(x, y)
    print(ss)

# getting xor's together and finding out key