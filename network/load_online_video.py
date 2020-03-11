import os


def init_you_get():
	print("init_you_get 开始")
	os.system("pip3 install you-get")
	os.system("pip3 install --upgrade you-get")
	print("init_you_get 完成")

def load_video(url,file_path):
	# you-get -i url
	# you-get url
	# you-get --format=flv360 url
	print("load from %s\nsave file to %s"%(url,file_path))
	os.chdir(file_path)
	os.system("you-get %s"%(url))

if __name__ == '__main__':
	# init_you_get()
	
	# url = input("请输入需要下载的网络资源的地址:")
	# file_path = input("请输入需要保存资源的文件地址:")
	url = "https://www.iqiyi.com/v_19ruzj9ny0.html"
	file_path = "F://test"
	load_video(url,file_path)