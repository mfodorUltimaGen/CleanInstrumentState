@echo off
setlocal
set "current_dir=%~dp0"
rem cd Path\To\Python\Project\updateState
python updator.py %current_dir:~0,-1%
endlocal

