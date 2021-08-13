@echo off
mode con cols=81 lines=25
set /a n=0
:cycle
echo ---------------------------------------------------------------------------------
set /a n+=1
echo 正在进行第%n%次尝试
echo.
.\main.exe
timeout /t 2
goto :cycle