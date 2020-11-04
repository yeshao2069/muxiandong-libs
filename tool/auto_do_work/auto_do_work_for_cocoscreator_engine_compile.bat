@echo off
echo Current WorkDirectory: %CD%
echo Enter My Engine WorkDirectory...
cd /d G:\myC3DEngine
echo Current WorkDirectory: %cd%

@REM dir *.* /B
echo [* Select Auto Mode *]
echo [1] install gulp and run build
echo [2] run build
set /p mode=Select Auto Mode:
echo You Choose Mode -> %mode%

echo [* Select Auto Cocos Creator Version *]
echo [1] Cocos Creator 2.4.3
echo [2] Cocos Creator 3D 1.2.0
echo [3] Cocos Creator 3D 1.2.1

set /p version=Select Auto Version:
echo You Choose Version -> %version%
if %version% equ 1 ( goto goVer1 ) else ( if %version% equ 2 ( goto goVer2 ) else ( if %version% equ 3 ( goto goVer3 ) else ( echo wrong )))

:goVer1
cd 2d/2.4.3/engine
echo Current WorkDirectory: %cd%
if %mode% equ 1 ( goto installAndRun ) else ( if %mode% equ 2 ( goto run2) else ( echo something wrong.))
pause

:goVer2
cd 3d/1.2.0/engine
echo Current WorkDirectory: %cd%
if %mode% equ 1 ( goto installAndRun ) else ( if %mode% equ 2 ( goto run3) else ( echo something wrong.))
pause

:goVer3
cd 3d/1.2.1/engine
echo Current WorkDirectory: %cd%
if %mode% equ 1 ( goto installAndRun ) else ( if %mode% equ 2 ( goto run3) else ( echo something wrong.))
pause

:installAndRun
npm install -g gulp
npm install
echo install finished
npm run build
echo run finished.
pause

:run3
npm run build
echo run finished.
pause

:run2
gulp build-dev
echo run finished.
pause