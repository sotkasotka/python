from PIL import Image

ris = Image.open("p19\city.jpg")

width, height = ris.size

pixels = list(ris.getdata())

red = sum([pixel[0] for pixel in pixels]) // len(pixels)
green = sum([pixel[1] for pixel in pixels]) // len(pixels)
blue = sum([pixel[2] for pixel in pixels]) // len(pixels)

print("Средние значения R, G, B:", red, green, blue)

n_image = Image.new("RGB", (width, height), (red, green, blue))
n_image.save("p19\city2.jpg")

n_image.show()