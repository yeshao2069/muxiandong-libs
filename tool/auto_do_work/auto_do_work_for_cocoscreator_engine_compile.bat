@echo off
echo ��ǰ�ļ�Ŀ¼ %CD%
echo �����Զ��������ļ�Ŀ¼...
cd /d G:\myC3DEngine
echo ��ǰ�ļ�Ŀ¼ %cd%

@REM dir *.* /B
echo ��ѡ��ģʽ��
echo [1] install gulp and run build
echo [2] run build
set /p mode=ѡ��ģʽ��
echo ��ѡ��ģʽ: %mode%

echo ��ѡ��汾��
echo [1] Cocos Creator 2.4.3
echo [2] Cocos Creator 3D 1.2.0
echo [3] Cocos Creator 3D 1.2.1
@REM ��������
@REM set ver_len = 3
@REM set ver[1].value = Cocos Creator 2.4.3
@REM set ver[2].value = Cocos Creator 3D 1.2.0
@REM set ver[3].value = Cocos Creator 3D 1.2.1

set /p version=ѡ��汾:
echo ��ѡ��汾: %version%
@REM �Ƚ� EQU - ���� ; NEQ - ������; LSS - С�� ; LEQ - С�ڻ���� ; GTR - ���� ; GEQ - ���ڻ����
if %version% equ 1 ( goto goVer1 ) else ( if %version% equ 2 ( goto goVer2 ) else ( if %version% equ 3 ( goto goVer3 ) else ( echo wrong )))

:goVer1
cd 2d/2.4.3/engine
echo ��ǰ�ļ�Ŀ¼ %cd%
if %mode% equ 1 ( goto installAndRun ) else ( if %mode% equ 2 ( goto run2) else ( echo something wrong.))
pause

:goVer2
cd 3d/1.2.0/engine
echo ��ǰ�ļ�Ŀ¼ %cd%
if %mode% equ 1 ( goto installAndRun ) else ( if %mode% equ 2 ( goto run3) else ( echo something wrong.))
pause

:goVer3
cd 3d/1.2.1/engine
echo ��ǰ�ļ�Ŀ¼ %cd%
if %mode% equ 1 ( goto installAndRun ) else ( if %mode% equ 2 ( goto run3) else ( echo something wrong.))
pause

@REM ��װgulp��������
@REM ��װ������ģ��
@REM ��������
:installAndRun
npm install -g gulp
npm install
echo install finished
npm run build
echo run finished.
pause

@REM ��������
:run3
npm run build
echo run finished.
pause

@REM ��������
:run2
gulp build-dev
echo run finished.
pause