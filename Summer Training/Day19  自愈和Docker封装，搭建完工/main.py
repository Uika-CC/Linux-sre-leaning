from monitor import(

​    cpu_check,

​    memory_check,

​    disk_check

)

from alarm import send_alarm

from restart import restart_service

def main():

​    checks = [

​        cpu_check(),

​        memory_check(),

​        disk_check()

​    ]

​    for result in checks:

​        if result["status"]:

​            send_alarm(result)

​            if result["name"] == "cpu":

​                restart_service("nginx")

​        else:

​            print(

​                f"{result['name']}正常:"

​                f"{result['value']}%"

​            )

​        

if __name__ == "__main__":

​    main()