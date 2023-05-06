import yaml


class Config(object):
    with open('requ.yml', 'r') as requConfigIO:
        requ = yaml.safe_load(requConfigIO)

    with open('lib/modules/syntax/cnf/syntax.yml', 'r') as syntaxConfigIO:
        syntax = yaml.safe_load(syntaxConfigIO)
