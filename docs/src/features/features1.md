# Editor Features
This editor has many features, such as syntax checking for errors, or highlighting, there are also custom keybindi.

## Check code syntax for errors flake8
flake8 version 6.0.0 allows you to take lines of errors or warnings, they can also be set along the path: `lib/modules/flake/` the whole system is there, also to update the system just press `Ctrl + R` this will update `flake8`.

## Syntax highlighting with Pygments
Code syntax highlighting is performed using `Pygments`, there is also a folder in which you can edit everything related to highlighting along the path: `lib/modules/syntax/`, there is also a file for configuring highlighting (it was written earlier) and also a file in which you can add new lexeries for the project to improve work with any programming language.

## Hot keys - make programming easier
this editor has hotkeys that make it easier to work with the editor, but you can work without them, it depends on you and your preferences, hotkeys are divided into 3 types:
1. File keys table, keys that work with files
    - Ctrl+N - New .python file
    - Ctrl+S - Save current file
2. Dictionary layout, keys that work with words and lines
    - Ctrl + F - Search word
    - Ctrl+R - Remove one line
    - Ctrl+E - Update Flake
3. Move layout, keys that help move in text
    - Ctrl+L - Scroll End of text
    - Ctrl+B - Scroll Up of text
    - Ctrl+T - Move right of line
    - Ctrl+D - Move left of line
    - Ctrl+A - Set Y down
    - Ctrl+K - Set Y top