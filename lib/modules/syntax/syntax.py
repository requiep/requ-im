from pygments.lexers import PythonLexer
from pygments.token import Keyword, Name, Comment, String, \
    Number, Operator, Token


class Syntax(object):
    def __init__(self) -> None:
        self.color_scheme: dict = {
            Token: ('white', 'white'),
            Comment: ('gray', 'gray'),
            Comment.Preproc: ('gray', 'gray'),
            Keyword: ('red', 'red'),
            Keyword.Type: ('red', 'red'),
            Operator.Word: ('green', 'green'),
            Name.Builtin: ('cyan', 'cyan'),
            Name.Function: ('green', 'green'),
            Name.Class: ('blue', 'blue'),
            Name.Decorator: ('blue', 'blue'),
            Name.Variable: ('magenta', 'magenta'),
            String: ('green', 'green'),
            Number: ('blue', 'blue')
        }
        self.lexers = {
            'py': PythonLexer
        }
