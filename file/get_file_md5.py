# coding=UTF-8

import hashlib
import os
import datetime

def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename,'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()

def GetAllFile(dir):
	pwd = os.getcwd()
	for root, dirs, files in os.walk(dir):
		os.chdir(root)
		for each_file in files:
			print "File:" + root + "/" + each_file + "\nMD5:" + GetFileMd5(each_file)
		os.chdir(pwd)

dir = "F:/test/"

# 输出文件的md5值以及记录运行时间
starttime = datetime.datetime.now()
GetAllFile(dir)
endtime = datetime.datetime.now()

# print(endtime,starttime)
print(u"运行时间 %ds%dms"%((endtime-starttime).seconds,(endtime-starttime).microseconds / 1000))