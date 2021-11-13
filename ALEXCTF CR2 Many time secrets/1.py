def xor(a, b):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))

def help_find_key(msgs):
    key = 'ALEXCTF{'
    max_len = max(map(len, msgs))
    while True:
        print '\n>>', key.encode('string-escape')
        for i, msg in enumerate(msgs):
            print '%-2d' % i, xor(key, msg)
        if len(key) == max_len:
            break
        i = int(raw_input('\nline: '))
        c = raw_input('char: ')
        key += xor(msgs[i][len(key)], c)

with open('msg') as f:
    help_find_key([x.strip().decode('hex') for x in f])