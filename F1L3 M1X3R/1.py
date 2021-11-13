



ba = bytearray()
f = open('in.jpeg', "rb")
ba = f.read()
f.close()
outba = bytearray()
for i in range(0, len(ba), 4):
    outba.append(ba[i+3])
    outba.append(ba[i+2])
    outba.append(ba[i+1])
    outba.append(ba[i])


OUT = open('OUT.jpeg', "wb")
OUT.write(outba)