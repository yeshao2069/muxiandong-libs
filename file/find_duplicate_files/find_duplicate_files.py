#coding=UTF-8
import os
import re
from collections import Counter
from collections import defaultdict
import chardet
import json

desDir = "F:/"     #请配置需要扫描的目录

DupHeaderFiles=[]
file_list = defaultdict(list)

# 获取文件编码类型
def get_encoding(file):
    # 二进制方式读取，获取字节数据，检测类型
    with open(file, 'rb') as f:
        data = f.read()

        return(chardet.detect(data)['encoding'])
 
# 查重
def find_Dup(fileName):
    code=get_encoding(fileName)
    f=open(fileName,'r',encoding=code)
    
    hasDup = False
    lines=f.readlines()
    f.close()

    #先筛选出包含"#include"的行
    include_lines = []
    for line in lines:
        if(re.match('#include', line)):
            include_lines.append(line)
    b = dict(Counter(include_lines))

    #判断文件是否有问题
    for key, value in b.items():
        if(value > 1):
            hasDup = True

    #记录问题        
    if(hasDup == True):
        print("问题文件:"+fileName)
        
        print("重复头文件:")
        p1 = re.compile(r'[<](.*?)[>]', re.S)  # 最小匹配
        p2 = re.compile(r'["](.*?)["]', re.S)
        toPrint=[key for key, value in b.items() if value > 1]  # 只展示重复元素
        for key in toPrint:
            
            if(re.findall(p1, key)):
                DupHeaderFile=re.findall(p1, key)[0]

            else:
                DupHeaderFile=re.findall(p2, key)[0]
            
            print(DupHeaderFile)
            file_list[fileName].append(DupHeaderFile) 
           
            DupHeaderFiles.append(DupHeaderFile) 
        
        #print("正在写入文件：filelog.txt......")

        write_to_filelog(file_list)#将问题文件与对应的重复头文件写入文件

        HeaderFiles = set(DupHeaderFiles) #去重
 
        #print("正在写入文件：HeaderFileLog.txt......")
        write_to_headerfilelog(HeaderFiles)  #将头文件列表写入文件

        
        print()
    
    


#将问题文件和对应的重复引用 写入文件
def write_to_filelog(file_list):
    json_str = json.dumps(file_list, indent=4)
    with open('FileLog.txt', 'w') as f:
        f.write(json_str)
        

#将头文件列表写入文件
def write_to_headerfilelog(HeaderFiles):
    with open('HeaderFileLog.txt', 'w') as f:
        for headerfile in HeaderFiles:
            f.write(headerfile+'\n')
        

#扫描指定目录下文件
def scan_files(directory, prefix=None, postfix=None):  
    print("开始扫描[{0}]......\n".format(directory))
    if not os.path.isdir(directory):  ##判断是否是目录
        print("{0} 目录有误,请检查".format(directory))
        exit(-1)


    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if special_file.endswith(".c") or special_file.endswith(".h"):  #添加后缀以便筛选文件
                #print("扫描中......："+os.path.join(root, special_file))                            
                find_Dup(os.path.join(root, special_file))



if __name__ == "__main__":
    scan_files(desDir)
    print("扫描完成！")
    print("写入文件完成！")