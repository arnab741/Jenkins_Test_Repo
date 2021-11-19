import os
import copy
import sys

spath = r"C:\Users\Arnab\Desktop\JAVASCRIPT"
for roots, dirs, files in os.walk(spath, topdown = True):
    origLen = len(dirs)
    dirs[:] = [dirr for dirr in dirs if len(os.path.join(roots,dirr)) < 50]
    if origLen != len(dirs):
        print('HeHe\n')
    print(roots, dirs, files)
    print('**************')
    '''
    if roots[len(spath):].count(os.sep) >= 2:
        dirs.clear()
    for file in files:
        print(os.path.join(roots,file))
        '''
print(os.environ['KIERMANFS'])
print(sys.argv)
