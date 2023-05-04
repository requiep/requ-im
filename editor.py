from lib.modules.syntax import Syntax
from lib.system import FileSystem
from lib.modules import Functions
from lib.config import Config
import curses
import sys


class Requ(object):
    def __init__(self) -> None:
        self.config: Config = Config()

        self.screen = curses.initscr()
        self.screen.keypad(self.config.requ['screen']['keypad'])
        self.screen.nodelay(self.config.requ['screen']['no_delay'])

        self.funcs: Functions = Functions(self)
        self.file_system: FileSystem = FileSystem(self.funcs)

        self.rows, self.cols = self.screen.getmaxyx()
        self.rows -= 1

        self.syntax_module: Syntax = Syntax()

        curses.raw()
        curses.noecho()

    def resize_window(self) -> None:
        self.rows, self.cols = self.screen.getmaxyx()
        self.rows -= 1
        self.screen.refresh()
        self.funcs.update_screen()

    def read_keyboard(self) -> None:
        def ctrl(c):
            return ((c) & 0x1f)

        c = -1
        while c == -1:
            c = self.screen.getch()
        if c == ctrl(ord('q')):
            self.exit()
        elif c == 9:
            [self.funcs.insert_char(ord(' ')) for i in range(4)]
        elif c == 353:
            [self.funcs.delete_char() for i in range(4) if self.funcs.current_x]
        elif c == ctrl(ord('u')):
            [self.funcs.delete_char() for i in range(1) if self.funcs.current_x]
        elif c == ctrl(ord('n')):
            self.file_system.new_file()
        elif c == ctrl(ord('s')):
            self.file_system.save_file()
        elif c == ctrl(ord('f')):
            self.funcs.search()
        elif c == ctrl(ord('d')):
            self.funcs.delete_line()
        elif c == ctrl(ord('t')):
            self.funcs.indent()
        elif c == curses.KEY_RESIZE:
            self.resize_window()
        elif c == curses.KEY_HOME:
            self.funcs.current_x = 0
        elif c == curses.KEY_END:
            self.funcs.current_x = len(self.funcs.buffer[self.funcs.current_y])
        elif c == curses.KEY_LEFT:
            self.funcs.move_cursor(c)
        elif c == curses.KEY_RIGHT:
            self.funcs.move_cursor(c)
        elif c == curses.KEY_UP:
            self.funcs.move_cursor(c)
        elif c == curses.KEY_DOWN:
            self.funcs.move_cursor(c)
        elif c == curses.KEY_BACKSPACE:
            self.funcs.delete_char()
        elif c == curses.KEY_NPAGE:
            self.funcs.scroll_page(c)
        elif c == curses.KEY_PPAGE:
            self.funcs.scroll_page(c)
        elif c == ctrl(ord('e')):
            self.funcs.scroll_end()
        elif c == ctrl(ord('p')):
            self.funcs.scroll_home()
        elif c == 560:
            self.funcs.skip_word(560)
        elif c == 545:
            self.funcs.skip_word(545)
        elif c == ord('\n'):
            self.funcs.insert_line()
        elif ctrl(c) != c:
            self.funcs.insert_char(c)

    def clear_prompt(self, line: str = None) -> None:
        command_line = '\x1b[' + str(self.rows + 1) + ';' + '0' + 'H'
        command_line += '\x1b[7m' + line
        pos = 'Row ' + str(self.funcs.current_y + 1) + ', Col ' + str(self.funcs.current_x + 1)
        while len(command_line) < self.cols - len(pos) + 10:
            command_line += ' '
        command_line += pos + ' '
        command_line += '\x1b[' + str(self.rows + 1) + ';' + '9' + 'H'
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
            if c == curses.KEY_BACKSPACE:
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
        self.funcs.update_screen()
        self.screen.refresh()
        return word

    @staticmethod
    def exit() -> None:
        curses.endwin()
        sys.exit(0)

    def start(self) -> None:
        self.funcs.update_screen()
        while True:
            self.read_keyboard()
            self.funcs.update_screen()
