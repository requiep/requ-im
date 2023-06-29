@echo off

set PYTHON=python
set MY_TITLE=Requ

:requ
set flags=%1

if "%flags%"=="-i" (
    rem Updating pip
    %2 -m pip install --upgrade pip
    rem Install all modules via pip
    %2 -m pip install -r requirements.txt
    cls
) else if "%flags%"=="-c" (
    echo If you want to help us or advise or correct our code,
    echo you can contact us via email: requiepmail@gmail.com.
    echo You can also write to the form on our website or
    echo contribute on GitHub. For more information, please
    echo visit the creator's GitHub profile.
) else if "%flags%"=="-h" (
    echo Application help menu: requ-im -
    echo   example:
    echo     requ <FLAG> <PYTHON_INTERPRETER>
    echo   options:
    echo       :args: - [
    echo         '-i' - installation
    echo         '-h' - help
    echo         '-c' - contribution
    echo         '<path>' - launch editor with specified path
    echo       ]
    echo   information:
    echo       :links: - [
    echo         'GitHub' - https://github.com/requiep/requ-im
    echo       ]
    echo   LICENSE - Apache License 2.0 /
    echo       https://github.com/requiep/requ-im/blob/main/LICENSE
    echo   AUTHOR - Requiep /
    echo       https://github.com/requiep/
) else (
    echo %MY_TITLE%
    %PYTHON% setup.py %flags%
)
