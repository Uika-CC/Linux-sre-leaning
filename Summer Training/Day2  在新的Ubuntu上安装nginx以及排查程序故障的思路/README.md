原本的ECS上是有nginx的，自己的VMware上没有，而且ecs又过期了，现在只能重装了
顺带也复习一下软件安装吧，今天复习的命令
sudo systemctl status  	查看状态
ss -tnlp	通常配合管道符和grep使用，用来查看程序进程以及是否启动
sudo apt install () —y  Ubuntu安装软件
curl	本地快速访问网站用的，要事先安装

自己主要需要会看的几种错误：

permission denied（权限问题）

address already in use（端口被占用）

syntax error（配置语法错误）

排查网站打不开这类问题的思路：
服务是否运行		sudo systemctl status
端口是否监听		ss -tnlp
本机是否能访问	curl ip
防火墙			如果是ecs额外需要考虑安全组有没有开放端口，如果有开放在检查本机的防火墙，现在已知的只有ufw

查看错误日志		tail -n 20 /var/log/nginx/error.log
实时追踪			tail -f /var/log/nginx/error.log
（虽然现在还完全不会看日志...）