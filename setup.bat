@echo off

rem Download the Python 3.8 installer
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.8.12/python-3.8.12-amd64.exe', 'python-3.8.12-amd64.exe')"

rem Install Python 3.8
python-3.8.12-amd64.exe /quiet InstallAllUsers=1 PrependPath=1

rem Install the required libraries
python -m pip install --upgrade pip
pip install -r requirements.txt

rem Clean up the installer file
del python-3.8.12-amd64.exe
