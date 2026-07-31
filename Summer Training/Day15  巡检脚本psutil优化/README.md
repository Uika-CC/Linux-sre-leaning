今天是7月31日，昨天知道了不少东西，纵观我自己现阶段的状态来看，目前我比较推崇自己搞一个个人轻量的，用sre思想运维的Ubuntu
其中，现在拟定了
一阶段：日志，告警，拨测，Iac
二阶段：自愈，自动化运维
三阶段：docker

暂时先这样，话说到底谁在说docker过时了，这东西必定成为Linux的底子之一

目前IaC暂时用shell来代替，而且个人的开发环境Iac也不太体现得出效果，等到了docker那个阶段再来用python写Iac

开始今天的内容吧，感觉今天的风格有点正式了，写完的脚本我一样会放在这个文件夹里

写巡检脚本的时候遇到的一个坑：输出的时候在输出的结果后面一定要加.stdout，subprocess返回的结果包括
正确输出（stdout），错误输出（errout），返回码（returncode）

subprocess.run使用命令的时候，如果要用到管道符，要加一个shell=True

我服了，搞了半天psutil都有现成的，转成psutil吧

psutil知识点也太多了吧