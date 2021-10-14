import os

def makedir(cmd) :
    path=os.getcwd()+"\\"+cmd[1]
    try:
        os.mkdir(path)
    except FileExistsError:
        print("mkdir: cannot create directory '"+cmd[1]+"': File exists") 