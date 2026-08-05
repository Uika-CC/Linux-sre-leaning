今天是2026年8月5日，前几天没打卡原因其实很简单，身体开始还债了，一下子整个人要没了一样，停了三天左右吧，今天好多了

今天刚复工的话也不要整太难的吧，之前监控工具的部署给我干破防了都，对于现在的我来说太难了，没有什么营养，干脆用python模块跑一个像模像样的先用着吧，等之后会的多了在用主流的工具吧

今天的内容很简单，python跑一个监控，部署一下docker，检查一下自己的框架有没有遗漏，然后用docker封装，明天开始压力测试了，还是一样，代码我会放文件夹里

哦对了有关基础不扎实这个事情我可以多提一嘴，作为过来人我还是很有感触的，作为一名学生，我们都是为了补基础而补基础，而对于所有技术领域来说其实并不是这样的，项目驱动才是最好的选择



先来补充一下monitor里面有关psutil的知识点

psutil.cpu_percent(interval=1)
interval表示采样时间间隔，这里=1代表返回1秒内的cpu使用率，返回值采用float形式，比如如果是25.6就会放回25.6%

psutil.virtual_memory()
返回一个命名元组，包含内存的详细信息，以下是可选参数
total：总内存(字节)，available(可用内存)，used(已用内存)，percent(使用百分比)，free：空闲内存

使用示例：
mem = psutil.virtual_memory()
print(mem.total)      # 总内存，单位字节
print(mem.percent)    # 使用百分比，如 62.5

psutil.disk_usage("/")
返回指定路径的磁盘使用信息，这里填的是"/"所以返回"/"的，也可以填/home
参数和使用示例和上面那个差不多，参数少了一个free我就不赘述了



##	补充几个可能用到的psutil函数

| 函数                       | 作用             |
| -------------------------- | ---------------- |
| `psutil.cpu_count()`       | CPU 核心数       |
| `psutil.cpu_freq()`        | CPU 主频         |
| `psutil.swap_memory()`     | 交换分区使用情况 |
| `psutil.disk_partitions()` | 所有磁盘分区列表 |
| `psutil.net_io_counters()` | 网络流量统计     |
| `psutil.boot_time()`       | 系统启动时间     |
| `psutil.users()`           | 当前登录用户     |



有关python语法的点符号：表示层级关系
比如上面的各种.cpu，.swap，就表示从psutil这个模块里调用某个函数/方法



装docker遇到的坑
我用的snap安装的docker，结果systemctl没办法管理
原因：apt安装的是.service，而snap不是，所以没办法被systemctl接管，而是snap接管，查看方式和systemctl一模一样，只不过是换成了snap
但是还是有区别的，查看服务：snap services

