import psutil
import shutil
# import subprocess
# import os
import time
import wmi
# for windows only
import win32api

def vdf():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    tsize=0
    tuse=0
    tava=0

    print ("{:<13} {:<8} {:<7} {:<12} {:<7}".format('File System','Size','Used','Available','Use%'))
    for f in drives:
        total, used, free = shutil.disk_usage(f)
        tsize += total
        tuse += used
        tava += free
        puse = int(used/total*100)
        print ("{:<13} {:<8} {:<7} {:<12} {:<7}".format(f,str(total//(2**30))+"G",str(used//(2**30))+"G",str(free//(2**30))+"G",str(puse)+"%"))

    tpuse = int(tuse/tsize*100)
    print ("{:<13} {:<8} {:<7} {:<12} {:<7}".format("Total",str(tsize//(2**30))+"G",str(tuse//(2**30))+"G",str(tava//(2**30))+"G",str(tpuse)+"%"))

# def old_ps():
#     Data = subprocess.check_output(['wmic', 'process', 'list', 'brief'])
#     a = str(Data)
#     try:
#         for i in range(len(a)):
#             print(a.split("\\r\\r\\n")[i])
#     except IndexError as e:
#         print("All Done")

def vps():
    # {:<8} {:<10} {:<12} ,'PPID','PGID','UID'
    # {:<8} {:<10} {:<12} ,os.getppid(vpid),os.getpgrp(vpid),os.getuid(vpid)
    print ("{:<8} {:<12} {:<20}".format('PID','STIME','NAME'))
    # output = os.popen('wmic process get description, processid').read()
    for process in wmi.WMI().Win32_Process():
        try: 
            vpid = process.ProcessId
            stime = psutil.Process(vpid)
            stime = time.strftime("%H:%M:%S", time.localtime(stime.create_time()))
            name = process.Name
            print ("{:<8} {:<12} {:<20}".format(vpid,stime,name))
        except:
            pass