import os

path = input('Open with >')
t = '%SystemRoot%\\system32\\OpenWith.exe ' + path
os.system(t)
