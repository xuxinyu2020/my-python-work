import socket
import threading
import time
# 创建一个基于IPv4和TCP的socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定要监听的客户端IP和端口，127.0.0.1代表只有本机可以连接
s.bind(('127.0.0.1', 9999))
# 监听端口，等待连接的最大数是5
s.listen(5)
print('Waiting for connection...')


def tcplink(sock, addr):
    print('Accept new connection from %s:%s' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed' % addr)


while True:
    # 接收新的连接
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
