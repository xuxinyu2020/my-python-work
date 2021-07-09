"""使用PIL生成验证码图片"""
# 定义图片的大小
import random

from PIL import Image, ImageFont, ImageDraw, ImageFilter


# 生成背景颜色
def bg_color():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
# 生成文字颜色
def txt_color():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
# 生成验证码大写字母
def code_char():
    return chr(random.randint(65,90))

width = 60*4
height = 60
# 新建image对象,白底
image = Image.new(mode='RGB',size=(width,height),color=(255,255,255))
# print(image)
# image.save('new-image.jpg')
# 创建font对象
font = ImageFont.truetype(font='arial.ttf',size=36)
# print(font)
# 创建draw对象
draw = ImageDraw.Draw(image)
# 填充像素。画底色
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=bg_color())

# 画验证码文字
for i in range(4):
    draw.text(xy=(10+60*i,10),text=code_char(),fill=txt_color(),font=font)

# 模糊图片
image=image.filter(ImageFilter.BLUR)
# 保存图片.save('code.jpg')
image.save('code.jpg')
print('验证码生成！')