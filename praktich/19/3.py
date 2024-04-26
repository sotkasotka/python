from PIL import Image
ris = Image.open("p19\hishniki.jpg")
width, height = ris.size
image = Image.new("RGB", (width, height))
for y in range(height):
    for x in range(width):
        xl = ris.getpixel((x, y))
        red, green, blue = xl

        min_rgb = min(red, green, blue)
        max_rgb2 = max(red, green, blue)

        new_red = min_rgb
        new_green = green
        new_blue = max_rgb2

        image.putpixel((x, height - y - 1), (new_red, new_green, new_blue))
image = image.transpose(Image.ROTATE_180)
image.save("p19\hishniki2.jpg")
image.show()