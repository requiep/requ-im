import curses


class Functions(object):
    def __init__(self, editor=None) -> None:
        self.modified: int = 0
        self.filename: str = ''
        self.total_lines,  self.search_index = 0, 0
        self.buffer, self.search_results = [], []
        self.offset_y, self.offset_x = 0, 0
        self.current_y, self.current_x = 0, 0

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

    def insert_char(self, code: int = None) -> None:
        self.buffer[self.current_y].insert(self.current_x, code)
        self.current_x += 1
        self.modified += 1

    def delete_char(self) -> None:
        if self.current_x:
            self.current_x -= 1
            del self.buffer[self.current_y][self.current_x]
        elif self.current_x == 0 and self.current_y:
            old_line = self.buffer[self.current_y][self.current_x:]
            del self.buffer[self.current_y]
            self.current_y -= 1
            self.current_x = len(self.buffer[self.current_y])
            self.buffer[self.current_y] += old_line
            self.total_lines -= 1
        self.modified += 1

    def insert_line(self) -> None:
        old_line = self.buffer[self.current_y][self.current_x:]
        self.buffer[self.current_y] = self.buffer[self.current_y][:self.current_x]
        self.current_y += 1
        self.current_x = 0
        self.buffer.insert(self.current_y, [] + old_line)
        self.total_lines += 1
        self.modified += 1

    def delete_line(self) -> None:
        if len(self.buffer) == 1:
            return
        try:
            del self.buffer[self.current_y]
            self.current_x = 0
            self.total_lines -= 1
        except Exception:
            pass
        self.modified += 1
        if self.current_y >= self.total_lines:
            self.current_y = self.total_lines - 1

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
        row_length = len(row) if row is not None else 0
        if self.current_x > row_length:
            self.current_x = row_length

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
            except Exception:
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
            except Exception:
                pass

    def search(self) -> None:
        self.search_results = []
        self.search_index = 0
        word = self.editor.command_prompt('search:')
        for row in range(len(self.buffer)):
            buffer_row = self.buffer[row]
            for col in range(len(buffer_row)):
                if ''.join([chr(c) for c in buffer_row[col:col + len(word)]]) == word:
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
