#encoding=UTF-8
import json
import sys
import os

# 获取文件内容
def get_file_data(filename):
    with open(filename, 'r') as f:
        return f.read()

# 将压缩后的js格式化
def format_js(path, filename):
	#忽略非js文件
    if not filename.lower().endswith('.js'):
		return
	#忽略已压缩的js文件
    if filename.lower().startswith('formated_'):
		return

	# 获取内容
    print(path + "/" + filename)
    data = get_file_data(path + "/" + filename)

    lines = data.split(";")
    #一般压缩后的文件所有代码都在一行里
    #视情况设定索引，我的情况时第0行是源代码。
    indent = 0
    formatted = []
    for line in lines:
      newline = []
      for char in line:
        newline.append(char)
        if char=='{': #{ 是缩进的依据
          indent+=1
          newline.append("\n")
          newline.append("\t"*indent)
        if char=="}":
          indent-=1
          newline.append("\n")
          newline.append("\t"*indent)
      formatted.append("\t"*indent+"".join(newline))

      with open(path + '/formated_%s'%(filename), 'w') as f:
        f.writelines(";\n".join(formatted))

# 处理所有
# recursive 为 True，遍历 root 目录
# recursive 为 False，只处理 root 的一级目录
def format_js_all(root, recursive=False):
    if recursive:
        for parent, dirnames, filenames in os.walk(root):
            for filename in filenames:
                format_js(parent, filename)               
    else:
        for filename in os.listdir(root):
            format_js(root, filename)

if __name__ == '__main__':
	# 获取当前执行文件的工作目录
    filename = sys.argv[0]
    dirname = os.path.dirname(filename)
    abspath = os.path.abspath(dirname)

    # format_js(r'%s/format_json_files'%(abspath))
    format_js_all(r'%s/format_js_files'%(abspath))