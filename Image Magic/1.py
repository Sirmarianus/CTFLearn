from PIL import Image

with Image.open('in.jpg') as im:
    px = im.load()

with Image.open('base.jpg') as img:
    px_out = img.load()

for i in range (27968):
    y = i%92
    x = i//92
    px_out[x,y] = px[i,0]
img.save('out.jpg')