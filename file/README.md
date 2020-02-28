# python-libs
Written by python. It strives to streamline workflow.

### 查找大文件(find_large_files.py)
#### 需要手动设定文件上限值, 需要搜索的文件路径
#### 查找超过指定大小的文件并列举出来
#### 如果路径下有中文的目录, 会导致程序异常停止

### 查找大文件 Version2(find_large_files_v2.py)
#### 需要手动设定文件上限值, 需要搜索的文件路径
#### 查找超过指定大小的文件并列举出来
#### 可以查找带中文的路径,不会报错, 效果比version1好

### 查找重复文件 重复引用头文件(find_duplicate_files.py)
#### 可以查找指定路径下文件中的重复引用头文件

### 查找重复文件(find_duplicate_files_v2.py)
#### 可以查找指定路径下重复文件
#### 匹配规则是 重复的文件名或者字符串匹配

### 查找重复文件(find_duplicate_files_v3.py)
#### 可以查找指定路径下重复文件
#### 匹配规则是 重复的文件名以及数组,可以列举出哪些文件重复的列表

### 获取目录下所有文件的MD5(get_files_md5.py)
#### 可以获取指定目录下所有文件的MD5
#### 可以计算当前运行总时长

### 写入/读取文件(write_or_read_file.py)
#### 支持写入txt文本文件
#### 支持写入CSV文件
#### 支持写入Excel文件
#### 支持写入Word文件
#### 备注: 需要python3.x 需要安装xlwt, xlrd, python-docx
#### 备注: 执行命令时,文件不能被打开,否则报错提示没有权限

### 批量压缩js代码(min_js_files.py)
#### 需要安装node.js
#### 需要安装 uglify-js或者uglify-es
#### npm install uglify-js -g 或者 npm install uglify-es -g
#### 支持递归查找目录下所有js代码/也支持只查找单前层级的js代码
#### 备注: 比如 main.js 压缩成 main.min.js

### 批量压缩json代码(min_json_files.py)
#### 支持递归查找目录下所有json文件/也支持只查找单前层级的json文件
#### 备注: 比如 test1.json 压缩成 json_min_test1.json

### 批量格式化被压缩的json文件(format_json.py)
#### 需要格式化的json文件放到format_json_files目录
#### 支持递归查找目录下所有json文件/也支持只查找单前层级的json文件
#### 备注: 比如 test1.json 格式化成 formated_test1.json

### 批量格式化被压缩的js文件(format_js.py)
#### 需要格式化的js文件放到format_js_files目录
#### 支持递归查找目录下所有js文件/也支持只查找单前层级的js文件
#### 备注: 比如 test1.min.js 格式化成 formated_test1.min.js