#!/usr/bin/python3

import cgi
import cgitb
import json
import os
import time

class fileDesc:
    def __init__(self, name, size, date):
        self.name = name
        self.size = size
        self.date = date

    def encode(self):
        return self.__dict__

def analyseFile(baseDir, relPath):
    path = os.path.join(baseDir, relPath)
    size = os.path.getsize(path)
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getmtime(path)))
    return fileDesc(relPath, size, date)

def printHeader():
    print ('Content-type: application/json\n\n')

def printBody(type):
    baseDir = os.path.join(os.getcwd(),"files/", type)
    list = []
    for root, dirs, files in os.walk(baseDir):
        for file in files:
            desc = analyseFile(baseDir, os.path.relpath(os.path.join(root,file), baseDir))
            list.append(desc)
    print(json.dumps(list, default=lambda o: o.encode(), indent=4))

def main():
    type = "game"
    try:
        args = cgi.parse()
        type = args['type'][0]
    except:
        pass
    printHeader()
    printBody(type)

if __name__ == '__main__':
    main()