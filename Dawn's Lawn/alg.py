def zamiana(x):
    if x == '.':
        return 1
    elif x == '_':
        return 2
    elif x == '\\':
        return 3
    elif x == '-':
        return 4
    elif x == '/':
        return 5
    elif x == '|':
        return 6
    elif x == '*':
        return 7
    else:
        return 0

f = open("dawn2.txt")
N = int(input())
tab = [0] * N
for i in range(N):
    tab[i] = [0]*N

for i in range(N):
    Linia = f.readline()
    for j in range(N):
        tab[i][j] = zamiana(Linia[j])

X = 0
for j in range(N):
    for i in range(N):
        tab[i][j] -= 2
        if (tab[i][j] > 1):
            tab[i][j] += N-(j+1)
            if (tab[i][j] >= 7):
                tab[i][j] = 7
                X += 1
        else:
            tab[i][j] = 1

for i in range(N):
    print(tab[i])
print(X)
