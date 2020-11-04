@echo off
echo 当前文件目录 %CD%
echo 进入自定义引擎文件目录...
cd /d G:\myC3DEngine
echo 当前文件目录 %cd%

@REM dir *.* /B
echo 【选择模式】
echo [1] install gulp and run build
echo [2] run build
set /p mode=选择模式：
echo 你选择模式: %mode%

echo 【选择版本】
echo [1] Cocos Creator 2.4.3
echo [2] Cocos Creator 3D 1.2.0
echo [3] Cocos Creator 3D 1.2.1
@REM 定义数组
@REM set ver_len = 3
@REM set ver[1].value = Cocos Creator 2.4.3
@REM set ver[2].value = Cocos Creator 3D 1.2.0
@REM set ver[3].value = Cocos Creator 3D 1.2.1

set /p version=选择版本:
echo 你选择版本: %version%
@REM 比较 EQU - 等于 ; NEQ - 不等于; LSS - 小于 ; LEQ - 小于或等于 ; GTR - 大于 ; GEQ - 大于或等于
if %version% equ 1 ( goto goVer1 ) else ( if %version% equ 2 ( goto goVer2 ) else ( if %version% equ 3 ( goto goVer3 ) else ( echo wrong )))

:goVer1
cd 2d/2.4.3/engine
echo 当前文件目录 %cd%
if %mode% equ 1 ( goto installAndRun ) else ( if %mode% equ 2 ( goto run2) else ( echo something wrong.))
pause

:goVer2
cd 3d/1.2.0/engine
echo 当前文件目录 %cd%
if %mode% equ 1 ( goto installAndRun ) else ( if %mode% equ 2 ( goto run3) else ( echo something wrong.))
pause

:goVer3
cd 3d/1.2.1/engine
echo 当前文件目录 %cd%
if %mode% equ 1 ( goto installAndRun ) else ( if %mode% equ 2 ( goto run3) else ( echo something wrong.))
pause

@REM 安装gulp构建工具
@REM 安装依赖的模块
@REM 编译引擎
:installAndRun
npm install -g gulp
npm install
echo install finished
npm run build
echo run finished.
pause

@REM 编译引擎
:run3
npm run build
echo run finished.
pause

@REM 编译引擎
:run2
gulp build-dev
echo run finished.
pause