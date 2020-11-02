#encoding=UTF-8
import os
import sys
# 需要安装python
# 需要安装node.js
# 需要安装 uglify-js或者uglify-es
# npm install uglify-js -g 或者 npm install uglify-es -g

# 处理一个
def ProcOne(parent, filename):
    if not filename.lower().endswith('.js'):    #忽略非js文件
        return
    if filename.lower().endswith('.min.js'):    #忽略已压缩的js文件
        return

    srcFile = os.path.join(parent, filename)
    dstFile = srcFile[:-3] + '.min.js'
    cmd = 'uglifyjs "%s" -o "%s"' % (srcFile, dstFile)
    print('%s ...' % cmd)
    os.system(cmd)

# 处理所有
# recursive 为 True，遍历 root 目录
# recursive 为 False，只处理 root 的一级目录
def ProcAll(root, recursive=True):
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

    ProcAll(r'%s/test_js_codes'%(abspath), recursive=False)