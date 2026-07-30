今天是7月30日，昨天没睡好难受了一天所以给自己放了一天

先把nginx的基础复习一遍

http：管理所有的http服务
server：一个网站/一个服务
location：匹配不同的URL路径
（大致结构我直接截图吧）

重点讲讲location
location是nginx的核心，nginx的本质就是收到请求后，根据URL匹配规则来返回内容

location规则

location / {}  ：普通匹配，所有请求默认走这里
location = /login {} ：精确匹配/login，不包含/login/
location /api/ {} ：前缀匹配，会包含/api/下的所有目录
location ~ \ .php$ {} ：正则匹配，也就是后缀匹配，注意那个美元符号和反斜杠不要漏了

proxy_pass：连接flask的关键，写在{  }里，后面跟你的ip地址和flask端口
这里也补一点：proxy_pass带不带反斜杠的区别
带/：把完整的URL传给flask
不带/：去掉location匹配的那一段，只传剩下的

nginx目录解释：
nginx.conf：主配置文件
conf.d：额外配置
sites-available：可用站点配置
sites-enabled：已启用站点
snippets：配置片段

目前的话只需要知道三个
nginx.conf用来改配置的，现阶段不需要改，但是要知道 nginx -c 目录，这个是改nginx配置的
sites-available：用来存放你需要用的目录的，并不会真正启用
sites-enabled：真正启用nginx的目录

其他需要知道的目录
/var/www/ ：网站文件
/var/log/nginx/ ：nginx日志

nginx常用的几条命令
nginx -s reload：reload 会在不会关闭当前的请求的情况下重载服务，改完配置一定要重载一次，不然配置不会生效
nginx -t：查看nginx的配置有没有出错的地方

值得一提，502和404都可以用上面的方式去解决，如果没有就看看80端口有没有正在被监听，这也就是排错思路了
再补一条总结：500看日志，502看后端，404看location，proxy_pass



今天在多复习一个理论吧，明天直接实操

python的subprocess模块
作用：用python来启动和控制外部程序的模块，示例代码截图放文件夹了

启动：subprocess.run( )

几个需要认识的参数

capture_output=True：把输出抓回来，也就是return
text=True：把输出的字节转成字符串

命令执行后的三个输出
stdout：正常输出
stderr：错误输出
returncode：返回状态，非0代表失败，0代表成功

subprocess和os.system的区别：os拿不到输出，sub拿得到