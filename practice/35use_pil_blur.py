from PIL import Image, ImageFilter

image = Image.open('R-C.jpg')
# 应用模糊滤镜
image2 = image.filter(ImageFilter.BLUR)
image2.save('R-C-blur.jpg')