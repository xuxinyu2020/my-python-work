#!/bin/bash
#Program:
# 用于在pod中查询glance名称信息



# 检查是否有最终的结果文件，有则删掉
if [ -f glance_image_info.txt ];then
  rm glance_image_info.txt
fi
image_id=$(cat result.txt | awk 'print $1')
for im in ${image_id[@]}
do
  im_name=$(openstack image show $im  | grep name | awk '{print $4}'|head -n 1)
  echo "$im $im_name" >> glance_image_info.txt
done