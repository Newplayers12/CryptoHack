from PIL import Image


p1 = Image.open('flag.png')
p2 = Image.open('lemur.png')

print(p1.size, p2.size)

d1 = p1.load()
d2 = p2.load()
xor_img = Image.new('RGB', p1.size)
for x in range(p1.width):
    for y in range(p1.height):
        r1, g1, b1 = d1[x, y]
        r2, g2, b2 = d2[x, y]
        x_r, x_g, x_b = r1 ^ r2, g1 ^ g2, b1 ^ b2
        xor_img.putpixel((x, y), (x_r, x_g, x_b))
# ans = Image.new('RGB', p1.size)

xor_img.save('ans.png')
