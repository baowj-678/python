from PIL import Image
# Image.MAX_IMAGE_PIXELS = None


def gray2ascii(r, g, b):
    gray = (r*0.299 + g*0.587 + b*0.114) / 255
    gray2char = [' ', '`', '.', '^', ',', ':', '~', '"', '<', '!', 'c',
                 't', '+', '{', 'i', '7', '?', 'u', '3', '0', 'p', 'w',
                 '4', 'A', '8', 'D', 'X', '%', '#', 'H', 'W', 'M']
    return gray2char[int(gray * (len(gray2char) - 1))]


def main(file_name: str, target_name: str, height=300, width=300):
    img = Image.open(file_name)
    if(height == 0):
        height = img.height
        width = img.width
    img.thumbnail((width, height))
    charas = []
    for h in range(height):
        chara_row = str([])
        for w in range(width):
            r, g, b = img.getpixel((w, h))
            chara_row += gray2ascii(r, g, b)
        chara_row += '\n'
        charas.append(chara_row)
    img.close()
    fp = open(target_name, 'w+')
    for y in range(height):
        fp.write(charas[y])
    fp.close()


if __name__ == '__main__':
    main('C:/Users/WILL/Desktop/b.jpg',
         'C:/Users/WILL/Desktop/baowenjie.txt',
         )
