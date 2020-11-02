#coding=utf-8
import json
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 需要检查的文件资源路径(绝对路径)
mateRootPath = "E:/GamesHub/assets/Texture/game"
# 需要检查的文件meta类型
matefileTypes = [".plist.meta"]
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
	f2 = open('./all_check_files.txt','w')
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
	print("All check files count: " + str(index))
	return noUseInfo

# 找到指定目录下 指定的meta类型文件
def findPlistMetaInfo(root = mateRootPath, fileTypes = matefileTypes):
	files = getFilesByType(root, fileTypes)
	f4 = open('./collect_meta_list.txt','w')
	plistMetaFiles = []
	index = 1
	for filePath in files:
		if os.path.isfile(filePath):
			f4.write("[%s] "%(index) + filePath + "\n")
			index = index + 1
			plistMetaFiles.append(filePath)
	return plistMetaFiles

def dumpToFile(data):
	f1 = open('./all_image_info.txt','w')
	index = 1
	for info in data:
		f1.write("[%s] "%(index) + ('{:<30}'.format(info)) + ":\t" + data[info] + "\n")
		index = index + 1

# dict1合并dict2
def Merge(dict1, dict2): 
    return(dict1.update(dict2))

if __name__ == '__main__':
	# 切换到当前执行文件的工作目录下
	filename = sys.argv[0]
	dirname = os.path.dirname(filename)
	abspath = os.path.abspath(dirname)
	os.chdir(abspath)
	print(os.getcwd())

	# 找到所有需要排查的meta
	plistMetaInfo = findPlistMetaInfo()
	print("All find plist.meta count: " + str(len(plistMetaInfo)))

	# 找到左右的图片集合
	allImgInfo = {}
	for paths in plistMetaInfo:
		imgInfo = getImgInfo(paths)
		Merge(allImgInfo, imgInfo)
	dumpToFile(allImgInfo)
	imgInfo = allImgInfo.copy()
	print("All image count: " + str(len(imgInfo)))

	noUseInfo = findNotExitImageInfo(imgInfo)
	key_value = sorted(noUseInfo)
	f3 = open('./unuse_image_list.txt','w')
	index = 1
	for key in key_value:
		f3.write("[%s] "%(index) + ('{:<30}'.format(key)) + ":\t" + noUseInfo[key] + "\n")
		index = index + 1

	print("Not used image count: " + str(len(noUseInfo)))