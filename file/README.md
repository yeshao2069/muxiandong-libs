# python-libs
Written by python. It strives to streamline workflow.

### (筛选)Creator工程,剔除目标路径下未被使用的资源(checkImage.py)
#### 需要手动修改需要排查的文件路径, 根文件路径, 文件类型
#### checkFiles.txt(自动生成) 该路径下的所有筛选的所有文件
#### imgInfo.txt(自动生成) 当前文件下所有的图片名称
#### log.txt(自动生成) 当前文件下所有未被所用的图片名称

### (筛选/加强功能3)Creator工程,剔除目标路径下未被使用的资源(checkImage_v2.py)
#### 需要手动修改需要排查的meta文件根路径, meta文件类型, 需要排查的文件的根文件路径, 文件类型
#### all_check_files.txt(自动生成) 该路径下的所有筛选的所有文件
#### all_image_info.txt(自动生成) 该路径下的所有文件下所有的图片名称
#### collect_meta_list(自动生成) 该路径下的所有筛选的meta文件
#### unuse_image_list.txt(自动生成) 该路径下的所有未被所用的图片名称

### 查找大文件(find_large_file.py)
#### 需要手动设定文件上限值, 需要搜索的文件路径
#### 查找超过指定大小的文件并列举出来
#### 如果路径下有中文的目录, 会导致程序异常停止

### 查找大文件 Version2(find_large_file_v2.py)
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

### 获取目录下所有文件的MD5(get_file_md5.py)
#### 可以获取指定目录下所有文件的MD5
#### 可以计算当前运行总时长

### 写入/读取文件(write_or_read_file.py)
#### 支持写入txt文本文件
#### 支持写入CSV文件
#### 支持写入Excel文件