@echo off
set target=%~1
if "%target%"=="" set target=%cd%

setlocal EnableDelayedExpansion

set LF=^


rem Previous two lines deliberately left blank for LF to work.

Set /a filenumber=0

for /f "tokens=*" %%i in ('dir /b /s /a:-d "%target%"') do (
    set ext=%%~xi
    Set /a filenumber+=1
    echo %filenumber%
    if "!ext!"=="" set ext=FileWithNoExtension
    echo !extlist! | find "!ext!:" > nul
    if not !ERRORLEVEL! == 0 set extlist=!extlist!!ext!:
)

echo Here are the extensions:

echo %extlist::=!LF!%

endlocal

pause