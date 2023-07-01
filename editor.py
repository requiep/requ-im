import curses
import sys

from lib.modules.syntax import Syntax
from lib.system import FileSystem, RequPrompt
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

        self.prompt: RequPrompt = RequPrompt(self)

        self.syntax_module: Syntax = Syntax(self.config.syntax)

        self.keybind: KeyBind = KeyBind(self)

        curses.raw()
        curses.noecho()

    def resize_window(self) -> None:
        self.rows, self.cols = self.screen.getmaxyx()
        self.rows -= 1
        self.screen.refresh()
        self.screen_module.update_screen()

    @staticmethod
    def exit() -> None:
        curses.endwin()
        sys.exit(0)

    def start(self) -> None:
        self.screen_module.update_screen()
        while True:
            self.keybind.key_bind()
            self.screen_module.update_screen()
