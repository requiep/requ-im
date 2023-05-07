from pygments.lexers import PythonLexer, CLexer, JsonLexer
from pygments.lexers.shell import BashLexer
from pygments_markdown_lexer import MarkdownLexer
from pygments.lexers.data import YamlLexer
from pygments.token import Keyword, Name, Comment, String, \
    Number, Operator, Token

from .syntax_parser import SyntaxParser

from lib.modules.kiwi.lexer import KiwiLexer


class Syntax(object):
    def __init__(self, config: dict = None) -> None:
        self.config: dict = config
        self.syntax_parser: SyntaxParser = SyntaxParser(self.config)

        self.color_scheme: dict = {
            Token: self.syntax_parser.syntax_list[0],
            Comment: self.syntax_parser.syntax_list[1],
            Comment.Preproc: self.syntax_parser.syntax_list[2],
            Keyword: self.syntax_parser.syntax_list[3],
            Keyword.Type: self.syntax_parser.syntax_list[4],
            Operator.Word: self.syntax_parser.syntax_list[5],
            Name.Builtin: self.syntax_parser.syntax_list[6],
            Name.Function: self.syntax_parser.syntax_list[7],
            Name.Class: self.syntax_parser.syntax_list[8],
            Name.Decorator: self.syntax_parser.syntax_list[9],
            Name.Variable: self.syntax_parser.syntax_list[10],
            String: self.syntax_parser.syntax_list[11],
            Number: self.syntax_parser.syntax_list[12]
        }
        self.lexers: dict = {
            "py": PythonLexer,
            "c": CLexer,
            "yml": YamlLexer,
            "json": JsonLexer,
            "md": MarkdownLexer,
            'sh': BashLexer,
            "kiwi": KiwiLexer
        }
