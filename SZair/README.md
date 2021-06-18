# my_python_work
保存学习python过程中的一些脚本
通过调用API接口，统计信息完成客户需求报表

脚本用途：
	imc_alarm_statics.py  用于统计某段时间内紧急和重要告警总次数超过3次的设备信息，并输出excel表格。（目前主要针对设备和应用告警做过测试）
	imc_monitor_statics.py 用于统计imc当前监控的设备和应用数量

脚本使用方法：
1.使用前提：安装python3.x和相关扩展包。
	python需要手动下载并安装，安装方式自行百度。
	python安装完成后，双击执行pre_script.bat。注意此时需要可连接外网

2.修改python脚本参数：
	将脚本中imc_url换成现场实际imc地址，username和passwords参数分别修改成实际imc账号和密码

3.执行脚本：
	1. 将脚本拷贝到电脑任意目录下，
	2.Ctrl+R，输入cmd，回车，打开命令界面
	3.进入脚本所在文件夹
	4.执行脚本，命令为：python imc_monitor_statics.py
			 python python alarm_statics.py 2021/5/23_17:19:00 2021/5/23_17:30:00
	5.执行成功后，即可在脚本所在文件夹下生成excel报告

注意：1.执行alarm_static.py脚本需要跟查询告警的起始时间参数，值可根据需要调节。时间格式要严格按照例子中的书写：年/月/日_时:分:秒
          2.第一次使用需要做使用方法的前两步，以后每次使用可直接执行脚本
