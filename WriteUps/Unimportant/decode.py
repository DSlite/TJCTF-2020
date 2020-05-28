from PIL import Image
import binascii

img = Image.open("6996b9ea93971d907329dd61be2a22c50e7608d6c183bfe66bbb621ac338b51b_unimportant.png")
pixels = img.load()

a= []
i = 0
for x in range(img.width):
    for y in range(img.height):
        pixel = pixels[x, y]
        a += [str((pixel[1]>>1)&1)]
        i += 1
        if i == 503:
            break
    if i == 503:
        break

a="".join(a)
a = "0b"+a

n = int(a, 2)
print(binascii.unhexlify('%x' % n))
