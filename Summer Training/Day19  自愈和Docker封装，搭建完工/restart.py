import subprocess

def restart_service(service):

​    #重启服务

​    

​    result = subprocess.run(

​        ["systemctl","restart",service,]

​        shell=True

​    )

​    if result.returncode == 0:

​        print(f"{service} restart success")

​    else:

​        print(f"{sercive} restart failed")

​        print(result.stderr)