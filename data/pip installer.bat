@echo off

title "INSTALLING PIP"
:start
cls
set python_ver=39
pip install pyttsx3==2.71
pip install pywin32
pip install pythoncom
pip install playsound
pip install wikipedia
pip install gtts
pip install SpeechRecognition
pip install pycaw
pip install comtypes
pip install pyautogui
pip install pyperclip
pip install googletrans
pip install keyboard
pip install Color_Console
pip install youtube_search
pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl
cls
echo "   -----   DONE   -----   "
pause
cd..
py GUI.py
pause
py Mia.py
