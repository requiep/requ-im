# Getting Started
## Installing
The beginning of this section and the study of the program as a whole begins with the basics, namely, how to download applications and install it on your operating system so that it works, let's start with the installation:

### MacOs, Linux
```bash
git clone https://github.com/requiep/requ-im.git && cd requ-im

source bin/requ.sh

requ -i <your-python-folder-path>
```

### Windows
```bash
git clone https://github.com/requiep/requ-im.git && cd requ-im

bin/requ.bat

requ -i <your-python-folder-path>
```

## Starting setup for yourself
You can skip this step, but you can also customize the editor for yourself, you can also change the configuration of commands and keybindings for yourself, and later distribute them to your friends or work colleagues, let's start with the simplest one - the editor configuration, there are all the main settings, we don't recommend changing the first section: `screen` as this can lead to problems.

`requ.yml` - configuration file where 80% of all information about the application and its data is stored

`lib/modules/syntax/cnf/syntax.yml` - color theme configuration file, you can change the highlighting of tokens to any color from the list of possible

`lib/modules/syntax/syntax.py` - you can also add lexers for other languages or your own in this script, get lexer you can from [pygments.lexer](https://pygments.org/languages/) website

## Hot Keys - Quick Programming
You can also change your hotkeys to your own in a separate file shown in the section above.

Hot keys are the most important thing in this editor, because without them the whole meaning of the editor is lost, but with them this editor becomes super fast, all the keys are arranged in a convenient order in which it will be convenient for you to press according to statistics, we have a key tables:
- File keys table, keys that work with files 

| key    | function          |
|--------|-------------------|
| Ctrl+N | New .python file  |
| Ctrl+S | Save current file |

- Dictionary layout, keys that work with words and lines

| key    | function        |
|--------|-----------------|
| Ctrl+F | Search word     |
| Ctrl+R | Remove one line |

- Move layout, keys that help move in text

| key    | function           |
|--------|--------------------|
| Ctrl+L | Scroll End of text |
| Ctrl+B | Scroll Up of text  |
| Ctrl+T | Move right of line |
| Ctrl+D | Move left of line  |
| Ctrl+A | Set Y down         |
| Ctrl+K | Set Y top          |

## Languages
In this editor, it is possible to create your own lexers to create a subgrid, you can also select the lexer you need from the `Pygments` website in the `pygments.lexer` section, there are a lot of them, and you can also connect it as shown in the post-last section, you can also create your lexer, you can find more details [here](https://pygments.org/docs/lexerdevelopment/), you can also connect it, you need to connect it in any path or via `pypi`, you can also read more about `Pygments` [here](https://pygments.org/).