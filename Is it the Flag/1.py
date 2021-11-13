def hash_code(a, b, c, d, e, f):
    hash = ord(a)*31**5 + ord(b)*31**4 + ord(c)*31**3 + ord(d)*31**2 + ord(e)*31 + ord(f)
    return hash

alphanurerics = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
for i in {'0', '1'}:
    for j in alphanurerics:
        for k in alphanurerics:
            for m in alphanurerics:
                for n in alphanurerics:
                    for o in alphanurerics:
                        a = i
                        b = j
                        c = k
                        d = m
                        e = n
                        f = o
                        y = hash_code(a, b, c, d, e, f)
                        x = 1472541258
                        if (x == y):
                            print("--------------")
                            print(y)
                            print(a, end='')
                            print(b, end='')
                            print(c, end='')
                            print(d, end='')
                            print(e, end='')
                            print(f)

# 0ghzxy