今天本来要学日志的，但是后面发现其实日志可以穿插在每天的日常里，所以今天不学日志了，今天来学学文本处理

找deepseek生成了一大段日志

今天复习的几个命令：

cat	这个只适合查看一些小文件，日志还是不要指望了

less	很好用的一个文本查阅命令，↑↓翻页，/关键字  可以检索，G跳到末尾，g跳到开头，q退出

grep	 关键字  file  在指定文件过滤关键字，可以用管道符加上wc -l统计总数

补充一点，grep -i  可以忽略大小写

head  -n  num  file  查看num行的文件开头

tail -n num file  查看num行的文件末尾

tail -f  file  事实追踪文件

awk '(print $n)'  用来提取第n列的结果

sort  排序，-n 把数字从小到大排序  -r  倒序

uniq：去重

注意一点，如果是ABA这样的，uniq通常不会去除第二个A，所以要先用sort排序一下在用管道符接uniq，这样才会去掉，也就是 sort | uniq

重点，uniq -c 统计次数，很好用



一串很好用的统计命令：

grep 403 app.log | awk '{print $5}' | sort | uniq -c

解释：在app.log把含有403的日志过滤出来，随后根据日志格式，第五列是ip，把ip提取出来，随后sort去重，最后uniq -c输出

上面那串命令需要注意的点：要先用less查看一下日志格式，不要一味的 $5