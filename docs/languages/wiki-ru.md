> НАПИСАННО С ОШИБКАМИ
# Начало
Requ - редактор кода создан для быстрого и бесплатного редактиривания кода при помощи терминала, также имеет много систем которые ускорят программиривания, такие как: `flake8`, `pygments`. 

# Установка
Уставноить проект можно двумя способами: вручную и автоматически, если ваша система это `Unix` то автоматически а если ваша система это `Windows` тогда только вручную.

## Установка автоматически
```bash
git clone https://github.com/requiep/requ-im.git && cd requ-im

source bin/requ.sh

requ -i

requ <path-to-edit-file>
```

## Уставнока вручную
```bash
git clone https://github.com/requiep/requ-im.git && cd requ-im

python -m pip install --upgrade pip

python -m pip install -r requirements.txt

python setup.py <path-to-edit-file>
```

> Для уставноки у вас должен быть уставновлен пайтон версии 3.11 и выше, это надо для коректной работи приложения.

# Настрйока под себя
В проекте есть много файлов которые можно редактиривать под себя, это надо для более удобной настройки. Таких файлов не много но они есть, разберем каждый из них, также я покажу их базовое соержание.

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

# Фишки Редактора
У данного редакторгго есть много фишек, такие как проверка синтаксиса на ошибки, или подсветка, также есть кастомные кейбинди.

## Проверка синтаксиса кода на ошибки flake8
flake8 версии 6.0.0 позволяет брать линии ошибок или предупреждений, их также можно настоить по пути: `lib/modules/flake/` там находиться вся система, также чтобы обновить систему просто нажмите `Ctrl+R` это обновит `flake8`.

## Подсветка синтаксиса при помощи Pygments
Подсветка синтаксиса кода испольняеться при помощи `Pygments`, также есть папка в котором можно редактиривать все связное с подсветкой по пути: `lib/modules/syntax/`, также есть файл для настройки подсветки(было написанно ранее) и также файл в котором можно добавлять новые лексери для проекта для улучшения работи с каким либо языком программиривания.

## Горячие клавиши - облехчают программиривание
у данного редактора есть горячие клавиши которые облехчают работу с редактором но можно работать и без них, это зависит от вас и ваших предпочтений, горячие клавиши разделени на 3 типа:
1. File keys table, keys that work with files
    - Ctrl+N - New .python file
    - Ctrl+S - Save current file
2. Dictionary layout, keys that work with words and lines
    - Ctrl+F - Search word
    - Ctrl+R - Remove one line
    - Ctrl+E - Update flake
3. Move layout, keys that help move in text
    - Ctrl+L - Scroll End of text
    - Ctrl+B - Scroll Up of text
    - Ctrl+T - Move right of line
    - Ctrl+D - Move left of line
    - Ctrl+A - Set Y down
    - Ctrl+K - Set Y top

# Командная строка
В нашем редакторе все базуеться на терминале, для этого есть наша команда `requ` которя исполняет несколько команд таких как: `requ`, `requlib`, последняя ище не создана. У комнади `requ` есть флаги

## Флаги команди `requ`
У команди `requ` есть несколько флагов которие дают информацию, списко которых тут:
- `-i` скачивание всех нужных библиотек
- `-h` дает меню помощи
- `-c` дает меню контрибуции

## Создание своей комнади или учушения существуещей
Для создания свой комнади или ее улучшения требуеттьяс перейте по пути: `bin/requ.sh` в данном файле написани все комнади и тексти. Там также есть переменная `PYTHON` это путь у пайтон интерпретатору, надо это для запуска уставноки и также запуска файла в автоматическом режиме.