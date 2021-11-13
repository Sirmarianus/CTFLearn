from PIL import Image
import numpy as np
import csv

dane = []

with open('the_data_scientist.csv') as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        dane.append(row)

with Image.open('1.jpg') as img:
    px = img.load()
for i in range(256):
    for j in range(53):
        x = dane[i][j]
        if(x <= 65 and x >= 64):
            px[j,i] = (0,0,0)


img.save('out.jpg')