from PIL import Image, ImageDraw
 
 
def picture(file_name, width, height, sky_color="#87CEEB", ocean_color="#017B92", boat_color="#874535",
            sail_color="#FFFFFF", sun_color="#FFCF40", beach="#fcdd76", sond="#5e481e"):
    im = Image.new("RGB", (width, height))
    drawer = ImageDraw.Draw(im)
    x, y = 100, 550
    a, b = 70, 500
    o, p = 0, 0
    o1, p1 = 30, 30
    o2, p2 = 60, 0
    o3, p3 = 90, 30
    o4, p4 = 120, 0
    o5, p5 = 150, 30
    drawer.rectangle(((0, 0), (width, int(height * 0.8))), sky_color)
    drawer.rectangle(((0, int(height * 0.7)), (width, height)),ocean_color)
    drawer.rectangle(((0, int(height * 0.85)), (width, height)),beach)
    drawer.ellipse((
        (int(0.8 * width), -int(0.2 * height)),
        (int(1.2 * width), int(0.2 * height))),sun_color)
    drawer.polygon(((int(0.20 * width), int(0.60 * height)),
                    (int(0.44 * width), int(0.60 * height)),
                    (int(0.44 * width), int(0.25 * height)),
                    (int(0.46 * width), int(0.25 * height)),
                    (int(0.46 * width), int(0.60 * height)),
                    (int(0.70 * width), int(0.60 * height)),
                    (int(0.65 * width), int(0.80 * height)),
                   (int(0.25 * width), int(0.80 * height))), boat_color)
    drawer.line([(x, y), (x, y + 200)], fill='brown', width=15)

    drawer.polygon([(a + -80, b + 100), (a + 35, b), (a + 150, b + 100)], fill='brown', outline='brown')
    
    drawer.ellipse([(o, p), (o + 100, p + 100)], fill='white', outline='black', width=1)
    drawer.ellipse([(o1, p1), (o1 + 100, p1 + 100)], fill='white', outline='black', width=1)
    drawer.ellipse([(o2, p2), (o2 + 100, p2 + 100)], fill='white', outline='black', width=1)
    drawer.ellipse([(o4, p4), (o4 + 100, p4 + 100)], fill='white', outline='black', width=1)
    drawer.ellipse([(o5, p5), (o5 + 100, p5 + 100)], fill='white', outline='black', width=1)
    drawer.ellipse([(o3, p3), (o3 + 100, p3 + 100)], fill='white', outline='black', width=1)
    
    
    
    
    
    


    drawer.polygon(((int(0.46 * width + 1), int(0.25 * height)),
                    (int(0.61 * width + 1), int(0.40 * height)),
                    int(0.46 * width + 1), int(0.55 * height)), sail_color)
    im.save(file_name)
 
 
picture('rss.jpg', 1000, 800)