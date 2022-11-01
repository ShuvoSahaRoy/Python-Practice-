import psutil
import psutil as ps
from datetime import timedelta
from sys import argv
from time import time

NAME= argv[0]
# print(NAME)
# print(argv)


def system_info():
    info = {
        "CPU in use": f"{ps.cpu_percent(interval=.1)}%",
        "Time on CPU": timedelta(seconds=ps.cpu_times().system+ ps.cpu_times().user),
        "Memory in use": f"{ps.virtual_memory().percent}%",
        "Disk in use": f"{ps.disk_usage('/').percent}%"
    }

    print("\n\n   System Info\n\n" + "\n".join([f"{key}: {value}" for key,value in info.items()]))


def process_info():
    for proc in ps.process_iter(attrs=("name","pid","cmdline","create_time","cpu_percent","cpu_times", "memory_percent")):
        if "python" in proc.info["name"] and (cl := proc.info["cmdline"]) is not None and len(cl) > 0 and NAME in cl[-1]:
            info = {
                "PID": proc.info["pid"],
                "Uptime": timedelta(seconds=time() - proc.info["create_time"]),
                "CPU in use": f"{proc.info['cpu_percent']}%",
                "Time on CPU": timedelta(seconds=proc.info["cpu_times"].system + proc.info["cpu_times"].user),
                "Memory in Use": f"{(mem := proc.info['memory_percent']):.3f}%",
                "Memory Usage":  f"{ps.virtual_memory().total*(mem/100)/(1027**3):,.3f} GiB",
            }
            print("\n\n" + "\n".join([f"{key}:{value}" for key, value in info.items()]))

system_info()
process_info()