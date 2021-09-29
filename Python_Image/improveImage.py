from PIL import Image

''' 用python提高图片像素

'''

def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)


if __name__ == '__main__':
    file_in = "LittleDemo/GetBiliBiliBarrage/lbxx.png"
    # 处理后图片宽度
    width = 5000
    # 处理后图片高度
    height = 5000
    file_out = 'LittleDemo/GetBiliBiliBarrage/lbxx.png'
    produceImage(file_in, width, height, file_out)
