import os
def getFiles(filepath, extention):
    a = list(filter(lambda x: extention in x, os.listdir(filepath)))
    return a

if __name__ == '__main__':
    filepath = './'
    extention = '.csv'
    files = getFiles(filepath, extention)
    print(files)