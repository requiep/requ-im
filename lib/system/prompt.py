import sys
import curses


class RequPrompt(object):
    def __init__(self, editor_class=None) -> None:
        self.editor_class = editor_class

    def search(self) -> None:
        self.editor_class.funcs.search_results = []
        self.editor_class.funcs.search_index = 0
        word = self.command_prompt('search:')
        for row in range(len(self.editor_class.funcs.buffer)):
            buffer_row = self.editor_class.funcs.buffer[row]
            for col in range(len(buffer_row)):
                if ''.join([chr(c) for c in buffer_row[col:col + len(word)]]) == word:
                    self.editor_class.funcs.search_results.append([row, col])
        if len(self.editor_class.funcs.search_results):
            self.editor_class.funcs.current_y, self.editor_class.funcs.current_x = self.editor_class.funcs.search_results[self.editor_class.funcs.search_index]
            self.editor_class.funcs.search_index += 1

    def clear_prompt(self, line: str = None) -> None:
        command_line = f'\x1b[{str(self.editor_class.rows + 1)};0H'
        command_line += f'\x1b[7m{line}'
        pos = f'Row {str(self.editor_class.funcs.current_y + 1)}, Col {str(self.editor_class.funcs.current_x + 1)}'
        while len(command_line) < self.editor_class.cols - len(pos) + 10:
            command_line += ' '
        command_line += pos + ' '
        command_line += f'\x1b[{str(self.editor_class.rows + 1)};9H'
        sys.stdout.write(command_line)
        sys.stdout.flush()

    def command_prompt(self, line: str = None) -> str | None:
        self.clear_prompt(line)
        self.editor_class.screen.refresh()
        word = ''
        c, pos = -1, 0
        while c != 0x1b:
            c = -1
            while c == -1:
                c = self.editor_class.screen.getch()
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
            if not c == 127:
                pos += 1
                sys.stdout.write(chr(c))
                sys.stdout.flush()
                word += chr(c)
        self.editor_class.screen_module.update_screen()
        self.editor_class.screen.refresh()
        return word
