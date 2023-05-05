class SyntaxParser(object):
    def __init__(self, config_dict: dict = None) -> None:
        self.config_dict: dict = config_dict
        self.syntax_list: list = self.parse_syntax_yml(config_dict)

    @staticmethod
    def parse_syntax_yml(config_dict: dict = None) -> list:
        local_list: list = []
        for item in config_dict['syntax']:
            local_list.append(config_dict['syntax'][item])
        return local_list
