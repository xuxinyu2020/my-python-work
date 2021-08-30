#!/bin/bash
#Program:
# 用于校验镜像列表中的镜像id在glance存储卷内是否存在
#History:
# 2021/8/18  xuxinyu   v1.0 
#Readme：
# 使用前，脚本所在目录需要进入glance的pod中通过openstack image list|awk 'NR>3{print $1}' > imagelist.txt获取到imagelist.txt文件。执行后，会在脚本所在文件夹下生成result.txt结果文件
#查看根目录下是否有结果文件，有则删除
workdir=$(pwd)
cd $workdir
if [ -f result.txt ];then
  rm result.txt 
fi
#找到glance的存储卷
glance_dir=$(df -hT | grep glance | awk '{print $7}')
if [ -z "$glance_dir" ];then
  echo "该节点不存在glance存储卷"
  exit 1
fi
#获取现在的镜像id
image_id=$(cat imagelist20210818.txt | awk '{print $1}')
cd $glance_dir
#检查镜像在存储卷中是否存在，并输出结果
for im in ${image_id[@]}
do
  if [ ! -f $im ];then
    echo "$im" >> $workdir/result.txt
  fi
done
if [ $? == 0 ];then
  echo "脚本执行成功，请到result.txt中查看结果"
fi
