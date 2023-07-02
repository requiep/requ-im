# Requ - Code Editor
Requ is a code editor designed for quick and free code editing using the terminal. It provides many features that speed up programming, such as `flake8` and `pygments`.

## Installation
There are two ways to install the project: manually and automatically. If you're using a Unix system, you can install it automatically. For Windows systems, manual installation is required.

### Automatic Installation
```bash
git clone https://github.com/requiep/requ-im.git
cd requ-im
source bin/requ.sh
requ -i
requ <path-to-edit-file>
```

### Manual Installation
```bash
git clone https://github.com/requiep/requ-im.git
cd requ-im
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python setup.py <path-to-edit-file>
```
> Python version 3.11 or higher is required for the installation.

## Customization
The project provides files that you can edit to customize the settings. These files are necessary for a more convenient configuration. Let's take a look at each of them and their basic content.

### requ.yml
This is the configuration file where 80% of all information about the application and its data is stored. Here is an example of its content:
```yaml
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

### lib/modules/syntax/cnf/syntax.yml
This file is the color theme configuration file. You can change the highlighting of tokens to any color from the list of possibilities. Here is an example:
```yaml
token: [
  "white", "white"]
comment: [
  "gray", "gray"]
preproc: [
  "gray", "gray"]
[...]
```

### lib/modules/syntax/syntax.py
In this script, you can add lexers for other languages or your own. You can get lexers from the `pygments.lexer` website. Here is an example:
```python
from pygments.lexers import PythonLexer, CLexer, JsonLexer
from pygments.lexers.shell import BashLexer
from pygments_markdown_lexer import MarkdownLexer
from pygments.lexers.data import YamlLexer
```

## Editor Features
Requ offers many features, such as syntax checking for errors and highlighting, as well as custom keybindings.

### Check Code Syntax with Flake8
The editor uses flake8 version 6.0.0 to check code syntax for errors. You can set the path to errors or warnings along the path `lib/modules/flake/`. To update the system, press `Ctrl + E`.

### Syntax Highlighting with Pygments
Code syntax highlighting is performed using Pygments. You can edit everything related to highlighting in the `lib/modules/syntax/` folder. You can also add new lexers for the project to improve work with any programming language.

### Customizable Hotkeys
The editor provides hotkeys that make programming easier. Here are the three types of hotkeys available:

1. File keys table (keys that work with files):
   - Ctrl+N: New .python file
   - Ctrl+S: Save current file
2. Dictionary layout (keys that work with words and lines):
   - Ctrl+F: Search word
   - Ctrl+R: Remove one line
   - Ctrl+E: Update Flake
3. Move layout (keys that help move in text):
   - Ctrl+L: Scroll to the end of text
   - Ctrl+B: Scroll up in text
   - Ctrl+T: Move right in line
   - Ctrl+D: Move left in line
   - Ctrl+A: Set cursor to bottom
   - Ctrl+K: Set cursor to top

# Command Line
The editor operates through the terminal using the requ command, which executes several commands, including requ and requlib (the latter is not yet created). The requ command supports flags.

## Flags for the requ Command
The requ command supports several flags that provide information. Here is a list of the available flags:

- -i: Download all required libraries.
- -h: Show the help menu.
- -c: Show the contribution menu.

### Creating and Modifying Commands
To create your own command or improve an existing one, navigate to bin/requ.sh. In this file, you can write all the commands and texts. There is also a variable PYTHON that represents the path of the Python interpreter, which is needed to run the setup and execute files in automatic mode.

```vbnet
I made the following changes:
- Added a title to the README file.
- Changed the header formatting for the project name and description.
- Added headings to the "Installation," "Customization," "Editor Features," and "Command Line" sections.
- Adjusted the heading levels for sub-sections.
- Fixed minor grammar and wording issues.
- Replaced inline code formatting with code blocks where necessary.
- Improved the formatting and structure of code examples.
```

# Plugins
Plugins are a way to make the editor better, for this there is a special system in our editor, now I will show you and tell you how to use it and create your plugins correctly.

## Create a plugin
Let's start by creating a plugin, for this we need to place the necessary `.py` file in the `plugins/` folder, now we need the plugin architecture and how it will work, after creating the file we go into it, and we start by putting the class there for execution:
```python
class Plugin(object):
    def __init__(self) -> None:
        pass

    @staticmethod
    def init(*args) -> None:
        arguments = args[0]
        print('Hello from plugin!')
```
> Note the class name! it must contain the word `Plugin` otherwise the plugin will not work correctly!

And here is our first ready-made plugin model, then you can create your own plugins, by the way, classes with which you can and even need to work are passed to `*args`

This code works immediately when the editor is launched. Also now there will be a table of what is passed to the plugin:
- editor - The most important object or class, everything is important here, here the editor is assembled from small uxes into one, and then it disintegrates
- filename - File name (its path)
- Class objects
- config_class - Config class object, all configs are located there
  - file_system - File system class object
  - keybind_class - Class object with data about the keyboard, also hot keys, etc.
  - syntax_module - Syntax module, here is all the highlighting and all the magic of colors
  - screen_module - Screen module, everything you see on the screen, also most rendering
  - function_module - Functional module, here are all the main navigation functions as well as systems and also many other functions

All this can be used, for example, now I will show you a system that opens and immediately closes, this is like a plugin:
```python
class Plugin(object):
    def __init__(self) -> None:
        pass

    @staticmethod
    def init(*args) -> None:
        arguments = args[0]
        editor = arguments['editor']
        editor.exit()
```