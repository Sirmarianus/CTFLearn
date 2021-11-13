counter = 0
pattern = [2,2,1,2,2,2,1]
f = open('input')
for line in f:
    tab = []
    splitted_line = line.split()
    for char in splitted_line:
        if(char == 'C' or char == 'B#'):
            tab.append(1)
        if(char == 'C#' or char == 'Db'):
            tab.append(2)
        if(char == 'D'):
            tab.append(3)
        if(char == 'D#' or char == 'Eb'):
            tab.append(4)
        if(char == 'E' or char == 'Fb'):
            tab.append(5)
        if(char == 'F' or char == 'E#'):
            tab.append(6)
        if(char == 'F#' or char == 'Gb'):
            tab.append(7)
        if(char == 'G'):
            tab.append(8)
        if(char == 'G#' or char == 'Ab'):
            tab.append(9)
        if(char == 'A'):
            tab.append(10)
        if(char == 'A#' or char == 'Bb'):
            tab.append(11)
        if(char == 'B' or char == 'Cb'):
            tab.append(12)
    tab.sort()

    for i in range(len(tab)-1):
        if(tab[i] == tab[i+1]):
            tab.extend(tab[:i+1])
            tab = tab[i+1:]
            
    diff = []
    for i in range(7):
        temp = tab[i+1] - tab[i]
        if(temp < 0):
            temp += 12
        diff.append(temp)           

    if(diff == pattern):
        counter += 1
print(counter)