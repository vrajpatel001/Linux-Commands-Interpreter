from PIL import Image
# import os

# make static pdf name dynamic in future "./img2pdf_DBH.pdf"

def img2pdf(images):
    image_data = []
    try:
        for image in images:
            imd = Image.open(image,'r')
            image_data.append(imd.convert('RGB'))
        image_data[0].save(r'./img2pdf_DBH.pdf',save_all=True,append_images=image_data[1:])
    except:
        print("Some error has occured.")
        print("Terminating the execution.")

# wpdf -i path1 path2 ...
# wpdf -if filename

def wpdf(cmd):
    if (cmd[1]=="-i"):
        images = []
        for path_index in range(len(cmd)-2):
            images.append(cmd[path_index+2])
        img2pdf(images)
    elif (cmd[1]=="-if"):
        try:
            with open(cmd[2],'r') as f:
                images = f.read().split()
            print(images)
            img2pdf(images)
        except:
            print("Error:",cmd[2])