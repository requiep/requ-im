class FileSystem(object):
    def __init__(self, funcs_) -> None:
        self.highlight = None
        self.funcs_ = funcs_

    def open_file(self, filename: str = None) -> None:
        self.funcs_.reset_editor()
        try:
            with open(filename) as f:
                content = f.read().split('\n')
                for row in content[:-1]:
                    self.funcs_.buffer.append([ord(c) for c in row])
        except:
            self.funcs_.buffer.append([])
        if filename:
            self.funcs_.filename = filename
            if '.txt' in filename:
                self.highlight = False
        else:
            self.highlight = True
        self.funcs_.total_lines = len(self.funcs_.buffer)
        self.funcs_.update_screen()

    def save_file(self) -> None:
        with open(self.funcs_.filename, 'w') as f:
            content = ''
            for row in self.funcs_.buffer:
                content += ''.join([chr(c) for c in row]) + '\n'
            f.write(content)
        self.funcs_.modified = 0

    def new_file(self) -> None:
        self.funcs_.reset_editor()
        self.funcs_.buffer.append([])
        self.funcs_.total_lines = 1
