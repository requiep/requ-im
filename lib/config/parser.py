import yaml


class Config(object):
    with open('/Users/mak/Desktop/ruqu-im/requ.yml', 'r') as requConfigIO:
        requ = yaml.safe_load(requConfigIO)
