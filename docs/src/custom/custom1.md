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