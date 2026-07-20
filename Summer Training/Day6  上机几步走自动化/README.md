昨天写了一个上机几步走的shell，今天打算把它自动化了，顺便创建一个日志文件，每天定时输出到那里

使用自动化之前先查看一下Linux里有没有装cron，用systemctl status cron查看一下，没有就sudo apt update更新一下然后sudo apt install cron -y

安装完之后crontab -e就会弹出来一个界面，在最底下写要自动化的文件就行了

格式如下

分钟，小时，日，月，星期，文件路径



补充一个之前写shell的小瑕疵，如果开头加了shebang，也就是#！/bin/bash，执行文件的时候就不需要再加bash，但是文件需要有可执行的权限

区分一下两种命令：第一种有shebang的，直接./文件路径就行，第二种有可执行权限但是没有shebang，就需要bash  文件路径