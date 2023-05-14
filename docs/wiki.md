# Start
Requ - code editor is designed for quick and free code editing using the terminal, also has many systems that will speed up programming, such as: `flake8`, `pygments`.

# Installation
There are two ways to install a project: manually and automatically, if your system is `Unix` then automatically and if your system is `Windows` then only manually.

## Install automatically
```bash
git clone https://github.com/requiep/requ-im.git && cd requ-im

source bin/requ.sh

requ -i

requ <path-to-edit-file>
```

## Manual setting
```bash
git clone https://github.com/requiep/requ-im.git && cd requ-im

python -m pip install --upgrade pip

python -m pip install -r requirements.txt

python setup.py <path-to-edit-file>
```

> For installation, you must have installed Python version 3.11 and higher, this is necessary for the correct operation of the application.

# Customization for yourself
The project has many files that you can edit for yourself, this is necessary for more convenient settings. There are not many such files, but they are, we will analyze each of them, I will also show their basic content.

`requ.yml` - configuration file where 80% of all information about the application and its data is stored
```yml
screen:
  keypad: true
  no_delay: true
default:
  default_filename: 'untitled.py'
  default_highlight: false
editor:
  vertical_lines: true
  vertical_line_sep: '|'
  color_mode: 'dark'
  white_space_dot: false
  white_space_dot_sep: '~'
path:
  log_errors_path: ['bin/logs/', 'errors.log']
```
`lib/modules/syntax/cnf/syntax.yml` - color theme configuration file, you can change the highlighting of tokens to any color from the list of possible
```yml
token: [
  "white",
  "white"
]
comment: [
  "gray",
  "gray"
]
preproc: [
  "gray",
  "gray"
]
[...]
```

`lib/modules/syntax/syntax.py` - you can also add lexers for other languages or your own in this script, get lexer you can from pygments.lexer website
```python
from pygments.lexers import PythonLexer, CLexer, JsonLexer
from pygments.lexers.shell import BashLexer
from pygments_markdown_lexer import MarkdownLexer
from pygments.lexers.data import YamlLexer
```

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

# Command line
In our editor, everything is based on the terminal, for this there is our `requ` command that executes several commands such as: `requ`, `requlib`, the last one has not yet been created. The `requ` command has flags

## Flags for the `requ` command
The `requ` command has several flags that give information, a list of which is here:
- `-i` download all required libraries
- `-h` gives help menu
- `-c` gives the contribution menu

## Create your own team or learn from an existing one
To create your own command or improve it, follow the path: `bin/requ.sh` in this file, write all the commands and texts. There is also a variable `PYTHON` which is the path of the python interpreter, you need it to run the setup and also run the file in automatic mode.