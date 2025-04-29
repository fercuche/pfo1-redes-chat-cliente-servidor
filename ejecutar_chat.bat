@echo off
echo Iniciando servidor...
start /B python servidor.py
set SERVER_PID=%ERRORLEVEL%

REM Esperar 1 segundo para que el servidor se inicie
sleep 1

echo Iniciando cliente...
python cliente.py

echo Finalizando servidor...
REM Cerrar el servidor usando taskkill (mata el proceso de Python)
taskkill /IM python.exe /F > nul

echo Todo finalizado.
pause
