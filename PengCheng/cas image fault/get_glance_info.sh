#!/bin/bash
#Program:
# 用于查询result.txt文件中的glance名称信息
#History:
# 2021/8/19  xuxinyu   v1.0 
#Readme：
# 需要使用check_image.sh查询得到result.txt文件
#检查当前文件夹下是否有result.txt文件，否则退出
if [ ! -f result.txt ];then
  echo "当前文件夹下缺少result.txt文件"
  exit 1
fi
#将result.txt和脚本文件拷贝进入glance的pod的opt目录下
kubectl cp  result.txt cloudos-iaas/os-glance-0:opt
kubectl cp  openstack_image.sh cloudos-iaas/os-glance-0:opt
# 在pod中执行目录下，执行命令
kubectl exec -it os-glance-0 -n cloudos-iaas -- source /root/admin-openrc.sh;cd /opt;sh openstack_image.sh
# 退出pod，并将结果文件拷贝到当前文件夹下
kubectl cp  cloudos-iaas/os-glance-0:opt/glance_image_info.txt .
if [ $? == 0 ];then
  echo "脚本执行成功，请到glance_image_info.txt中查看结果"
fi




