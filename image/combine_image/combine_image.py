# coding=UTF-8
import PIL.Image as Image
import os
import sys
# PIL 是 python image labrary, 需要3.x以上使用
# pip3 install pillow
# 如果pip需要20.0.2版本以上,不过不够版本需要提升pip版本
# python -m pip install --upgrade pip

# 图片格式
IMAGES_FORMAT = ['.jpg', '.JPG']
# 每张小图片的大小
IMAGE_SIZE = 256
# 图片间隔，也就是合并成一张图后，一共有几行
IMAGE_ROW = 2
# 图片间隔，也就是合并成一张图后，一共有几列
IMAGE_COLUMN = 2
# 备注 IMAGE_ROW * IMAGE_COLUMN = 4, 至少需要4张

# 创建文件夹
def MkDir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False

def image_init(image_path):
    # 获取图片集地址下的所有图片名称
    image_names = [name for name in os.listdir(image_path) for item in IMAGES_FORMAT if os.path.splitext(name)[1] == item]

    # 简单的对于参数的设定和实际图片集的大小进行数量判断
    if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
            raise ValueError("合成图片的参数和要求的数量不能匹配！")

    return image_names
    
# 定义图像拼接函数
def image_compose(image_names, image_path, save_path):
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE)) #创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(image_path + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize((IMAGE_SIZE, IMAGE_SIZE),Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE, (y - 1) * IMAGE_SIZE))

    MkDir(save_path)
    return to_image.save(save_path + "save_image.jpg") # 保存新图

if __name__ == '__main__':
    # 切换到当前执行文件的工作目录下
    filename = sys.argv[0]
    dirname = os.path.dirname(filename)
    abspath = os.path.abspath(dirname)
    os.chdir(abspath)
    print(os.getcwd())

    # 图片集地址
    image_path = './need_combine_images\\'
    save_path = "./save_image\\"
    
    image_names = image_init(image_path)
    image_compose(image_names, image_path, save_path) #调用函数