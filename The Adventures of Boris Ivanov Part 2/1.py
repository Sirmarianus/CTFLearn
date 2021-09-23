from PIL import Image

with Image.open('OUT.png') as im:
    px_out = im.load()



for i in range(500):
    with Image.open(str(i) + '.png') as img:
        px = img.load()
        for j in range(500):
            px_out[j,i] = px[j,0]
im.save('OUT.png')