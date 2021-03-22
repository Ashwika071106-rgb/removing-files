import os
import shutil
import time

path = input("Enter the path of directory")

seconds =  time.time()
if(os.path.exists(path)):
    folder_name = os.walk(path)

    os.path.join(path,folder_name)

    ctime = os.stat(path).st_ctime
    return ctime

    if(seconds>ctime):
        print("Greater")
else:
    print("Path not found")