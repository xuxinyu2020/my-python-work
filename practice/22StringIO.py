from io import StringIO, BytesIO

# 在内存中读写str
f = StringIO()
f.write('Hello')
f.write(' ')
f.write('World!')
print(f.getvalue()) # Hello World!

g = StringIO('Hello\nWorld\n!!!')
while True:
    s = g.readline()
    if s == '':
        break
    print(s.strip())

# 在内存中读写二进制数据
h = BytesIO()
h.write('开心'.encode('utf-8'))
print(h.getvalue())

j = BytesIO(b'\xe5\xbc\x80\xe5\xbf\x83')
print(j.read())
