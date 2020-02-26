#coding=UTF-8
import os
import sys
# print sys.getdefaultencoding()

def FindSameFiles(dir):
	file_list = []
	same_path_list = {}
	pwd = os.getcwd()
	for root, dirs, files in os.walk(dir):
		os.chdir(root)
		for each_file in files:
			# 检查字典里面是否含有目前文件集合
			current = same_path_list.get(each_file)
			temp = {}
			if current:
				current.append("" + root + "/" + each_file)
				temp.clear()
				temp[each_file] = current
				same_path_list.update(temp)
			else:
				current = []
				current.append("" + root + "/" + each_file)
				temp.clear()
				temp[each_file] = current
				same_path_list.update(temp)

			# 检查是否重复
			if each_file in file_list:
				print("%s in %s checked more than once!"%(each_file, root))

			if len(same_path_list[each_file]) > 1:
				print(same_path_list[each_file])
			file_list.append(each_file)
		os.chdir(pwd)

dir = "F:/test/"
FindSameFiles(dir)