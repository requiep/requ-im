from lib.utils import Logger


class FileSystem(object):
    def __init__(self, funcs_=None, screen=None) -> None:
        self.funcs_ = funcs_
        self.screen = screen
        self.highlight: bool = self.funcs_.editor.config.requ['default']['default_highlight']

        self.logger = Logger('lib/system/filesystem.py')

    def open_file(self, filename: str = None) -> None:
        self.funcs_.reset_editor()
        try:
            with open(filename, 'r') as f:
                content = f.readlines()
                for row in content[:-1]:
                    self.funcs_.buffer.append([ord(c) for c in row])
                self.funcs_.buffer.append([ord(c) for c in content[-1]])
        except Exception as error:
            with open(filename, 'w') as f:
                content = [[]]
                for row in content[:-1]:
                    self.funcs_.buffer.append([ord(c) for c in row])
                self.funcs_.buffer.append([ord(c) for c in content[-1]])
            self.funcs_.buffer.append([])
            self.logger.logger('open_file', f'{error}')
        if filename:
            self.funcs_.filename = filename
            if '.txt' in filename:
                self.highlight = False
        else:
            self.highlight = True
        self.funcs_.total_lines = len(self.funcs_.buffer)
        self.screen.update_screen()

    def save_file(self) -> None:
        with open(self.funcs_.filename, 'w') as f:
            content = ''
            for row in self.funcs_.buffer:
                content += ''.join([chr(c) for c in row])
            f.write(content)
        self.funcs_.modified = 0

    def new_file(self) -> None:
        self.funcs_.reset_editor()
        self.funcs_.buffer.append([])
        self.funcs_.total_lines = 1
