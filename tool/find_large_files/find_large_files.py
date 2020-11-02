#encoding=UTF-8
import os,sys

# 该脚本用于在用户目录中查找大的用户文件

# 限制需要查找的文件大小
# 例如 200MB = 200 * 1024 * 1024
Bigjudge = 200 * 1024 * 1024
# 搜索路径(如F盘)
dir_path = "F:"

def isLarge(file_path):
    # 判断文件大小是否大于Bigjudge，大于返回文件大小，小于返回false
    filesize = os.path.getsize(file_path)
    if os.path.isfile(file_path) == False:
        raise os.error("没有该文件")
    if(filesize > Bigjudge):
        return filesize
    else:
        return 0
 
def getAlltree(dir_path, log_path):
    # 查找该目录下所有文件大小大于Bigjudge的文件，并打印。
    f1 = open(log_path + '/find_large_file_v1_log.txt','w')
    index = 1

    for name in os.listdir(dir_path):
        full_path = os.path.join(dir_path, name)
        if os.path.isfile(full_path):
            filesize = isLarge(full_path)            
            if filesize > 0:
                f1.write("[%s] "%(index) + str(full_path) + "\t" + str(filesize) + "\n")
                index = index + 1
                print(u"文件路径:%s 文件大小:%d"%(full_path,filesize))              
        if os.path.isdir(full_path):
            getAlltree(full_path, log_path)
 
def main():
    # 获取当前执行文件的工作目录
    filename = sys.argv[0]
    dirname = os.path.dirname(filename)
    abspath = os.path.abspath(dirname)

    getAlltree(dir_path, abspath)
    print("搜索结束orz")

if __name__ == '__main__': 
    main()