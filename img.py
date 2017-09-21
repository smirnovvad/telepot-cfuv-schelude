from PIL import ImageFont
from PIL import Image, ImageDraw

font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 16)

# draw.text((0, 0), "This is a test", (0, 0, 0), font=font)


def render(xy, text, fill, chat_id):
    img = Image.new("RGBA", (650, 200), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.multiline_text(xy, text[:-1], fill, font=font)
    #draw.line((0, 50, 700, 50), fill='black', width=3)
    draw = ImageDraw.Draw(img)
    img.save('img/%d.png' % chat_id)


'''
draw.chord((500, 750, 700, 100), 0, 360, fill='green')
draw.chord((75, 100, 100, 125), 0, 180, fill='blue')
draw.chord((125, 125, 150, 150), 0, 360, fill='yellow')
draw.line((0, 50, 500, 50), fill='yellow', width=5)
'''
