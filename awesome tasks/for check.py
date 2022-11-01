# print("hello")

import time
# # at the beginning of the script
startTime = time.time()
# # ...
for i in range(0,10**5):
    print(f"{i}\n")


def getUptime():
    """
    Returns the number of seconds since the program started.
    """
    # do return startTime if you just want the process start time
    return

print(time.time() - startTime)

# import platform
#
# print(platform.processor())

import os,psutil

print(os.getpid())
print(os.getpid())

print(psutil.disk_usage('/').percent)
print(f"Memory :{psutil.virtual_memory().total/(1024**3):.3f} GB")

current_process = psutil.Process();
print(current_process.cpu_percent())
