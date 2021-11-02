import os
from dbhimport import dbhcolors

prev_path=""

def change_dir(path):
    try :
        #if cmd[0]=="cd":
        global prev_path 
        prev_path = os.getcwd()
        os.chdir(path)
        #elif cmd[0]=="ls" :
        #return path
    except FileNotFoundError :
        print(path+": "+"No such file or directory")

def changedir(cmd) :
    # cd=input("Write the full path to change working directory: ")
    if len(cmd)==1 or cmd[1]=="~" or cmd[1]=="--":
        #vpath = change_dir(cmd,os.path.expanduser('~'))
        change_dir(os.path.expanduser('~'))
    elif cmd[1]=="" :
        pass
    elif cmd[1]=="-" :
        os.chdir(prev_path)      
    elif (cmd[1][0]=="\"" and cmd[len(cmd)-1][-1]=="\"") or (cmd[1][0]=="'" and cmd[len(cmd)-1][-1]=="'") :
        if len(cmd)!=2 :
            path_cmd=cmd[1][1:]
            for i in range (2,len(cmd)-1):
                path_cmd+=" "+cmd[i]
            path_cmd+=" "+cmd[len(cmd)-1][:-1]
        else :
            path_cmd=cmd[1][1:-1]        
        #vpath = change_dir(cmd,path_cmd)
        change_dir(path_cmd)
    elif cmd[1]=="." :
        #vpath = change_dir(cmd,os.pardir)
        change_dir(os.getcwd())
    elif cmd[1]==".." :
        #vpath = change_dir(cmd,os.pardir)
        cmd_path=str(os.getcwd())
        cmd_path+="\\..\\"
        change_dir(cmd_path)
    elif len(cmd)==2 :    
        cmd_path=str(os.getcwd())
        cmd_path+="\\"+cmd[1]
        #os.path.join(cmd_path,str(cmd[1]))
        #vpath = change_dir(cmd,cmd_path)
        change_dir(cmd_path)
    elif cmd[1][-1]=="\\" :
        #vpath = change_dir(cmd,cmd[1][:-1]+" "+cmd[2])
        change_dir(cmd[1][:-1]+" "+cmd[2])
    #return vpath

def justls (path, columns, hidden, reverse=0) :
    charsize=0
    #print(os.listdir(path))
    order = os.listdir(path)
    if reverse==0 :
        pass
    else :
        order.reverse()     
    for f in order:
        if os.path.isdir(f) :
            if hidden :
                if f.startswith('.') :
                    continue
            if len(f) < columns - charsize - 5 :    
                dbhcolors.prLightPurple("\""+f+"\""+"   ")
                charsize+=len(f)+5
            else :
                print("")
                dbhcolors.prLightPurple("\""+f+"\""+"   ")
                charsize=len(f)+5    
        elif os.path.isfile(f) :
            if hidden :
                if f.startswith('.') :
                    continue
            if len(f) < columns - charsize - 3 :
                dbhcolors.prLightGray(f+"   ")
                charsize+=len(f)+3
            else :
                print("")
                dbhcolors.prLightGray(f+"   ")
                charsize=len(f)+5         
    print("")

def wildcardls (path, columns, hidden, extension) :
    charsize=0
    for f in os.listdir(path):   
        if os.path.isfile(f) :
            if f.endswith(extension):
                if hidden :
                    if f.startswith('.') :
                        continue
                if len(f) < columns - charsize - 3 :
                    dbhcolors.prLightGray(f+"   ")
                    charsize+=len(f)+3
                else :
                    print("")
                    dbhcolors.prLightGray(f+"   ")
                    charsize=len(f)+5
    print("")

def listFD (cmd) :
    columns = os.get_terminal_size().columns
    path=os.getcwd()
    #print(path)
    #f=os.listdir(path)
    #charsize = sum(len(i) for i in f)
    if len(cmd)==1 :
        justls(path, columns, 1)
    elif cmd[1][0]=="-" :
        if cmd[1][1]=="l" :
            pass
        elif cmd[1][1]=="a" :
            justls(path, columns, 0)
        elif cmd[1][1]=="r" :
            justls(path, columns, 0, 1)    
    elif cmd[1]=="*" :
        pass
    elif cmd[1][0]=="*" :
        wildcardls(path, columns, 0, cmd[1][1:])
    else :
        #vpath = changedir(cmd)
        #os.chdir(path)
        changedir(cmd)
        #print(vpath)
        justls(os.getcwd(), columns, 1)
        os.chdir(path)

# old tree implementation

# def treeFD (cmd):
#     path=os.getcwd()
#     changedir(cmd)
#     startpath = os.getcwd()
#     os.chdir(path)
#     i=1
#     for root, dirs, files in os.walk(startpath):
#         level = root.replace(startpath, '').count(os.sep)
#         indent = '─' * 2 * (level)
#         if i==1:
#             print('{}{}/'.format(indent, os.path.basename(root)))
#             i=i+1        
#         else:
#             print(' ├{}'.format(indent),'{}/'.format(os.path.basename(root)))
#         subindent = ' ' * 2 * (level + 1)
#         for f in files:
#             print(' │{}'.format(subindent),"└──",'{}'.format(f))

import pathlib

from rich import print as rprint
from rich.filesize import decimal
from rich.markup import escape
from rich.text import Text
from rich.tree import Tree

def walk_directory(directory: pathlib.Path, tree: Tree) -> None:
    """Recursively build a Tree with directory contents."""
    # Sort dirs first then by filename
    paths = sorted(
        pathlib.Path(directory).iterdir(),
        key=lambda path: (path.is_file(), path.name.lower()),
    )
    for path in paths:
        # Remove hidden files
        if path.name.startswith("."):
            continue
        if path.is_dir():
            branch = tree.add(
                f"[bold magenta]:open_file_folder: [link file://{path}]{escape(path.name)}",
            )
            walk_directory(path, branch)
        else:
            text_filename = Text(path.name, "green")
            file_size = path.stat().st_size
            text_filename.append(f" ({decimal(file_size)})", "blue")
            tree.add(text_filename)

def treeFD (cmd):
    try:
        directory = os.path.abspath(cmd[1])
    except:
        print("Incorrect path")
    else:
        tree = Tree(
            f":open_file_folder: [link file://{directory}]{directory}",
        )
        walk_directory(pathlib.Path(directory), tree)
        rprint(tree)