#encoding=UTF-8
import os
import sys
import json

# 获取文件内容
def get_file_data(filename):
    with open(filename, 'r') as f:
        return f.read()

# 转换带有转义符
def ProcOneWithEscape(path):
    # 获取内容
	data = get_file_data(path + "/test1.json");
    
	with open(path + '/json_min.json', 'w') as f:
		f.write(json.dumps(data))

# 转换不带转义符
def ProcOne(path, filename):
	#忽略非json文件
    if not filename.lower().endswith('.json'):
		return
	#忽略已压缩的json文件
    if filename.lower().startswith('json_min_'):
		return
    # if filename.lower().endswith('.json_min.json'):
		# return

	# 获取内容
    print(path + "/" + filename)
    data = get_file_data(path + "/" + filename)

    with open(path + '/json_min_%s'%(filename), 'w') as f:
		d = json.dumps(data)
		# 去除所有空格/换行符号/缩进符号
		d = d.replace(' ', '')
		d = d.replace('\\n','')
		d = d.replace('\\','')
		# 去除首尾的""
		d = d.strip('\"')
		f.write(d)

# 处理所有
# recursive 为 True，遍历 root 目录
# recursive 为 False，只处理 root 的一级目录
def ProcAll(root, recursive=False):
    if recursive:
        for parent, dirnames, filenames in os.walk(root):
            for filename in filenames:
                ProcOne(parent, filename)               
    else:
        for filename in os.listdir(root):
            ProcOne(root, filename)
    
if __name__ == '__main__':
    # 获取当前执行文件的工作目录
    filename = sys.argv[0]
    dirname = os.path.dirname(filename)
    abspath = os.path.abspath(dirname)

    # ProcOne(r'%s/test_json_codes'%(abspath))
    ProcAll(r'%s/test_json_codes'%(abspath))