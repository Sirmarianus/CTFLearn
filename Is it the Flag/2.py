def hash_code(a, b, c, d, e, f):
    hash = ord(a)*31**5 + ord(b)*31**4 + ord(c)*31**3 + ord(d)*31**2 + ord(e)*31 + ord(f)
    return hash

for i in {'0'}:
    for j in {'g', 'G'}:
        for k in {'h', 'H'}:
            for m in {'z', 'Z'}:
                for n in {'x', 'X'}:
                    for o in {'y', 'Y'}:
                        a = i
                        b = j
                        c = k
                        d = m
                        e = n
                        f = o
                        print(a+b+c+d+e+f)
                        print(hash_code(a, b, c, d, e, f))

# 0gHzxY
