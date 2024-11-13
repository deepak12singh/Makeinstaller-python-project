@echo off

REM Define the project name and paths
set "project_name=ProjectStart"
set PROJECT_PATH=C:\%project_name%

REM Check for administrator privileges
net session >nul 2>&1
if %errorlevel% neq 0 (
    REM echo Requesting administrator privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

REM Step 1: Remove the project folder
if exist "%PROJECT_PATH%" (
    echo Deleting project folder at %PROJECT_PATH%...
    rmdir /S /Q "%PROJECT_PATH%"
    if %errorlevel% neq 0 (
        echo Error: Failed to delete project folder. Exiting...
        exit /b
    )
    echo Project folder deleted.
) else (
    echo Warning: Project folder not found at %PROJECT_PATH%.
)

REM Notify completion
echo Uninstallation complete.
pause
