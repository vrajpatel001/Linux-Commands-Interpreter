# Stegnography
# Hide data using append
# works for jpeg

# import sys
import PIL.Image as imtype
import io

# n = len(cmd)
# img = imtype.open(str(cmd[2]))

# if (img.formats=='JPEG') :

def sha(cmd) :
    if (cmd[1]=="-wt") :
        try:
            with open(cmd[2],'ab') as f:
                with open(cmd[3],'r') as a:
                    secret=a.read()
                msg = bytes(secret, 'utf-8')
                f.write(msg)
        except:
            print("Some error has occured!")
            print("Terminating Execution!!")

    elif (cmd[1]=="-rt") :
        try :
            with open(cmd[2],'rb') as f:
                content = f.read()
                offset = content.index(bytes.fromhex("FFD9"))
                f.seek(offset + 2)
                print(f.read())
        except:
            print("Some error has occured!")
            print("Terminating Execution!!")

    elif (cmd[1]=="-wi") :
        try :
            img = imtype.open(cmd[3])
            bytesarr = io.BytesIO()
            img.save(bytesarr, format=img.format)
            with open(cmd[2],'ab') as f:
                f.write(bytesarr.getvalue())
        except :
            print("Some error has occured!")
            print("Terminating Execution!!")

    elif (cmd[1]=="-ri") :
        try :
            with open(cmd[2],'rb') as f:
                content = f.read()
                offset = content.index(bytes.fromhex("FFD9"))
                f.seek(offset + 2)
                nimg = imtype.open(io.BytesIO(f.read()))
                nimg.save("./stegextract.jpg")
                print("Created file: stegextract.jpg")
        except:
            print("Some error has occured!")
            print("Terminating Execution!!")
    
    elif(cmd[1]=="-we"):
        try:
            with open(cmd[2],'ab') as f, open(cmd[3],'rb') as e:
                f.write(e.read())
        except:
            print("Some error has occured!")
            print("Terminating Execution!!")
    
    elif(cmd[1]=="-re"):
        try :
            with open(cmd[2],'rb') as f:
                content = f.read()
                offset = content.index(bytes.fromhex("FFD9"))
                f.seek(offset + 2)
                with open("./stegextract.exe",'wb') as e:
                    e.write(f.read())
                print("Created file: stegextract.exe")
        except:
            print("Some error has occured!")
            print("Terminating Execution!!")

# else :
#     print("Image file format not supported.")