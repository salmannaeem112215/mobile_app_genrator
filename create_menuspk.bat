@echo off

set PYTHON_EXECUTABLE=python
set SCRIPT_PATH=creater.py
set ARG1=menuspk
set ARG2=com.menuspk
set ARG3="https://menuspk.com"
set ARG4="C:/SALMAN/gits/web_app_cerater/apps"
set ARG5="C:/SALMAN/gits/web_app_cerater/app_icons/menuspk.png"
set ARG6="Discover endless possibilities with menuspk.com your go-to destination for modern website templates, from e-commerce and portfolios to food and digital marketing, all designed for easy customization and a standout online presence."

%PYTHON_EXECUTABLE% %SCRIPT_PATH% %ARG1% %ARG2% %ARG3% %ARG4% %ARG5% %ARG6%

pause
