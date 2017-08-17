@echo off
set /p file_name=please enter file_name:
set /p line=please enter max_line for split:
echo script star...
python split.py tmp\%file_name% %line%

pause
