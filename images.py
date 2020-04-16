# %%
from PIL import Image, ImageDraw, ImageFont
from os import listdir


def create_super_image(image_path: str, logo_path: str, qr_code_path: str, output: str, im_width=800):
    """
    :param image_path: путь к изображению
    :param logo_path: путь к логотипу
    :param qr_code_path: путь к qr коду
    :param output: место и название, где будет сохранено изображение. пример: images/im1.jpg
    :param im_width: ширина выходного изображения. НЕ ниже 480 или выбросит ошибку
    :return: None
    """
    image_path = Image.open(image_path)
    logo_path = Image.open(logo_path)
    qr_code_path = Image.open(qr_code_path)

    assert im_width >= 480, RuntimeError("Small size")
    im_height = im_width * image_path.size[1] // image_path.size[0]
    image_path = image_path.resize((im_width, im_height), Image.ANTIALIAS)

    lo_width = im_width // 10
    lo_height = lo_width * logo_path.size[1] // logo_path.size[0]
    logo_path = logo_path.resize((lo_width, lo_height), Image.ANTIALIAS)

    qr_code_path = qr_code_path.resize((100, 100), Image.ANTIALIAS)

    if image_path.size[1] > image_path.size[0]:
        image_path = image_path.rotate(180)

    idraw = ImageDraw.Draw(image_path)
    date = image_path.getexif().get(36867).split()[0]
    text = "Сергей Соколов"
    font = ImageFont.truetype("arial.ttf", size=18)
    idraw.text((im_width // 2 - 125, im_height - 25), f"{text} {date}", font=font)

    image_path.paste(logo_path, (im_width - lo_width, 0), logo_path)
    image_path.paste(qr_code_path, (0, 0))

    # image_path.show()
    image_path.save(output)


# %%
files = listdir('images')
for file in files[:]:
    if '.jpg' not in file:
        files.remove(file)
    else:
        create_super_image(f'images/{file}', 'images/logo.png', 'images/qr.png', f'images/out/{file}', im_width=1000)
