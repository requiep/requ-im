import curses
import sys

from pygments import highlight
from pygments.formatters import TerminalFormatter


class Functions(object):
    def __init__(self, editor=None) -> None:
        self.search_index = None
        self.search_results = None
        self.modified = None
        self.filename = None
        self.total_lines = None
        self.buffer = None
        self.offset_y = None
        self.current_y = None
        self.offset_x = None
        self.current_x = None

        self.editor = editor

    def reset_editor(self) -> None:
        self.current_x, self.current_y = 0, 0
        self.offset_x, self.offset_y = 0, 0
        self.buffer = []
        self.total_lines = 0
        self.filename = self.editor.config.requ['default']['default_filename']
        self.modified = 0
        self.search_results = []
        self.search_index = 0

    def insert_char(self, c: str = None) -> None:
        self.buffer[self.current_y].insert(self.current_x, c)
        self.current_x += 1
        self.modified += 1

    def delete_char(self) -> None:
        if self.current_x:
            self.current_x -= 1
            del self.buffer[self.current_y][self.current_x]
        elif self.current_x == 0 and self.current_y:
            oldline = self.buffer[self.current_y][self.current_x:]
            del self.buffer[self.current_y]
            self.current_y -= 1
            self.current_x = len(self.buffer[self.current_y])
            self.buffer[self.current_y] += oldline
            self.total_lines -= 1
        self.modified += 1

    def insert_line(self) -> None:
        oldline = self.buffer[self.current_y][self.current_x:]
        self.buffer[self.current_y] = self.buffer[self.current_y][:self.current_x]
        self.current_y += 1
        self.current_x = 0
        self.buffer.insert(self.current_y, [] + oldline)
        self.total_lines += 1
        self.modified += 1

    def delete_line(self) -> None:
        if len(self.buffer) == 1:
            return
        try:
            del self.buffer[self.current_y]
            self.current_x = 0
            self.total_lines -= 1
        except:
            pass
        self.modified += 1
        if self.current_y >= self.total_lines:
            self.current_y = self.total_lines - 1

    def indent(self) -> None:
        indent = self.editor.command_prompt('indent:')
        try:
            start_row = self.current_y
            end_row = self.current_y + int(indent.split()[0])
            start_col = self.current_x
            end_col = self.current_x + int(indent.split()[1])
            dir = indent.split()[2]
            try:
                char = indent.split()[3]
            except:
                char = ''
            for row in range(start_row, end_row):
                for col in range(start_col, end_col):
                    if dir == '+':
                        self.buffer[row].insert(col, ord(char if char != '' else ' '))
                    if dir == '-':
                        del self.buffer[row][self.current_x]
            self.modified += 1
        except:
            pass

    def move_cursor(self, key: int = 0) -> None:
        row = self.buffer[self.current_y] if self.current_y < self.total_lines else None
        if key == curses.KEY_LEFT:
            if self.current_x != 0:
                self.current_x -= 1
            elif self.current_y > 0:
                self.current_y -= 1
                self.current_x = len(self.buffer[self.current_y])
        elif key == curses.KEY_RIGHT:
            if row is not None and self.current_x < len(row):
                self.current_x += 1
            elif row is not None and self.current_x == len(row) and self.current_y != self.total_lines - 1:
                self.current_y += 1
                self.current_x = 0
        elif key == curses.KEY_UP:
            if self.current_y != 0:
                self.current_y -= 1
            else:
                self.current_x = 0
        elif key == curses.KEY_DOWN:
            if self.current_y < self.total_lines - 1:
                self.current_y += 1
            else:
                self.current_x = len(self.buffer[self.current_y])
        row = self.buffer[self.current_y] if self.current_y < self.total_lines else None
        rowlen = len(row) if row is not None else 0
        if self.current_x > rowlen:
            self.current_x = rowlen

    def skip_word(self, key: int = 0) -> None:
        if key == 545:
            self.move_cursor(curses.KEY_LEFT)
            try:
                if self.buffer[self.current_y][self.current_x] != ord(' '):
                    while self.buffer[self.current_y][self.current_x] != ord(' '):
                        if self.current_x == 0:
                            break
                        self.move_cursor(curses.KEY_LEFT)
                elif self.buffer[self.current_y][self.current_x] == ord(' '):
                    while self.buffer[self.current_y][self.current_x] == ord(' '):
                        if self.current_x == 0:
                            break
                        self.move_cursor(curses.KEY_LEFT)
            except:
                pass
        if key == 560:
            self.move_cursor(curses.KEY_RIGHT)
            try:
                if self.buffer[self.current_y][self.current_x] != ord(' '):
                    while self.buffer[self.current_y][self.current_x] != ord(' '):
                        self.move_cursor(curses.KEY_RIGHT)
                elif self.buffer[self.current_y][self.current_x] == ord(' '):
                    while self.buffer[self.current_y][self.current_x] == ord(' '):
                        self.move_cursor(curses.KEY_RIGHT)
            except:
                pass

    def search(self) -> None:
        self.search_results = []
        self.search_index = 0
        word = self.editor.command_prompt('search:')
        for row in range(len(self.buffer)):
            bufferrow = self.buffer[row]
            for col in range(len(bufferrow)):
                if ''.join([chr(c) for c in bufferrow[col:col + len(word)]]) == word:
                    self.search_results.append([row, col])
        if len(self.search_results):
            self.current_y, self.current_x = self.search_results[self.search_index]
            self.search_index += 1

    def scroll_end(self) -> None:
        while self.current_y < self.total_lines - 1:
            self.scroll_page(curses.KEY_NPAGE)

    def scroll_home(self) -> None:
        while self.current_y:
            self.scroll_page(curses.KEY_PPAGE)

    def scroll_page(self, key: int = 0) -> None:
        count = 0
        while count != self.editor.rows:
            if key == curses.KEY_NPAGE:
                self.move_cursor(curses.KEY_DOWN)
                if self.offset_y < self.total_lines - self.editor.rows:
                    self.offset_y += 1
            elif key == curses.KEY_PPAGE:
                self.move_cursor(curses.KEY_UP)
                if self.offset_y:
                    self.offset_y -= 1
            count += 1

    def scroll_bufferer(self) -> None:
        if self.current_y < self.offset_y:
            self.offset_y = self.current_y
        if self.current_y >= self.offset_y + self.editor.rows:
            self.offset_y = self.current_y - self.editor.rows + 1
        if self.current_x < self.offset_x:
            self.offset_x = self.current_x
        if self.current_x >= self.offset_x + self.editor.cols:
            self.offset_x = self.current_x - self.editor.cols + 1

    def print_status_bar(self) -> str:
        status = '\x1b[7m'
        status += self.filename + ' - ' + str(self.total_lines) + ' lines'
        status += ' modified' if self.modified else ' saved'
        pos = 'Row ' + str(self.current_y + 1) + ', Col ' + str(self.current_x + 1)
        while len(status) < self.editor.cols - len(pos) + 3:
            status += ' '
        status += pos + ' '
        status += '\x1b[m'
        status += '\x1b[' + str(self.current_y - self.offset_y + 1) + ';' + str(
            self.current_x - self.offset_x + 1) + 'H'
        status += '\x1b[?25h'
        return status

    def print_bufferer(self) -> str:
        print_bufferer = '\x1b[?25l'
        print_bufferer += '\x1b[H'
        for row in range(self.editor.rows):
            bufferrow = row + self.offset_y
            if bufferrow < self.total_lines:
                rowlen = len(self.buffer[bufferrow]) - self.offset_x
                if rowlen < 0:
                    rowlen = 0
                if rowlen > self.editor.cols:
                    rowlen = self.editor.cols
                try:
                    print_bufferer += highlight(
                        ''.join([chr(c) for c in self.buffer[bufferrow][self.offset_x: self.offset_x + rowlen]]),
                        self.editor.syntax_module.lexers[self.filename.split('.')[-1]](),
                        TerminalFormatter(bg='dark', colorscheme=self.editor.syntax_module.color_scheme))[:-1]
                except:
                    print_bufferer += ''.join(
                        [chr(c) for c in self.buffer[bufferrow][self.offset_x: self.offset_x + rowlen]])
            print_bufferer += '\x1b[K'
            print_bufferer += '\r\n'
        return print_bufferer

    def update_screen(self) -> None:
        self.scroll_bufferer()
        print_bufferer = self.print_bufferer()
        status_bar = self.print_status_bar()
        sys.stdout.write(print_bufferer + status_bar)
        sys.stdout.flush()
