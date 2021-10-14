# elif(cmd[0]=="dha") :
#     ppath = program_path
#     # ppath+="\\bin"
#     ppath+="\\binscipts"
#     cdir = os.getcwd()
#     os.chdir(ppath)
#     # print(ppath)
#     # os.system("start sha.exe "+str(cmd[1:]))
#     os.system("sha.py "+str(cmd[1:]))
#     os.chdir(cdir)

# Stegnography
# Hide data using append
# works for jpeg

import sys
import PIL.Image as imtype
import io

# n = len(sys.argv)
# img = imtype.open(str(sys.argv[2]))

# if (img.formats=='JPEG') :

if (sys.argv[1]=="-wt") :
    try:
        with open(sys.argv[2],'ab') as f:
            with open(sys.argv[3],'r') as a:
                secret=a.read()
            msg = bytes(secret, 'utf-8')
            f.write(msg)
    except:
        print("Some error has occured!")
        print("Terminating Execution!!")

elif (sys.argv[1]=="-rt") :
    try :
        with open(sys.argv[2],'rb') as f:
            content = f.read()
            offset = content.index(bytes.fromhex("FFD9"))
            f.seek(offset + 2)
            print(f.read())
    except:
        print("Some error has occured!")
        print("Terminating Execution!!")

elif (sys.argv[1]=="-wi") :
    try :
        img = imtype.open(sys.argv[3])
        bytesarr = io.BytesIO()
        img.save(bytesarr, format=img.format)
        with open(sys.argv[2],'ab') as f:
            f.write(bytesarr.getvalue())
    except :
        print("Some error has occured!")
        print("Terminating Execution!!")

elif (sys.argv[1]=="-ri") :
    try :
        with open(sys.argv[2],'rb') as f:
            content = f.read()
            offset = content.index(bytes.fromhex("FFD9"))
            f.seek(offset + 2)
            nimg = imtype.open(io.BytesIO(f.read()))
            nimg.save("Noextension.jpg")
    except:
        print("Some error has occured!")
        print("Terminating Execution!!")

# else :
#     print("Image file format not supported.")