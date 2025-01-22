@echo off
REM Запуск игры TERMINAL 2025

REM Проверка, установлен ли Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python не установлен. Установите Python и добавьте его в PATH.
    pause
    exit /b
)

REM Активация виртуального окружения (если используется)
if exist "venv\Scripts\activate" (
    call venv\Scripts\activate
) else (
    echo Виртуальное окружение не найдено. Запуск без активации.
)

REM Запуск игры
python main.py

REM Пауза, чтобы окно не закрывалось сразу после завершения игры
pause