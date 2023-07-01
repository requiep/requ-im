import curses


class KeyBind(object):
    def __init__(self, editor=None) -> None:
        self.editor = editor

        self.keys_dict: dict = {
            "ctrl": {
                "q": self.editor.exit,
                "b": self.editor.funcs.scroll_home,
                "n": self.editor.file_system.new_file,
                "s": self.editor.file_system.save_file,
                "f": self.editor.prompt.search,
                "r": self.editor.funcs.delete_line,
                "l": self.editor.funcs.scroll_end,
                "t": self.editor.funcs.scroll_right,
                "d": self.editor.funcs.scroll_left,
                "a": self.editor.funcs.y_down,
                "k": self.editor.funcs.y_up,
                "e": self.editor.screen_module.reload_flake}}

    @staticmethod
    def _ctrl(code: int = 0) -> int:
        return code & 0x1f

    def key_bind(self) -> None:
        c = -1
        while c == -1:
            c = self.editor.screen.getch()
        for ctrl_ in self.keys_dict['ctrl']:
            if c == self._ctrl(ord(ctrl_)):
                self.keys_dict['ctrl'][ctrl_]()
        self.command_keybind(c)

    def command_keybind(self, c: int = 0) -> None:
        if c == ord('\n'):
            self.editor.funcs.insert_line()
        elif c == 9:
            [self.editor.funcs.insert_char(ord(' ')) for i in range(4)]
        elif c == 353:
            [self.editor.funcs.delete_char() for i in range(4) if self.editor.funcs.current_x]
        elif c == 127:
            [self.editor.funcs.delete_char() for i in range(1) if self.editor.funcs.current_x]
        elif c == 560:
            self.editor.funcs.skip_word(560)
        elif c == 545:
            self.editor.funcs.skip_word(545)
        elif c == curses.KEY_RESIZE:
            self.editor.resize_window()
        elif c == curses.KEY_LEFT:
            self.editor.funcs.move_cursor(c)
        elif c == curses.KEY_RIGHT:
            self.editor.funcs.move_cursor(c)
        elif c == curses.KEY_UP:
            self.editor.funcs.move_cursor(c)
        elif c == curses.KEY_DOWN:
            self.editor.funcs.move_cursor(c)
        elif self._ctrl(c) != c:
            self.editor.funcs.insert_char(c)
