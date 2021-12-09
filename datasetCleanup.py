import os
from natsort import natsorted 

path = 'testset'


def is_image(filename, verbose=False):

    data = open(filename,'rb').read(10)

    # check if file is JPG or JPEG
    if data[:3] == b'\xff\xd8\xff':
        if verbose == True:
             print(filename+" is: JPG/JPEG.")
        return True

    # check if file is PNG
    if data[:8] == b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a':
        if verbose == True:
             print(filename+" is: PNG.")
        return True

    # check if file is GIF
    if data[:6] in [b'\x47\x49\x46\x38\x37\x61', b'\x47\x49\x46\x38\x39\x61']:
        if verbose == True:
             print(filename+" is: GIF.")
        return True

    return False

def get_file_parts(path):
    fname = os.path.splitext(path)[0]
    file_parts = os.path.splitext( fname )
    number = file_parts[1].replace('.','')
    name = file_parts[0]
    try:
        number_int = int(number)
    except ValueError:
        print("Invalid int at: " + path)
    return name, int(number)

image_paths = []
for subdir, dirs, files in os.walk(path):
    for filename in files:
        filepath = subdir + os.sep + filename
        if is_image(filepath):
            image_paths.append(filepath)
        elif os.path.isfile(os.path.abspath(filepath)):
            os.remove(filepath)
            print("removed: " + filepath)




image_paths = natsorted(image_paths)
last_name = ""
for img in image_paths:
    curr_name, curr_num = get_file_parts(img)
    if last_name != curr_name:
        last_name = curr_name
        last_num = -1
    if last_num + 1 != curr_num:
        new_name = img.replace(str(curr_num),str(last_num + 1))
        os.rename(img, new_name.lower())
        print("found: " + img)
    else:
        os.rename(img, img.lower())
    last_num += 1

def cutTo7(path):
    image_paths = []
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            filepath = subdir + os.sep + filename
            if is_image(filepath):
                image_paths.append(filepath)

    image_paths = natsorted(image_paths)
    last_name = ""
    for img in image_paths:
        curr_name, curr_num = get_file_parts(img)
        if last_name != curr_name:
            last_name = curr_name
        if curr_num > 6:
            os.remove(img)
#cutTo7(path)