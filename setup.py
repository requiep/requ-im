from editor import Requ

from lib.system.plug import RequPlug

import curses
import sys


def main(*args) -> None:
    editor = Requ()
    if len(sys.argv) >= 2:
        editor.file_system.open_file(sys.argv[1])
    else:
        editor.file_system.open_file('')
    returned_data = {
        "editor": editor,
        "filename": sys.argv[1],
        "config_class": editor.config,
        "file_system": editor.file_system,
        "keybind_class": editor.keybind,
        "syntax_module": editor.syntax_module,
        "screen_module": editor.screen_module,
        "function_module": editor.funcs
    }
    plug = RequPlug(returned_data)
    plug.init_plug()
    editor.start()


if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except Exception:
        pass
