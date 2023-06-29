from editor import Requ

import curses
import sys


def main(*args) -> None:
    editor = Requ()
    if len(sys.argv) >= 2:
        editor.file_system.open_file(sys.argv[1])
    else:
        editor.file_system.open_file('')
    editor.start()


if __name__ == "__main__":
    curses.wrapper(main)
