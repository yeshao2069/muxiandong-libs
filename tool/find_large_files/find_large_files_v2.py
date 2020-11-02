#encoding=UTF-8
import os
import sys

# 限制需要查找的文件大小
# 例如 200MB = 200 * 1024 * 1024
Bigjudge = 200 * 1024 * 1024
# 搜索路径(如F盘)
dir_path = "F:"

def get_big_file(path, filesize, file_path):
    """
    找出path目录下文件大小大于filesize的文件
    :param path:
    :param filesize:
    :return:
    """
    f1 = open(file_path + '/find_large_file_v2_log.txt','w')
    index = 1
    
    # 遍历指定文件夹及其子文件夹
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            target_file = os.path.join(dirpath, filename)
            # 要判断是否真的是文件,有可能是个链接哦
            if not os.path.isfile(target_file):
                continue
            size = os.path.getsize(target_file)
            
            if size > filesize:
                size = size//(1024*1024)    # 转换兆
                size = '{size}M'.format(size=size)
                f1.write("[%s] "%(index) + target_file + "\t" + size + "\n")
                index = index + 1
                print("Rount:" + target_file + "\tSize:" + size)

if __name__ == '__main__':
    # 获取当前执行文件的工作目录
    filename = sys.argv[0]
    dirname = os.path.dirname(filename)
    abspath = os.path.abspath(dirname)

    size = Bigjudge //(1024*1024)
    print("Setting find file max size: {size}M".format(size = size))
    get_big_file(dir_path, Bigjudge, abspath)