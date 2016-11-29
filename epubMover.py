import os


def isEpub(s):
    return s.find(".epub") != -1

def getEpubFiles():
    return filter(isEpub, os.listdir("."))

def moveEpubFile(filename):
    foldername = filename.split(".")[0]

    newPath = os.path.join(os.getcwd(), foldername, filename)
    oldPath = os.path.join(os.getcwd(), filename)

    if os.path.exists(newPath):
        raise Warning("Path already exists: " + newPath)
    else:
        os.makedirs(foldername)
        os.rename(oldPath, newPath)

def moveEpubFiles(foldername):
    os.chdir(foldername)
    for filename in getEpubFiles():
        try:
            moveEpubFile(filename)
        except Warning as warning:
            print "Could not move file: " + warning.message
