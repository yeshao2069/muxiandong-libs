#-*-coding:utf-8-*-
import os
import zipfile
import time

# cocos creator 引擎路径
creator_engine_path = "E:/CocosCreator/CocosCreator.exe"
# cocos creator 工程目录
creator_project_path = "E:/GamesHub/"

# 压缩zip 
def zip_file_path(input_path, output_path, output_name):
    f = zipfile.ZipFile(output_path + '/' + output_name, 'w', zipfile.ZIP_DEFLATED)
    filelists = []
    get_zip_file(input_path, filelists)
    for file in filelists:
        f.write(file)
    f.close()
    return output_path + r"/" + output_name

def get_zip_file(input_path, result):
    files = os.listdir(input_path)
    for file in files:
        if os.path.isdir(input_path + "/" + file):
            get_zip_file(input_path + "/" + file, result)
        else:
            result.append(input_path + "/" + file)

if __name__ == "__main__":
	# 切换工作路径
	print(u"切换工作路径到:%stools"%(creator_project_path))
	os.chdir(creator_project_path + "tools")

	# 编译并打包
	print(u"编译并打包Web-mobile")
	os.system(creator_engine_path + " --path ..\ --build")

	# 切换路径(避免打包的zip包有很多不需要的分层)
	os.chdir(creator_project_path + "build/debug/web-mobile")

	# 压缩成zip包并重命名
	print(u"压缩成zip包并重命名")
	file_zip_name = time.strftime("web-mobile-%Y-%m-%d-%H-%M-%S.zip",time.localtime(time.time()))
	zip_file_path("./","../",file_zip_name)