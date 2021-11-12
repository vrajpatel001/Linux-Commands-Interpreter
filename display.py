import getpass
# import shutil
import socket
import os
import datetime
import calendar
# import subprocess

from dbhimport import changedir_listFD
from dbhimport import makedir
from dbhimport import touchlp
from dbhimport import catlp
from dbhimport import evaluateme
from dbhimport import dbhcolors
from dbhimport import df_ps
from dbhimport import local_server
from dbhimport import downloader
from dbhimport import pdf_maker

from binscripts import sha

program_path = os.getcwd()

# https://stackoverflow.com/questions/2330393/how-to-set-the-program-title-in-python
os.system('color')
# for windows only
os.system("title DBHTermEcIbP")

print("Thank you for using DBHTermEcIbP!\n")
dbhcolors.prGreen("DBH Linux Commands Interpreter [Version 0.20]\n")
dbhcolors.prRed("(c)-DBH Author: Vraj Patel. All rights reserved.\n")
dbhcolors.prPurple("Open Source Project written in Python\n\n")

def checkfile(file):
    try:
        rfile = open(file,'r')
        #print("Reading this File:",file,"is done successfully!")
        data = rfile.readlines()
        rfile.close()
        return data
    except FileNotFoundError:
        print("\nThis File is not available:",file)
        print("Terminating the execution!")
        return "vraj"
    except:
        print("\nSome error has occured in reading this file:",file)
        print("Terminating the execution!")
        return "vraj"

def initial():
    dbhcolors.prGreen(getpass.getuser())
    dbhcolors.prYellow("@")
    dbhcolors.prCyan(socket.gethostname())
    print('::'+os.path.basename(os.getcwd())+">",end="")
    # print(getpass.getuser()+"@"+socket.gethostname()+'::'+os.path.basename(os.getcwd())+">",end="")
    return

def dbhterminal(cmd):
    #while(1):
    if(cmd[0]=="ls") :
        changedir_listFD.listFD(cmd)
    elif(cmd[0]=="cd") :
        changedir_listFD.changedir(cmd)            
    elif(cmd[0]=="pwd") :
        print(os.getcwd())
    elif(cmd[0]=="date") :
        print(datetime.datetime.now().strftime("%c"))
    elif(cmd[0]=="cal") :
        print(calendar.month(datetime.datetime.today().year,datetime.datetime.today().month))
    elif(cmd[0]=="whoami") :
        print(getpass.getuser())
    elif(cmd[0]=="mkdir") :
        makedir.makedir(cmd)
    elif(cmd[0]=="touch") :
        touchlp.touchlp(cmd)
    elif(cmd[0]=="cat") :
        catlp.catlp(cmd)
    elif(cmd[0]=="tac") :
        catlp.catlp(cmd)    
    elif(cmd[0]=="hostname") :
        print(socket.gethostname())
    elif(cmd[0]=="eval") :
        evaluateme.evaluateme(cmd)
    elif(cmd[0]=="tree") :
        changedir_listFD.treeFD(cmd)
    elif(cmd[0]=="df") :
        df_ps.vdf()  
    elif(cmd[0]=="ps") :
        df_ps.vps()
    elif(cmd[0]=="sha") :
        sha.sha(cmd)    
    elif(cmd[0]=="httpserve") :
        path=os.getcwd()
        changedir_listFD.changedir(cmd)
        url_path=os.getcwd()
        local_server.simple_http_server(url_path)
        os.chdir(path)
    elif(cmd[0]=="wget") :
        downloader.wget(cmd)
    elif(cmd[0]=="wpdf"):
        pdf_maker.wpdf(cmd)
    elif(cmd[0]=="ytd"):
        downloader.ytd(cmd)
    else :
        try :
            os.system(" ".join(cmd))
        except :
            print("Command or Application non recognisable!")                         
    return

def main():
    while(1):
        initial()
        cmd=input().split(" ")
        if cmd[0]=="dbh":
            data = checkfile(cmd[1])
            if data!="vraj":
                for i in range(len(data)):
                    initial()
                    print(data[i],end="")
                    dbhterminal(str(data[i]).split())
            print()
        elif(cmd[0]=="exit") :
            break
        elif(cmd[0]=="clear") :
            os.system("cls")
        else:
            dbhterminal(cmd)   

if __name__ == "__main__":
    main()