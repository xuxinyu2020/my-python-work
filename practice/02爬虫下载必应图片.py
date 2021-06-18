# /th?id=OHR.BrazilSandDunes_ZH-CN2924749051_1920x1080.jpg&amp;rf=LaDigue_1920x1080.jpg&amp;pid=hp

import re
from datetime import datetime
from urllib import parse
import requests

# 获取必应的网站回应
url = "https://cn.bing.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
r = requests.get(url=url, headers=headers)
print(r)
# 正则表达式匹配url
a = re.findall(r'id="bgLink" rel="preload" href="(.*?)" as="image"', r.text)
print(a)

# 组合图片下载url，并写入文件
if a:
    pic_url = parse.urljoin(url, a[0])
    print(pic_url)
    biying_pic = requests.get(url=pic_url, headers=headers)
    pic_name = "biying_pic" + datetime.now().strftime("%Y%m%d") + ".jfif"
    with open(f'biying_pic\\{pic_name}', 'wb') as f:
        f.write(biying_pic.content)
        print("图片下载成功！")

'''注意：
re.match只从待匹配的字符串或文本的开头开始匹配，即如果匹配的字符串不在开头，而是在中间或结尾，则无法匹配！
match返回的时match object；而findall返回的是匹配到的元素列表！
'''
'''
本次练习涉及requests，正则表达式，datetime的用法。
'''
