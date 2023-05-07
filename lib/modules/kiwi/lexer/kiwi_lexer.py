from pygments.lexer import RegexLexer
from pygments.token import Punctuation, Whitespace, \
    Text, Comment, Operator, Keyword, Name, String, Number, Generic
from pygments.lexer import Lexer, RegexLexer, do_insertions, bygroups, \
    include, default, this, using, words, line_re


class KiwiLexer(RegexLexer):
    name = 'Kiwi'
    aliases = [
        'kiwi'
    ]
    filenames = [
        '*.kiwi'
    ]

    tokens = {
        'root': [
            include('basic'),
            (r'`', String.Backtick, 'backticks'),
            include('data'),
            include('interp'),
        ],
        'interp': [
            (r'\(', Keyword, 'math'),
            (r'\$\{#?', String.Interpol, 'curly'),
            (r'\$[a-zA-Z_]\w*', Name.Variable),  # user variable
            (r'\$(?:\d+|[#$?!_*@-])', Name.Variable),  # builtin
            (r'\$', Text),
        ],
        'basic': [
            (r'\b(fun|print|import|if|this|return|else|private|package|interpret|class|inline)(\s*)\b',
             bygroups(Keyword, Whitespace)),
            (r'\b(false|true|lateinit|load|log|this|by|or|\B\$\w+)(?=[\s)`])',
             Name.Builtin),
            (r'\B\@\w+', Name.Decorator),
            (r'\A#!.+\n', Comment.Hashbang),
            (r'#.*\n', Comment.Single),
            (r'\\[\w\W]', String.Escape),
            (r'[\[\]{}()=]', Operator),
            (r':', Operator),
            # (r'&&|\|\|', Operator)
        ],
        'data': [
            (r'(?s)\$?"(\\.|[^"\\$])*"', String.Double),
            (r'"', String.Double, 'string'),
            (r"(?s)\$'(\\\\|\\[0-7]+|\\.|[^'\\])*'", String.Single),
            (r"(?s)'.*?'", String.Single),
            (r',', Punctuation),
            (r'\s+', Whitespace),
            (r'\d+\b', Number),
            (r'[^=\s\[\]{}()$"\'`\\<&|;]+', Text),
            (r'<', Text),
        ],
        'string': [
            (r'"', String.Double, '#pop'),
            (r'(?s)(\\\\|\\[0-7]+|\\.|[^"\\$])+', String.Double),
            include('interp'),
        ],
        'curly': [
            (r'\}', String.Interpol, '#pop'),
            (r':-', Keyword),
            (r'\w+', Name.Variable),
            (r'[^}:"\'`$\\]+', Punctuation),
            (r':', Punctuation),
            include('root'),
        ],
        'math': [
            (r'\)\)', Keyword, '#pop'),
            (r'\*\*|\|\||<<|>>|[-+*/%^|&<>]', Operator),
            (r'\d+#[\da-zA-Z]+', Number),
            (r'\d+#(?! )', Number),
            (r'0[xX][\da-fA-F]+', Number),
            (r'\d+', Number),
            (r'[a-zA-Z_]\w*', Name.Variable),  # user variable
            include('root'),
        ],
        'backticks': [
            include('root'),
        ],
    }
