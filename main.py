import os
import shutil

def main():
    files = listFiles("files/")
    groups = groupBy(files, getPrefix)

    for prefix, files in groups.items():
        targetDirectory = makeDirectory(prefix)
        moveFiles(files, targetDirectory)

def listFiles(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory)]

def makeDirectory(name):
    directory = "files/" + name
    os.makedirs(directory)
    return directory

def moveFiles(files, targetDirectory):
    for file in files:
        shutil.move(file, targetDirectory)

def getPrefix(filename):
    return filename.split('-', 1)[0]

def groupBy(items, getKey):
    result = {}
    for item in items:
        key = getKey(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result

main()
