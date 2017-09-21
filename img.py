from PIL import ImageFont
from PIL import Image, ImageDraw

font = ImageFont.truetype("teen.ttf", 30)
img = Image.new("RGBA", (500, 500), (255, 255, 255))
draw = ImageDraw.Draw(img)
#draw.text((0, 0), "This is a test", (0, 0, 0), font=font)


def render(text, x, y):
    pass
draw.chord((500, 750, 700, 100), 0, 360, fill='green')
draw.chord((75, 100, 100, 125), 0, 180, fill='blue')
draw.chord((125, 125, 150, 150), 0, 360, fill='yellow')
draw.line((0, 50, 500, 50), fill='yellow', width=5)
draw.text((0, 75), 'Sunday', fill='green', font=font)
draw = ImageDraw.Draw(img)

img.save("test.png")
