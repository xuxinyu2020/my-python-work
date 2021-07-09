"""PIL图片缩放"""
from PIL import Image

image = Image.open("R-C.jpg")
# 获取图像尺寸
width, height = image.size
print('图片尺寸是：%sx%s'%(width,height))
# 缩放到50%
image.thumbnail((width/2,height/2))
print('图片现在的尺寸是：%sx%s'%(width/2,height/2))
# 图片保存
image.save('New-R-C.jpg')
