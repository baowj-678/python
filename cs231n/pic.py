from PIL import Image
import numpy as np
# import scipy
import matplotlib.pyplot as plt

def ImageToMatrix(filename):
    # 读取图片
    im = Image.open(filename)
    # 显示图片
    im.show()
    width,height = im.size
    im = im.convert("RGB") 
    data = im.getdata()
    data = np.matrix(data,dtype='float')/255.0
    new_data = np.reshape(data, (-1, width, height))
    return new_data

def MatrixToImage(data):
    data = data*255
    new_im = Image.fromarray(data.astype(np.uint8))
    return new_im



filename = 'C:\\Users\\WILL\\Pictures\\Windows聚焦壁纸\\RE1LBvN_1920x1080.jpg'
data = ImageToMatrix(filename)
print(data.shape)
data=data.transpose()
new_im = MatrixToImage(data)
plt.imshow(data, cmap=plt.cm.gray, interpolation='nearest')
new_im.show()

# new_im.save('lena_1.bmp')