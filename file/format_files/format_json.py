#encoding=UTF-8
import json
import sys
import os

# 获取文件内容
def get_file_data(filename):
    with open(filename, 'r') as f:
        return f.read()

# 将压缩后的json格式化
def format_json(path, filename):
	#忽略非json文件
    if not filename.lower().endswith('.json'):
		return
	#忽略已压缩的json文件
    if filename.lower().startswith('formated_'):
		return

	# 获取内容
    print(path + "/" + filename)
    data = get_file_data(path + "/" + filename)
	# 获取json字符串
    str = json.loads(data)
	# 格式化
    Objects = json.dumps(str, indent=4)
    with open(path + '/formated_%s'%(filename), 'wt') as f:
    	f.write(Objects)

# 处理所有
# recursive 为 True，遍历 root 目录
# recursive 为 False，只处理 root 的一级目录
def format_json_all(root, recursive=False):
    if recursive:
        for parent, dirnames, filenames in os.walk(root):
            for filename in filenames:
                format_json(parent, filename)               
    else:
        for filename in os.listdir(root):
            format_json(root, filename)

if __name__ == '__main__':
	# 获取当前执行文件的工作目录
    filename = sys.argv[0]
    dirname = os.path.dirname(filename)
    abspath = os.path.abspath(dirname)

    # format_json(r'%s/format_json_files'%(abspath))
    format_json_all(r'%s/format_json_files'%(abspath))

# 在线解析
# https://www.sojson.com/