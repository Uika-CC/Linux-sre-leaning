今天买了一本python自动化运维的书，原本还想再买一本Linux的后来想想算了先把买的那本吃透再说，主要还是那本python真的太便宜了，才5.7，一顿早餐钱就能学到一堆东西
今天打算学一下git：

git的作用其实很简单，就是可以让你随时回溯到你改了无数次的脚本的任意一个版本

git有三个区域，分别是工作区，暂存区，git仓库

整个流程：写文件→git add→暂存区→git commit→git仓库

git关联你的GitHub要拿到ssh密钥，在命令行里输入ssh -keygen -t ed25519 -C "你的GitHub邮箱"，随后我自己是三次回车，结束后就会在.ssh的目录里生成一个pub文件，里面就是密钥
补充一点，pub文件是公钥，同名但是没有pub结尾的是私钥

关联成功后还可以用ssh -T git@github.com检查一下

git相关的命令：

git init：将当前的目录初始化为git仓库  建议单独创建一个空的目录来初始化，也方便管理

git status：检查当前git的状态

git add . ：将当前目录下的所有文件上传到暂存区

git commit -m “第一次提交” ：保存第一个版本

git remote add origin  ：这个要配合仓库里的code使用，我用的是ssh的，后面就跟上ssh的code
这里补充一点，我之前搞混了，origin只是一个名字

git remote -v ：查看关联

git branch -M main ：将当前分支改名为main

git branch ：查看当前的分支名称

git push -u origin main 

先理清一个点，commit只是保存了一个版本，push才是上传到了GitHub，这个main完全属于git，是git的一个分支，-u的作用就是建立关联