from PIL import Image, ImageDraw, ImageFont


str_hineses = ['鲍', '文', '杰']
start, end = (0x4E00, 0x9FD5)  # 汉字编码的范围,20950个汉字

# for codepoint in range(int(start), int(end)+1):
#     str_hineses.append(chr(codepoint))

img = Image.new('RGB', (4096, 4096), (255, 255, 255))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('simsun.ttc', 4096)

for str_hinese in str_hineses:
    draw.text((0, 0), str_hinese, fill=(0, 0, 0), font=font)

img.show()
img.save('C:/Users/WILL/Desktop/img.jpg')
