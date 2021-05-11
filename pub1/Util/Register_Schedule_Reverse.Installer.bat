rem ****
rem
rem This file install the Scheduler bat Files at the system
rem Run File with Elevated Privileges
rem
rem ****
@echo off

setlocal enableextensions enabledelayedexpansion

rem System Variables Set

set Dest_DIR=c:\pub1\Util

rem Check System

if not exist %Dest_DIR%\settings-reverse.ini exit /b 1
if not exist %Dest_DIR%\NIT.CredReplacer.exe exit /b 1


echo Run the Installer...

%Dest_DIR%\NIT.CredReplacer.exe
if not exist %Dest_DIR%\Register_Schedule_Reverse.bat exit /b 1
call %Dest_DIR%\Register_Schedule_Reverse.bat

echo Remove Temprorary Files...

del /F /Q %Dest_DIR%\Register_Schedule_Reverse.bat
del /F /Q %Dest_DIR%\Task_Daily.xml
del /F /Q %Dest_DIR%\Task_Half.xml
del /F /Q %Dest_DIR%\Task_Hourly.xml
del /F /Q %Dest_DIR%\Task_Kwint.xml
del /F /Q %Dest_DIR%\Task_Mounthly.xml
del /F /Q %Dest_DIR%\Task_Quart.xml
del /F /Q %Dest_DIR%\Task_Weekly.xml
del /F /Q %Dest_DIR%\Task_Write.xml

echo Install Succes!
exit /b 0
