@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion
title X2NSoft VDub - Cai dat tu dong

cd /d "%~dp0"

echo.
echo ============================================================
echo   X2NSoft VDub - CAI DAT TU DONG HOAN TOAN
echo ============================================================
echo.

echo.
echo ------------------------------------------------------------
echo  [1/5] Kiem tra Python
echo ------------------------------------------------------------

set "PY="
py -3 --version >nul 2>&1 && set "PY=py -3"
if not defined PY python --version >nul 2>&1 && set "PY=python"

if not defined PY (
    echo.
    echo  [LOI] Khong tim thay Python.
    echo.
    echo  Hay tai Python 3.10 tro len tai:
    echo      https://www.python.org/downloads/
    echo.
    echo  QUAN TRONG: khi cai NHO TICH o "Add Python to PATH".
    echo  Cai xong mo lai file nay.
    echo.
    pause
    exit /b 1
)

for /f "tokens=2" %%v in ('%PY% --version 2^>^&1') do set "PYVER=%%v"
echo  Da tim thay Python !PYVER!

echo.
echo ------------------------------------------------------------
echo  [2/5] Kiem tra ffmpeg
echo ------------------------------------------------------------

where ffmpeg >nul 2>&1
if errorlevel 1 (
    echo.
    echo  [CANH BAO] Khong tim thay ffmpeg. Thieu no thi KHONG xuat duoc video.
    echo  Hay cai dat ffmpeg va them vao PATH sau.
    echo.
) else (
    echo  Da tim thay ffmpeg
)

echo.
echo ------------------------------------------------------------
echo  [3/5] Tao moi truong ao (.venv) va cai thu vien
echo ------------------------------------------------------------
echo.

if exist ".venv" goto :venv_exists
echo  Dang tao moi truong ao (.venv)...
%PY% -m venv .venv
if errorlevel 1 goto :venv_fail
goto :venv_ok

:venv_exists
echo  Da co moi truong ao .venv.
goto :venv_ok

:venv_fail
echo  [LOI] Tao moi truong ao .venv that bai.
pause
exit /b 1

:venv_ok

set "VENV_PY=.venv\Scripts\python.exe"

echo  Dang cap nhat pip va cai dat cac thu vien tu requirements.txt...
"%VENV_PY%" -m pip install --upgrade pip
if errorlevel 1 goto :pip_fail
"%VENV_PY%" -m pip install -r requirements.txt
if errorlevel 1 goto :pip_fail
goto :pip_ok

:pip_fail
echo.
echo  [LOI] Cai thu vien that bai. Kiem tra mang roi thu lai.
pause
exit /b 1

:pip_ok
echo.
echo  Xong phan thu vien.

echo.
echo ------------------------------------------------------------
echo  [4/5] Tao file cau hinh .env
echo ------------------------------------------------------------

if exist ".env" goto :env_exists
copy ".env.example" ".env" >nul
echo  Da tao .env tu .env.example
goto :env_ok

:env_exists
echo  Da co .env tu truoc - giu nguyen, khong ghi de.

:env_ok

echo.
echo ------------------------------------------------------------
echo  [5/5] Cai bo nghe-chep va giong doc (Tu dong)
echo ------------------------------------------------------------
echo.

echo  Dang cai bo nghe-chep Whisper...
"%VENV_PY%" scripts\setup_whisper.py
if errorlevel 1 echo  [CANH BAO] Cai Whisper that bai.

echo.
echo  Dang cai bo nghe tieng Trung Paraformer...
"%VENV_PY%" scripts\setup_paraformer.py
if errorlevel 1 echo  [CANH BAO] Cai Paraformer that bai.

echo.
echo  Dang cai bo giong doc VieNeu...
"%VENV_PY%" scripts\setup_vieneu.py
if errorlevel 1 echo  [CANH BAO] Cai VieNeu that bai.

echo.
echo  Dang nap bo giong doc mau...
"%VENV_PY%" scripts\setup_voices.py
if errorlevel 1 echo  [CANH BAO] Nap giong mau that bai.

echo.
echo ============================================================
echo   CAI DAT HOAN TAT
echo ============================================================
echo.
echo   Mo ung dung: dup chuot vao file  chay_app.bat
echo.
pause
