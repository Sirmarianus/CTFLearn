f = open("Flaga.txt")
b = open("f.txt", 'w')
for line in f:
    x = line.replace("255", "")
    b.write(x)
