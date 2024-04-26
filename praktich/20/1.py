from PIL import Image, ImageDraw, ImageFont

width, height = 600, 200
img = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(img)

font_path = 'arial.ttf' 
font_size = 100
font = ImageFont.truetype(font_path, size=font_size)

x, y = 50, 50

#О
draw.ellipse([(x, y), (x + 100, y + 100)], fill='orange', outline='orange', width=15)

#Р
x += 110
draw.line([(x, y), (x, y + 100)], fill='blue', width=15)
draw.ellipse([(x, y), (x + 50, y + 50)], fill='blue', width=15)

#Х
x += 80
draw.line([(x, y), (x + 70, y + 100)], fill='green', width=15)
draw.line([(x + 70, y), (x, y + 100)], fill='green', width=15)

#А
x += 90
draw.polygon([(x, y + 100), (x + 35, y), (x + 70, y + 100)], fill='purple', outline='purple')
draw.line([(x + 10, y + 50), (x + 60, y + 50)], fill='purple', width=8)

#Н
x += 80
draw.line([(x, y), (x, y + 100)], fill='brown', width=15)     
draw.line([(x + 70, y), (x + 70, y + 100)], fill='brown', width=15)
draw.line([(x, y + 50), (x + 70, y + 50)], fill='brown', width=15) 

img.save('name.png')