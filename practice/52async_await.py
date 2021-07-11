import asyncio
"""参考博客：https://www.jianshu.com/p/eed5da9965f2"""


async def wget(host):
    print("开始爬虫 %s" % host)
    # 创建 TCP 客户端并连接服务器，或者说创建一个 TCP 连接对象
    # open_connection 接收两个参数：主机和端口号
    # connect 是协程，这步仅是创建协程对象，立即返回，不阻塞
    connect = asyncio.open_connection(host, 80)
    # 连接创建成功后，asyncio.open_connection 方法的返回值就是读写对象
    # 读写对象分别为 StreamReader 和 StreamWriter 实例
    # 它们也是协程对象，底层调用 socket 模块的 send 和 recv 方法实现读写
    reader, writer = await connect
    # header 是发送给服务器的消息，意为获取页面的 header 信息
    # 这个格式是固定的
    header = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % host
    # 给服务器发消息，注意消息是二进制的
    writer.write(header.encode('utf-8'))
    # 这是一个与底层 IO 输入缓冲区交互的流量控制方法
    # 当缓冲区达到上限时，drain() 阻塞，待到缓冲区回落到下限时，写操作恢复
    # 当不需要等待时，drain() 会立即返回，例如上面的消息内容较少，不会阻塞
    # 这就是一个控制消息的数据量的控制阀
    await writer.drain()
    print('%s ok' % host)
    # 给服务器发送消息后，就等着读取服务器返回来的消息
    while True:
        line = await reader.readline()
        # 数据接收完毕，会返回空字符串 \r\n ，退出 while 循环，结束数据接收
        if line == b'\r\n':
            break
        # 接收的数据是二进制数据，转换为 UTF-8 格式并打印
        # rstrip 方法删掉字符串的结尾处的空白字符，也就是 \n
        print('%s header >%s' % (host, line.decode('utf-8').rstrip()))
    writer.close()  # 关闭数据流，可以省略


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
