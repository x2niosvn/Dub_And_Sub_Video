@echo off
chcp 65001 >nul
title X2NSoft VDub

cd /d "%~dp0"

set "VENV_PY=.venv\Scripts\python.exe"

if exist "%VENV_PY%" goto :venv_ok
echo.
echo  [LOI] Khong tim thay moi truong ao (.venv). Hay chay  cai_dat.bat  truoc.
echo.
pause
exit /b 1

:venv_ok

if exist ".env" goto :env_ok
if exist ".env.example" copy ".env.example" ".env" >nul

:env_ok

echo  Dang mo X2NSoft VDub...
"%VENV_PY%" -m autodub_gui
if errorlevel 1 goto :app_fail
goto :eof

:app_fail
echo.
echo  [LOI] App khong mo duoc. Hay chay lai  cai_dat.bat  roi thu lai.
echo  Van loi thi bao loi tai:
echo      https://github.com/ttthanh2044/x2nsoft_vdub/issues
echo.
pause
