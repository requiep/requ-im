import curses
import sys

from lib.modules.syntax import Syntax
from lib.system import FileSystem
from lib.config import Config
from lib import Functions, Screen


class Requ(object):
    def __init__(self) -> None:
        self.config: Config = Config()

        self.screen = curses.initscr()
        self.screen.keypad(self.config.requ['screen']['keypad'])
        self.screen.nodelay(self.config.requ['screen']['no_delay'])

        self.funcs: Functions = Functions(self)
        self.screen_module: Screen = Screen(self.funcs)
        self.file_system: FileSystem = FileSystem(self.funcs, self.screen_module)

        self.rows, self.cols = self.screen.getmaxyx()
        self.rows -= 1

        self.syntax_module: Syntax = Syntax(self.config.syntax)

        curses.raw()
        curses.noecho()

    def resize_window(self) -> None:
        self.rows, self.cols = self.screen.getmaxyx()
        self.rows -= 1
        self.screen.refresh()
        self.screen_module.update_screen()

    def read_keyboard(self) -> None:
        def ctrl(code: int = 0) -> int:
            return code & 0x1f
        c = -1
        while c == -1:
            c = self.screen.getch()
        if c == ctrl(ord('q')):
            self.exit()
        elif c == ctrl(ord('b')):
            self.funcs.scroll_home()
        elif c == ctrl(ord('n')):
            self.file_system.new_file()
        elif c == ctrl(ord('s')):
            self.file_system.save_file()
        elif c == ctrl(ord('f')):
            self.funcs.search()
        elif c == ctrl(ord('r')):
            self.funcs.delete_line()
        elif c == ctrl(ord('l')):
            self.funcs.scroll_end()
        elif c == ctrl(ord('t')):
            self.funcs.current_x = len(self.funcs.buffer[self.funcs.current_y])-1
        elif c == ctrl(ord('d')):
            self.funcs.current_x = 0
        elif c == ord('\n'):
            self.funcs.insert_line()
        elif c == ctrl(ord('a')):
            if self.funcs.current_y < self.funcs.total_lines-1:
                if len(self.funcs.buffer[self.funcs.current_y+1])-1 >= self.funcs.current_x:
                    self.funcs.current_y += 1
        elif c == ctrl(ord('k')):
            if self.funcs.current_y > 0:
                if len(self.funcs.buffer[self.funcs.current_y - 1]) - 1 >= self.funcs.current_x:
                    self.funcs.current_y -= 1
        elif c == 9:
            [self.funcs.insert_char(ord(' ')) for i in range(4)]
        elif c == 353:
            [self.funcs.delete_char() for i in range(4) if self.funcs.current_x]
        elif c == 127:
            [self.funcs.delete_char() for i in range(1) if self.funcs.current_x]
        elif c == 560:
            self.funcs.skip_word(560)
        elif c == 545:
            self.funcs.skip_word(545)
        elif c == curses.KEY_RESIZE:
            self.resize_window()
        elif c == curses.KEY_LEFT:
            self.funcs.move_cursor(c)
        elif c == curses.KEY_RIGHT:
            self.funcs.move_cursor(c)
        elif c == curses.KEY_UP:
            self.funcs.move_cursor(c)
        elif c == curses.KEY_DOWN:
            self.funcs.move_cursor(c)
        elif ctrl(c) != c:
            self.funcs.insert_char(c)

    def clear_prompt(self, line: str = None) -> None:
        command_line = f'\x1b[{str(self.rows + 1)};0H'
        command_line += f'\x1b[7m{line}'
        pos = f'Row {str(self.funcs.current_y + 1)}, Col {str(self.funcs.current_x + 1)}'
        while len(command_line) < self.cols - len(pos) + 10:
            command_line += ' '
        command_line += pos + ' '
        command_line += f'\x1b[{str(self.rows + 1)};9H'
        sys.stdout.write(command_line)
        sys.stdout.flush()

    def command_prompt(self, line: str = None) -> str | None:
        self.clear_prompt(line)
        self.screen.refresh()
        word = ''
        c, pos = -1, 0
        while c != 0x1b:
            c = -1
            while c == -1:
                c = self.screen.getch()
            if c == 10:
                break
            if c == 127:
                pos -= 1
                if pos < 0:
                    pos = 0
                    continue
                sys.stdout.write('\b')
                sys.stdout.write(' ')
                sys.stdout.write('\b')
                sys.stdout.flush()
                word = word[:len(word) - 1]
            if c != curses.KEY_BACKSPACE:
                pos += 1
                sys.stdout.write(chr(c))
                sys.stdout.flush()
                word += chr(c)
        self.screen_module.update_screen()
        self.screen.refresh()
        return word

    @staticmethod
    def exit() -> None:
        curses.endwin()
        sys.exit(0)

    def start(self) -> None:
        self.screen_module.update_screen()
        while True:
            self.read_keyboard()
            self.screen_module.update_screen()

