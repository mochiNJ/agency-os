@echo off
title DB Tech Global - Agency Dashboard
echo.
echo   Starting your Agency Dashboard...
echo   Keep this window open while you use it.
echo.
echo   Opening in your browser: http://localhost:4321
echo.
start "" http://localhost:4321
node "%~dp0server.js"
pause
