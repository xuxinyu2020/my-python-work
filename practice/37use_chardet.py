import chardet

result=chardet.detect(b'Hello World!')
print(result)
data = '今天，我们开始学习一门新的编程语言，首先大家先翻开课本的234页'.encode('utf-8')
result = chardet.detect(data)
# {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
print(result)
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
data = '今天，我们开始学习一门新的编程语言'.encode('gbk')
result = chardet.detect(data)
print(result)
# {'encoding': 'GB2312', 'confidence': 0.99, 'language': 'Chinese'}

