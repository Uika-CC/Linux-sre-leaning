今天是26年7月26日，昨天那个内存其实没咋学，因为昨天莫名的累，反正以后用到了再补吧

今天的内容：

进程相关

ps aux：最经典的查看进程命令，通常配合grep使用，比如说  ps aux | grep nginx

htop：现代多用的动态查看进程命令，要提前安装

kill  PID：杀进程
kill -9 PID：强制杀掉

&：后台运行，比如  python  app,py &
jobs：查看后台运行的进程
fg：恢复后台进程

pstree：查看进程树



日志相关

journalctl：查看全部日志（少用）

journalctl -u nginx：查看nginx的日志，也可以是其他服务的，比如mysql，ssh

journalctl -f：实时查看日志

journalctl -n 100：查看最近100条的日志

journalctl --since today：查看今天的日志，也可以是昨天的（yesterday）



Linux命令基础到现在其实就告一段落了，接下来如果还有需要的命令，服务，那后面再说吧
接下来就是shell了，vscode remote连上虚拟机开始先写一个日志处理脚本吧，v1我会放在这个文件夹里，也会顺便用git上传到GitHub的另一个git的仓库里

