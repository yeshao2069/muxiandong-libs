# bat-libs
Written by bat. It strives to streamline workflow.

### CocosCreator引擎编译(auto_do_work_for_cocoscreator_engine_compile.bat)
```
mode = 1 > 安装gulp环境并安装，且编译引擎
mode = 2 > 编译引擎
```
```
version = 1 > Cocos Creator 2.4.3
version = 2 > Cocos Creator 3D 1.2.0
version = 3 > Cocos Creator 3D 1.2.1
```
###### 备注：如果需要更多的版本，需要自己手动添加，且需要goto函数等
###### 备注：默认的自定义引擎放置在G:\myC3DEngine，如果需要修改，请在bat中修改这个路径为自己需要的路径
###### 备注：Cocos Creator2.x系列放置到2d目录下，且以版本号命名文件名作为区别，如Cocos Creator 2.4.3, 是2.x系列，完整的引擎路径为 G:\myC3DEngine\2d\2.4.3\engine，如果需要修改为不同，请自行修改
###### 备注：Cocos Creator3D 系列放置到3d目录下，且以版本号命名文件名作为区别，如Cocos Creator 3D 1.2.0, 是3D系列，完整的引擎路径为 G:\myC3DEngine\3d\1.2.0\engine