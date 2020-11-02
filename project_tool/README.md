# python-libs
Written by python. It strives to streamline workflow.

### 基于Cocos Creator工程,检查未被使用的资源(checkImage.py)
#### 需要手动修改需要排查的文件路径, 根文件路径, 文件类型
#### checkFiles.txt(自动生成) 该路径下的所有筛选的所有文件
#### imgInfo.txt(自动生成) 当前文件下所有的图片名称
#### log.txt(自动生成) 当前文件下所有未被所用的图片名称

### (加强)基于Cocos Creator工程,检查未被使用的资源(checkImage_v2.py)
#### 需要手动修改需要排查的meta文件根路径, meta文件类型, 需要排查的文件的根文件路径, 文件类型
#### all_check_files.txt(自动生成) 该路径下的所有筛选的所有文件
#### all_image_info.txt(自动生成) 该路径下的所有文件下所有的图片名称
#### collect_meta_list(自动生成) 该路径下的所有筛选的meta文件
#### unuse_image_list.txt(自动生成) 该路径下的所有未被所用的图片名称

## Egret自动打包(egret_pack)
### Egret ios自动打包(ios_package.py)
#### 配置路径等,需要配置config.json 设置ios工程路径等
##### work egret游戏工程路径
##### ios egret生成的ios工程路径
##### tools 为当前打包脚本的路径
##### ftp 为需要发送Ftp地址等
##### ios-json 为打包egret有时候会生成多余的skin.exmls文件的备份,如果不备份,需要自己手动删除不需要的内容,否则打包失败或者打的包进入游戏会异常
##### ios-egret-json 为打包egret备份文件,设置打包类型为ios打包
#### ios打包脚本流程解释(ios_package.py)
##### Step1 切换当前的工作路径到当前的打包脚本目录下,然后读取config.json
##### Step2 执行打包脚本,开始打包
##### Step3 命令行清屏,更新git,更新完成后替换ios-egret-json后,发布ios项目,替换default-thm-json文件,清理Xcode项目
##### Step4 使用Xcode命令xcodebuild生成archive包,再打包成ipa包,重命名ipa包
##### Step5 发送ipa包到ftp上,结束

### Egret android自动打包(android_package.py)
#### 配置路径等,需要配置config.json 设置android工程路径等
##### work egret游戏工程路径
##### android egret生成的android工程路径
##### tools 为当前打包脚本的路径
##### ftp 为需要发送Ftp地址等
##### android-json 为打包egret有时候会生成多余的skin.exmls文件的备份,如果不备份,需要自己手动删除不需要的内容,否则打包失败或者打的包进入游戏会异常
##### android-egret-json 为打包egret备份文件,设置打包类型为android打包
#### 配置安装打包环境env.profile 设置android studio环境参数
##### 设置ndk enviroment路径
##### 设置sdk enviroment路径
##### 设置ant enviroment路径
##### 设置gradle environment路径
#### android打包脚本流程解释(android_package.py)
##### Step1 切换当前的工作路径到当前的打包脚本目录下,然后读取config.json
##### Step2 初始化android打包环境env
##### Step3 执行打包脚本,开始打包
##### Step4 命令行清屏,更新git,更新完成后替换android-egret-json后,发布android项目,替换default-thm-json文件,清理Gradle(Android Studio)项目
##### Step5 使用gradle命令编译并发布release/debug包(.apk),重命名apk
##### Step6 发送apk包到ftp上,结束

### Egret android/ios热更新包(update_version.py)
#### 配置config.json
##### update路径下的path为本地的热更新资源备份,download_url为服务端热更新备份地址
#### 配置update_version.json
##### 和当前的游戏线上版本保持一致,v1,v2,v3 组合为1.0.x, 即v1=1,v2=0,v3=x
#### 热更新包流程解释
##### Step1 切换当前的工作路径到当前的打包脚本目录下,然后读取config.json,读取update_version.json
##### Step2 获取work,ios,android,update等路径,开始打更新包
##### Step3 ios热更新包,原理同执行一次ios打包后,在ios目录下获取js,resources等需要的资源,和update下旧版本的线上热更新的资源(也有可能没有旧的版本资源)比较,如果文件名和md5一致,则不添加,否则添加到filelist.json中,且拷贝资源到备份文件夹目录下,并记录当前的版本version.json,把所有需要的资源(js,resources),version.json,filelist.json等资源打包成zip包
##### Step4 android热更新包,原理同执行一次android打包后,在android目录下获取js,resources等需要的资源,和update下旧版本的线上热更新的资源(也有可能没有旧的版本资源)比较,如果文件名和md5一致,则不添加,否则添加到filelist.json中,且拷贝资源到备份文件夹目录下,并记录当前的版本version.json,把所有需要的资源(js,resources),version.json,filelist.json等资源打包成zip包
##### Step5 把生成的ios/android更新包改名并发到ftp上,结束
#### Egret 热更新匹配机制
##### 首次出包,将会把当前最新的js代码,resources资源等,打成apk/ipa. 当前最新的资源将作为热更新的匹配资源,和后续的热更新资源比较
##### 热更新包,将会对比当前项目中最新的资源和原本旧的资源的名字以及MD5值,如果js代码修改或者资源发生变化,那么相应的MD5值将产生变化.
##### 换句话说,如果当前资源名称在旧资源里面不存在,那么需要添加到热更新中;
##### 如果当前资源名称在旧的资源里面存在,但是md5不一致,即资源发生修改,也需要添加到热更新中;
##### 如果名称和MD5都一样,则资源未发生修改,则不添加;
##### 如果在最新js代码或者资源不存在,但是旧的资源中存在,那么有可能该资源在最新中已经不需要且删除,不添加,但是也没有办法从原apk/ipa中删除资源(不好实现,就不管,该资源变成无用垃圾存在原包,但是不引用的情况下,不会影响)
##### 更新列表filelist.json列举所有需要热更新(新增的/修改的)的资源,打包成zip
##### 服务端收到zip,把zip解压后,把所有的文件资源(不能修改原本文件的层级,因为这个文件的路径,已经被记录到filelist.json中,文件和json中的路径一一对应),放到原本config.json中定义的远程下载地址上.客户端就可以从远程获取资源列表以及资源和原本资源做比较且下载了

## Cocos自动打包(cocos_pack)
### Cocos Creator Web-Mobile自动打包(creator_publish_web_mobile.py)
#### 设置构建发布相关选项, 打开引擎->项目->构建发布
#### 游戏名称,初始场景,参与构建场景等等,根据自身游戏设定
#### 选择发布平台 Web Mobile
#### 选择发布路径 默认为build(但是因为我经常需要出debug包,所以我设定的是项目路径下/build/debug, 如果你不这么使用, 需要修改python脚本中的路径和这个保持一致)
#### 其余默认,运行脚本,在build/debug中会生成编译后的zip包. 加压缩后放到web服务端运行即可.

### Cocos Creator Web-Desktop自动打包与Web-Mobile一样,不过要修改发布平台, 这两种都是html5(h5)打包方式
#### 备注:Web-Mobile默认会将游戏视图撑满整个手机浏览器窗口
#### 备注:Web-Desktop平台允许在发布时指定一个游戏视图的分辨率，而且之后游戏视图也不会随着浏览器窗口大小变化而变化，一般构建运行在 PC 浏览器上。