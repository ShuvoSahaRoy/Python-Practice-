import shutil
import sys

def check_disk_usage(disk,min_absolute,min_percent):
    du = shutil.disk_usage(disk)
    print(du)
    percent_free = 100* du.free/du.total

    gigabytes_free = du.free/ 2**30
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True


if not check_disk_usage("/",2,10):
    print('Error: Not Enough disk space')
    sys.exit(1)

print("Everything ok")
sys.exit(0)