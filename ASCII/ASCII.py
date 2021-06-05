s = input().split()
wynik = ''
for i in range(len(s)):
    s[i] = int(s[i], 16)
    wynik += str(chr(s[i]))
print(wynik)
