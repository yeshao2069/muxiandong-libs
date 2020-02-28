#encoding=UTF-8
import json
import sys
import os

# 获取文件内容
def get_file_data(filename):
    with open(filename, 'r') as f:
        return f.read()

# 将压缩后的json格式化
def format_json(path):
	# 获取内容
	data = get_file_data(path + "/test1.json");
	# 获取json字符串
	str = json.loads(data)
	# 格式化
	Objects = json.dumps(str, indent=4)
	with open(path + '/format_json_test1.json', 'wt') as f:
  		f.write(Objects)

if __name__ == '__main__':
	# 获取当前执行文件的工作目录
    filename = sys.argv[0]
    dirname = os.path.dirname(filename)
    abspath = os.path.abspath(dirname)

    # 需要格式化的json文件路径
    format_json(abspath)

# 在线解析
# https://www.sojson.com/