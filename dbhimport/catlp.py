import os

def catlp(cmd) :
    if (cmd[1][0]=="-") :
        if (cmd[1][1:3]=="ns" or cmd[1][1:3]=="sn") :
            catprint(cmd,1,1,-1)
        elif (cmd[1][1]=="n") :
            catprint(cmd,1)
        elif (cmd[1][1]=="s") :
            catprint(cmd,0,1)
        elif (cmd[1][1]=="b") :
            catprint(cmd,1,0,0,0)
    elif (cmd[1]=="*") :
        vfiles = os.listdir(os.getcwd())
        mycmd = ["cat"]
        if cmd[0]=="tac":
            mycmd[0] = "tac"
        for f in vfiles:
            if os.path.isfile(f):
                mycmd.append(f)
        if (len(cmd)>2) :
            if (cmd[2][0]=="-") :
                #mycmd.append("-")
                if (cmd[2][1:3]=="ns" or cmd[2][1:3]=="sn") :
                    catprint(mycmd,1,1,-1,-1,-1)
                elif (cmd[2][1]=="n") :
                    catprint(mycmd,1,0,0,-1,-1)
                elif (cmd[2][1]=="s") :
                    catprint(mycmd,0,1,0,-1,-1)
                elif (cmd[2][1]=="b") :
                    catprint(mycmd,1,0,0,0,-1)
        else :
            catprint(mycmd)            
    else :
        catprint(cmd)
    
def catprint(cmd,n=0,s=0,ns=0,b=-1,wild=0):
    n_linecount=1
    s_linecount=0
    try:
        text = ""
        for i in range(1+n+s+ns+wild,len(cmd)):
            if (str(cmd[i])!=">"):
                f = open(cmd[i], "r")
                if n==0 and s==0 and ns==0:
                    if (str(cmd[0])=="cat") :
                        text += f.read()
                    elif (str(cmd[0])=="tac") :
                        temp = f.readlines()
                        temp.reverse()
                        for m in range(len(temp)) :
                            text += str(temp[m]) 
                elif n==1 or s==1 or b==0:
                    temp = f.readlines()
                    if (str(cmd[0])=="tac") :
                        ##print("lol")
                        temp.reverse()
                    for j in range(len(temp)):
                        if (s==1 and temp[j]=="\n" and temp[j+1]=="\n") :
                            s_linecount += 1    
                        elif (b==0 and temp[j]=="\n") :
                            s_linecount += 1
                            text += str(temp[j])
                        else :
                            text += "\t"+str(n_linecount+j-s_linecount)+" "+str(temp[j])
                    n_linecount+=j
                f.close()
    except FileNotFoundError :
        text = cmd[0]+": "+cmd[1]+": No such file or directory"   
    except PermissionError :
        text = cmd[0]+": "+cmd[1]+": Permission denied"
        if os.path.isdir(cmd[1]) :
            text = cmd[0]+": "+cmd[1]+": Is a directory"
    print(text)