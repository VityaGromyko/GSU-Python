# %%
from PIL import Image, ImageDraw, ImageFont
import os

canvas = Image.new('RGB', (1800, 600))
idraw = ImageDraw.Draw(canvas)

images = []
path_images = '/home/vitya/IT/GSU/Python/images2/'
for path in os.listdir(path_images):
    if os.path.isfile(path_images + path):
        images.append(Image.open(path_images + path))

images = sorted(images, key=lambda x: x.getexif().get(34855))

for i, image in enumerate(images):
    image = image.rotate(-90)
    image = image.resize((image.size[0]//3, image.size[1]//3))
    image = image.crop((625, 10, 925, 610))

    images[i] = image

    canvas.paste(image, (300 * i, 0))
    idraw.text(
        (300 * i + 100, 580),
        f'ISO:{image.getexif().get(34855)}',
        font=ImageFont.truetype("arial.ttf", size=18),
        fill=(25, 255, 0)
    )

canvas.show()
canvas.save(path_images + 'out/123.jpg')



