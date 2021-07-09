import psutil as psutil
# 获取Cpu逻辑个数
cpu_num = psutil.cpu_count()
print(cpu_num)
# 获取cpu物理核心
cpu_core = psutil.cpu_count(logical=False)
print(cpu_core)
#统计CPU的用户／系统／空闲时间
cpu_time = psutil.cpu_times()
print(cpu_time) # scputimes(user=76057.90625, system=70410.3125, idle=277266.234375, interrupt=2759.546875, dpc=1303.53125)

# 实时刷新cpu利用率
# for i in range(10):
#     print(psutil.cpu_percent(interval=1,percpu=True))


# 获取内存信息
# 物理内存
print(psutil.virtual_memory()) # svmem(total=17053683712, available=381485056, percent=97.8, used=16672198656, free=381485056)
# 交换内存
print(psutil.swap_memory()) # sswap(total=23496134656, used=19628974080, free=3867160576, percent=83.5, sin=0, sout=0)


# 获取磁盘信息
# 获取磁盘使用情况
print(psutil.disk_usage('C:')) #sdiskusage(total=128850063360, used=119052767232, free=9797296128, percent=92.4)
# 获取磁盘分区情况
print(psutil.disk_partitions())


# 获取网络信息
print(psutil.net_io_counters()) # 获取网络读写字节／包的个数
print(psutil.net_if_addrs()) # 获取网络接口信息
print(psutil.net_if_stats()) # 获取网络接口状态
print(psutil.net_connections()) # 当前网络连接信息

# 获取进程
print(psutil.pids())
p = psutil.Process(1868)
print(p.name())
# print(p.cwd())
print(p.ppid())
print(p.parent())
print(p.children())
print(p.status())
# print(p.username())
print(p.create_time())
# print(p.terminal())
print(p.cpu_times())