import curses
import sys

from lib.modules.syntax import Syntax
from lib.system import FileSystem
from lib.keybind import KeyBind
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
        self.file_system: FileSystem = FileSystem(
                self.funcs, self.screen_module)

        self.rows, self.cols = self.screen.getmaxyx()
        self.rows -= 1

        self.syntax_module: Syntax = Syntax(self.config.syntax)

        self.keybind = KeyBind(self)

        curses.raw()
        curses.noecho()

    def resize_window(self) -> None:
        self.rows, self.cols = self.screen.getmaxyx()
        self.rows -= 1
        self.screen.refresh()
        self.screen_module.update_screen()

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
            self.keybind.key_bind()
            self.screen_module.update_screen()


