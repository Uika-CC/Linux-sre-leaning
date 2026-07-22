昨天买的那本python自动化今天就到了，真的快啊，马上七月份也要结束了，今天是第八天了啊，前面一个星期感觉都是泛泛的学，剩下几天就打算把Linux的四大基础模块，也就是磁盘和文件系统，网络，内存管理，进程和日志这几块，还有shell收个尾

八月份就专门啃那本python了



今天的内容：

lsdlk：查看磁盘结构
输出内容解释：
一大堆的loop：Ubuntu用了snap软件包的镜像文件
fd0：软盘，虚拟机模拟出来的
sr0，1：ubuntu ISO的镜像文件
sda：用户的硬盘
disk：整块硬盘
part：分区
mountpoint：挂载点

fdisk -i：查看磁盘信息
df -h：查看文件系统使用情况
du -sh：查看目录占用空间

开始LVM之前需要知道的点：挂载和mount

windows和linux的一个区别：你在windows上插u盘，Windows会自动帮你挂载好，但是linux不会，因为linux整个系统就是一个目录树
Linux识别了u盘后，你不能直接cd进去，因为它还不是目录，这个时候就需要mount命令

sudo  mount  u盘路径  你想要挂载的路径

需要注意的一个点，挂载的目录必须的空目录，不然原来的文件会消失，想要找回来就需要umount  被mount的路径

额外插一条命令，格式化磁盘分区：mkfs.ext4 /dev/sdb1
							  作用：创建 ext4 文件系统（格式化）

最后再补充一点，mount只是临时挂载，重启服务器之后会直接失效
永久挂载：修改 /etc/fstab



LVM（如果没有要先sudo apt install lvm2）：

首先需要知道为什么需要LVM：普通磁盘分区的大小基本固定，但是如果想要加空间呢？这个时候就需要逻辑卷了

LVM的三个区域：
PV：物理卷，作用就是把一块普通硬盘声明成LVM可以管理的硬盘
命令：pvcreate  /dev/sdb

VG：卷组，也可以理解为资源池
命令：vgcreate data_vg /dev/sdb /dev/sdc
命令结果解释：/dev/sdb和/dev/sdc合并成为了data_vg，假设两个磁盘一个1TB，一个2TB，那么合并后就是3TB

LV：逻辑卷
作用：假设VG = 3TB，那么LV就可以将它划分为数个目录

LVM相关命令（现在主要知道LVM是什么，有什么用就行）

查看

pvs
vgs
lvs

创建

pvcreate
vgcreate
lvcreate

扩容

vgextend
lvextend