import sys
import pathlib
import os
import shutil
import time
print("Übung1")
print(os.getcwd())
print()
print("Übung2")
# Prints current Python version
print("Current version of Python is ", sys.version)
print()
print("Übung3")
os.chdir("/home/user20/data/eigenespackage")
print(os.getcwd())
os.chdir("/home/user20/data")
print(os.getcwd())
print()
print("Übung4")
p = pathlib.Path("/home/user20/data/uebung82.py")
print(p)
print(os.path.join("home", "user20", "data"))
print()
print("Übung5")
# checks if path is a file
isFile = os.path.isfile("/home/user20/data")
print(isFile)
# checks if path is a directory
isDirectory = os.path.isdir("/home/user20/data")
print(isDirectory)
print()
print("Übung6")
original = r'/home/user20/data/text.txt'
target = r'/home/user20/data/eigenespackage/text.txt'
shutil.copyfile(original, target)
print("Hat funktioniert! \n")
print("Übung7")
os.chdir("/home/user20/data")
currenttime = time.time()
for f in os.listdir("/home/user20/data/"):
    access_time = os.path.getatime(f)
    since_access = currenttime - access_time
    if since_access <= 60*60*24:
        print(f)