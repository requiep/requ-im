import sys
import colors as color

from .funcs import Functions
from lib.utils import Logger
from lib.config.parser import Config

from pygments import highlight
from pygments.formatters import TerminalFormatter


class Screen(object):
    def __init__(self, funcs: Functions = None) -> None:
        self.funcs: Functions = funcs
        self.config = Config()

    def print_status_bar(self) -> str:
        status = '\x1b[7m'
        status += f'{self.funcs.filename} - {str(self.funcs.total_lines)} lines'
        status += ' modified' if self.funcs.modified else ' saved'
        pos = f'Row {str(self.funcs.current_y + 1)}, Col {str(self.funcs.current_x + 1)}'
        while len(status) < self.funcs.editor.cols - len(pos) + 3:
            status += ' '
        status += pos + ' '
        status += '\x1b[m'
        status += f'\x1b[{str(self.funcs.current_y - self.funcs.offset_y + 1)};' + str(
            self.funcs.current_x - self.funcs.offset_x + 1) + 'H'
        status += '\x1b[?25h'
        return status

    def print_bufferer(self) -> str:
        print_bufferer = '\x1b[?25l'
        print_bufferer += '\x1b[H'
        for row in range(self.funcs.editor.rows):
            buffer_row = row + self.funcs.offset_y
            if buffer_row < self.funcs.total_lines:
                row_length = len(self.funcs.buffer[buffer_row]) - self.funcs.offset_x
                if row_length < 0:
                    row_length = 0
                if row_length > self.funcs.editor.cols:
                    row_length = self.funcs.editor.cols
                try:
                    print_bufferer += highlight(
                        ''.join([chr(c) for c in self.funcs.buffer[buffer_row][
                                                 self.funcs.offset_x: self.funcs.offset_x + row_length]]),
                        self.funcs.editor.syntax_module.lexers[self.funcs.filename.split('.')[-1]](),
                        TerminalFormatter(bg=self.config.requ['editor']['color_mode'],
                                          colorscheme=self.funcs.editor.syntax_module.color_scheme))[:-1]
                    if self.config.requ['editor']['white_space_dot']:
                        print_bufferer = print_bufferer.replace(' ',
                                                                f"{self.config.requ['editor']['white_space_dot_sep']}")
                        if self.config.requ['editor']['vertical_lines']:
                            print_bufferer = print_bufferer.replace(
                                f"{self.config.requ['editor']['white_space_dot_sep']*4}",
                                f"{self.config.requ['editor']['vertical_line_sep']}   ")
                    else:
                        if self.config.requ['editor']['vertical_lines']:
                            print_bufferer = print_bufferer.replace(
                                '    ',
                                f"{self.config.requ['editor']['vertical_line_sep']}   ")
                except Exception as error:
                    print_bufferer += ''.join(
                        [chr(c) for c in self.funcs.buffer[buffer_row][
                                         self.funcs.offset_x: self.funcs.offset_x + row_length]])
            print_bufferer += '\x1b[K'
            print_bufferer += '\r\n'
        return print_bufferer

    def update_screen(self) -> None:
        self.funcs.scroll_bufferer()
        print_bufferer = self.print_bufferer()
        status_bar = self.print_status_bar()
        sys.stdout.write(print_bufferer + status_bar)
        sys.stdout.flush()
