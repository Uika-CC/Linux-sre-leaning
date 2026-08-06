#2026/8/6

一句话概括今日：用Python的sub模块，函数，If语句构成的自愈脚本，结合到main.py里，Docker封装整个环境

核心特性：有了自愈系统的存在就不需要人工去重载服务，main.py有巡检，告警，自愈的功能，Docker封装环境之后可以随意操作，也不需要担心环境的影响导致服务跑不起来



关于镜像加速器：阿里云有免费的镜像加速器，我是用snap安装的docker，所以在/var/snap/docker/current/config/下新建一个daemon.json文件，文件内容我截图了，阿里云里也有文档可以参考

国内公共镜像源(来自DaoCloud，国内访问比较稳定)：

sudo docker pull docker.m.daocloud.io/library/python:3.12

命令执行成功后只需要把dockerfile的FROM行换成：

FROM docker.m.daocloud.io/library/python:3.12

改完之后同样可以去/var/snap/docker/current/config/把"https://docker.m.daocloud.io”设置成默认的加速器，之后就可以直接sudo docker pull python:3.12直接拉取了



 