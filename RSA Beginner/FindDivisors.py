import math

f = open("n.txt", 'r')
L = int(f.readline())
print(L)

sqr = int(math.sqrt(L) + 1)
print(sqr)

i = int(math.sqrt(sqr))
while(i < sqr):
    if(L%i == 0):
        print('---------------------')
        print(i)
        print(L/i)
    i+=1
