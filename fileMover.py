import os

def get_files(file_ext):
    return filter(lambda f: f.find("." + file_ext) != -1, os.listdir("."))

def move_file(filename):
    foldername = filename.split(".")[0]

    newPath = os.path.join(os.getcwd(), foldername, filename)
    oldPath = os.path.join(os.getcwd(), filename)

    if os.path.exists(newPath):
        raise Warning("Path already exists: " + newPath)
    else:
        os.makedirs(foldername)
        os.rename(oldPath, newPath)

def move_files_with_extension(folder_name, file_ext):
    os.chdir(folder_name)
    for filename in get_files(file_ext):
        try:
            move_file(filename)
        except Warning as warning:
            print "Could not move file: " + warning.message
