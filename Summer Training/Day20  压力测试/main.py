from monitor.monitor import(

​    cpu_check,

​    memory_check,

​    disk_check

)

from alarm.alarm import send_alarm

from recovery.restart import restart_service

import time

def main():

​    while True:

​        print('')

​        print('=' * 40)

​        print('')

​        print(f"开始巡检... {time.strftime('%Y-%m-%d %H:%M:%S')}")

​        print('')

​        checks = [

​            cpu_check(),

​            memory_check(),

​            disk_check()

​        ]

​        for result in checks:

​            if result["status"]:

​                send_alarm(result)

​            

​            else:

​                print(

​                    f"{result['name']}正常:"

​                    f"{result['value']}%"

​                

​                )

​        print('')

​        print('=' * 40)

​        print('')

​        print('下次巡检将在10秒后...')

​        print('')

​        time.sleep(10)

​        

if __name__ == "__main__":

​    main()