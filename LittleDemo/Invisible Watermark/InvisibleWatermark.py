""" 给照片添加隐形水印
@Author: Bao Wenjie
@Date: 2020/8/6
@Email: bwj_678@qq.com
"""
from PIL import Image


class InvisibleWatermark:
    def __init__(self):
        super().__init__()

    def __makeImageEven(self, image):
        """ 将PIL图像所有值变成偶数
        """
        # (r, g, b)
        pixels = list(image.getdata())
        evenPixels = [(r >> 1 << 1, g >> 1 << 1, b >> 1 << 1) for [r, g, b] in pixels]
        evenImage = Image.new(image.mode, image.size)
        evenImage.putdata(evenPixels)
        return evenImage

    def __constLenBin(self, int_):
        """ 去掉bin()返回的二进制字符串的'0b',并在左边补足'0'直到字符串长度为8
        """
        binary = "0"*(8-(len(bin(int_)) - 2)) + bin(int_).replace('0b', '')
        return binary

    def __encoderDataToIamge(self, image, data):
        """ 将字符串编码进图片
        @param image: 图片
        @param data(str): 待编码的信息
        @return image: 编码好的信息
        """
        evenImage = self.__makeImageEven(image)
        binary = ''.join(map(self.__constLenBin, bytearray(data, 'utf-8')))
        if(len(binary) > len(image.getdata()) * 3):
            raise Exception('在此图像中不能编码超过'+len(evenImage.getdata() * 3) + '位')
        encodedPixels = [(r + int(binary[index*3+0]),
                          g + int(binary[index*3+1]),
                          b + int(binary[index*3+2]))
                         if index*3 < len(binary) else (r, g, b)
                         for index, (r, g, b) in enumerate(list(evenImage.getdata()))]
        encodedImage = Image.new(image.mode, image.size)
        encodedImage.putdata(encodedPixels)
        return encodedImage

    def __binaryToString(self, binary):
        """ 将二进制字符串变成UTF-8
        @param binary(str): 二进制字符串
        """
        string = []
        for i in range(len(binary) // 8):
            string.append(int(binary[8*i:8*i + 8], 2))
        string = bytearray(string)
        return string.decode('utf-8')

    def _decodeImage(self, image):
        """ 解码图片
        """
        pixels = list(image.getdata())
        binary = ''.join([str(int(r >> 1 << 1 != r)) +
                          str(int(g >> 1 << 1 != g)) +
                          str(int(b >> 1 << 1 != b))
                          for (r, g, b) in pixels])
        locationDoubleNull = binary.find('0'*8)
        locationDoubleNull = 120
        endIndex = locationDoubleNull + (8 - (locationDoubleNull % 8)) if locationDoubleNull % 8 != 0 else locationDoubleNull
        data = self.__binaryToString(binary[:endIndex])
        return data

    def encodeImage(self, src_path, tar_path, data):
        """ 编码图片
        @param src_path(str): 源路径
        @param tar_path(str): 目标路径
        @param data(str): 待编码信息
        """
        image = Image.open(src_path)
        image_ = self.__encoderDataToIamge(image, data)
        image_.save(tar_path, quality=100)
        return image_

    def decodeImage(self, src_path):
        """ 解码图片
        @param src_path(str): 源路径
        @return data(str): 编码信息
        """
        image = Image.open(src_path)
        data = self._decodeImage(image)
        return data


if __name__ == '__main__':
    test = InvisibleWatermark()
    image = test.encodeImage('C:\\Users\\WILL\\Pictures\\bk.jpg', 'C:\\Users\\WILL\\Pictures\\bkk.png', '哈哈哈哈哈')
    print(test.decodeImage('C:\\Users\\WILL\\Pictures\\bkk.png'))
    # print(test._decodeImage(image))
    # image.show()
