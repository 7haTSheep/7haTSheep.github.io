@echo off
REM Double-click this on Windows to preview the site at http://localhost:8080
cd /d "%~dp0"
echo Serving at http://localhost:8080  --  press Ctrl+C to stop
start "" http://localhost:8080
python -m http.server 8080
