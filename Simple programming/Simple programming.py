wynik = 0
f = open('data.dat')
for line in f:
    zera = 0
    jedynki = 0
    s = line.strip()
    for letter in s:
        if letter == '1':
            jedynki += 1
        elif letter == '0':
            zera += 1
    if zera%3 == 0 or jedynki%2 == 0:
        wynik += 1
print(wynik)
