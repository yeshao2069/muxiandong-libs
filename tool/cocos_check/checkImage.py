#coding=utf-8
import json
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 需要检查的文件资源列表(绝对路径)
matePath = "E:/GamesHub/assets/Texture/game/sicbo/room/sicbo_room.plist.meta"
# 需要检查的文件meta类型
# matefileTypes = ".plist.meta"
# 需要检查的文件根路径(绝对路径)
rootPath = "E:/GamesHub/assets"
# 需要检查的文件类型
fileTypes = [".js", ".prefab", ".fire"]

# 获取.meta 文件中img name uuid
def getImgInfo(path):
	file = open(path,'r')
	jsonData = json.load(file)
	subMetas = jsonData["subMetas"]

	imgInfo = {}
	for key in subMetas:
		name = key.replace(".png","")
		imgInfo[name] = subMetas[key]["uuid"]
	return imgInfo

# 获取 指定路径下 指定类型文件列表
def getFilesByType(root, fileTypes):
	putFiles = []
	for dirpath,dirs,files in os.walk(root):
		for fileName in files:
			for fileType in fileTypes:
				if fileName.endswith(fileType):
					putFiles.append(os.path.join(dirpath, fileName))
	return putFiles

# 找出指定目录下 未直接使用图片
def findNotExitImageInfo(imgInfo, fileTypes = fileTypes, root = rootPath):
	files = getFilesByType(root, fileTypes)
	noUseInfo = imgInfo.copy()
	f2 = open('./checkFiles.txt','w')
	index = 1
	for filePath in files:
		if os.path.isfile(filePath):
			f2.write("[%s] "%(index) + filePath + "\n")
			index = index + 1
			file = open(filePath, "r")
			fileStr = file.read()
			for name in imgInfo:
				uuid = imgInfo[name]
				if fileStr.find(str(name)) != -1 or fileStr.find(str(uuid)) != -1:
					if name in noUseInfo:
						del noUseInfo[name]
	return noUseInfo

def dumpToFile(data):
	f1 = open('./imgInfo.txt','w')
	index = 1
	for info in data:
		f1.write("[%s] "%(index) + ('{:<30}'.format(info)) + ":\t" + data[info] + "\n")
		index = index + 1

if __name__ == '__main__':
	# 切换到当前执行文件的工作目录下
	filename = sys.argv[0]
	dirname = os.path.dirname(filename)
	abspath = os.path.abspath(dirname)
	os.chdir(abspath)
	print(os.getcwd())

	imgInfo = getImgInfo(matePath)
	dumpToFile(imgInfo)

	print("All img count: " + str(len(imgInfo)))

	noUseInfo = findNotExitImageInfo(imgInfo)
	key_value = sorted(noUseInfo)
	f3 = open('./log.txt','w')

	for key in key_value:
		f3.write(('{:<30}'.format(key)) + ":\t" + noUseInfo[key] + "\n")

	print("not used img count: " + str(len(noUseInfo)))