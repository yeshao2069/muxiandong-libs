#encoding=utf-8  
import io
import os
import sys  
import hashlib  
import string  
import re




rootPath = os.path.abspath(os.path.join(sys.argv[0], os.pardir))

# # input paths
ImageDir= os.path.join(rootPath, "input")

# temporary path to place the sprite sheets
OutputDir = os.path.join(rootPath, "output")

#PVRTC4
OutputDirPVRTC4 = os.path.join(OutputDir, "PVRTC4") #ios 中PVRTC4输出目录
#ETC
OutputDirETC =  os.path.join(OutputDir, "ETC") #android 中 ETC输出目录
#PNG
OutputDirPNG =  os.path.join(OutputDir, "PNG") #通用 中 PNG输出目录

OutputDirPNG8 =  os.path.join(OutputDir, "PNG8") #通用 中 PNG输出目录

# # path of the texture packer command line tool
TP="TexturePacker"


print("ImageDir = " + ImageDir)
print("OutputDir = " + OutputDir)
print("OutputDirPVRTC4 = " + OutputDirPVRTC4)
print("OutputDirETC = " + OutputDirETC)
print("OutputDirPNG = " + OutputDirPNG)
print("OutputDirPNG8 = " + OutputDirPNG8)
print("TP = " + TP)


#文件输出目录
def createPath(cPath):
    if not os.path.isdir(cPath):
        os.mkdir(cPath)


# --trim-sprite-names  去除png等后缀
# --multipack 多图片打包开起，避免资源图太多，生成图集包含不完全，开起则会生成多张图集。
# --maxrects-heuristics macrect的算法  参数 Best ShortSideFit LongSideFit AreaFit BottomLeft ContactPoint
# --enable-rotation 开起旋转，计算rect时如果旋转将会使用更优的算法来处理，得到更小的图集
# --border-padding 精灵之间的间距
# --shape-padding 精灵形状填充
# --trim-mode Trim 删除透明像素，大下使用原始大小。 参数 None Trim Crop CropKeepPos Polygon
# --basic-sort-by Name  按名称排序
# --basic-order Ascending 升序
# --texture-format 纹理格式
# --data 输出纹理文件的信息数据路径 plist
# --sheet 输出图集路径 png
# --scale 1 缩放比例 主要用于低分辨率的机子多资源适配。
# --max-size 最大图片像素 一般我是用的2048，超过2048以前的有些android机型不支持。
# --size-constraints 结纹理进行大小格式化，AnySize 任何大小 POT 使用2次幂 WordAligned
# --replace 正则表达式，用于修改plist加载后的名称
# --pvr-quality PVRTC 纹理质量
# --force-squared 强制使用方形
# --etc1-quality ETC 纹理质量
def pack_textures(inputPath, outputPath, opt, scale, maxSize, sheetSuffix, textureFormat, sizeConstraints, sheetName, otherParams, fileNameSuffix):
    packCommand = TP + \
        " --multipack" \
        " --format cocos2d-v2" \
        " --maxrects-heuristics best" \
        " --enable-rotation" \
        " --shape-padding 2" \
        " --border-padding 0" \
        " --trim-mode Trim" \
        " --basic-sort-by Name" \
        " --basic-order Ascending" \
        " --texture-format {textureFormat}" \
        " --data {outputSheetNamePath}{fileNameSuffix}.plist" \
        " --sheet {outputSheetNamePath}{fileNameSuffix}.{sheetSuffix}" \
        " --scale {scale}" \
        " --max-size {maxSize}" \
        " --opt {opt}" \
        " --size-constraints {sizeConstraints}" \
        " {inputPath}" \
        " {otherParams}"


    # win 和 mac 上处理正则表达式结果不一样
    if sys.platform == "win32":
        packCommand = packCommand + " --replace (.png)$=" \
            " --replace \\b={sheetName}_" \
            " --replace {sheetName}_$=.png"
    else:
        packCommand = packCommand + " --replace ^={sheetName}_"


    packCommand = packCommand.format(
        textureFormat=textureFormat,
        outputSheetNamePath=os.path.join(outputPath,sheetName) + "_{n}",
        sheetName=sheetName,
        sheetSuffix=sheetSuffix,
        scale=scale,
        maxSize=maxSize,
        opt=opt,
        sizeConstraints=sizeConstraints,
        inputPath=inputPath,
        otherParams=otherParams,
        fileNameSuffix=fileNameSuffix)
    os.system(packCommand)

if __name__ == '__main__':
    createPath(OutputDir)
    createPath(OutputDirPVRTC4)
    createPath(OutputDirETC)
    createPath(OutputDirPNG)
    createPath(OutputDirPNG8)
    for sheet in os.listdir(ImageDir):
        iPath = os.path.join(ImageDir, sheet)
        if os.path.isdir(iPath): 
            pack_textures(iPath,OutputDirPVRTC4,'PVRTCI_4BPP_RGBA',1,2048,'pvr.ccz',"pvr3ccz","POT",sheet,"--pvr-quality best --force-squared", "")
            pack_textures(iPath,OutputDirETC,'ETC1_RGB',1,2048,'pkm',"pkm","AnySize",sheet,"--etc1-quality high-perceptual", "")
            pack_textures(iPath,OutputDirETC,'ETC1_A',1,2048,'pkm',"pkm","AnySize",sheet,"--etc1-quality high-perceptual", "_alpha")
            pack_textures(iPath,OutputDirPNG,'RGBA8888',1,2048,'png',"png","AnySize",sheet,"--png-opt-level 7", "")
            pack_textures(iPath,OutputDirPNG8,'RGBA8888',1,2048,'png',"png8","AnySize",sheet,"--png-opt-level 7 --dither-type PngQuantHigh", "")