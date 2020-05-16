from PIL import Image, ImageDraw, ImageFont

# 利用pyhton将几个文字重叠起来显示


# start, end = (0x4E00, 0x9FD5)  # 汉字编码的范围,20950个汉字
# for codepoint in range(int(start), int(end)+1):
#     str_hineses.append(chr(codepoint))

size = 10240
# str_hineses = ['鲍', '文', '杰']
img = Image.new('RGB', (size, size), (255, 255, 255))
draw = ImageDraw.Draw(img)
# SIMYOU.TTF为幼圆字体文件，SIMLI.TTF为隶书字体文件，STXINGKA.TTF为行楷字
font = ImageFont.truetype('simkai.ttf', size)

# for str_hinese in str_hineses:
#     draw.text((0, 0), str_hinese, fill=(0, 0, 0), font=font)

draw.text((0, 0), '鲍', fill=(255, 0, 0), font=font)
draw.text((0, 0), '文', fill=(0, 255, 0), font=font)
draw.text((0, 0), '杰', fill=(0, 0, 255), font=font)

img.show()
img.save('C:/Users/WILL/Desktop/baowenjie_kai.jpg')
