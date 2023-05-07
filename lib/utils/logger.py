import datetime
import os

from lib.config.parser import Config


class Logger(object):
    def __init__(self, file_name: str = None) -> None:
        self.config = Config()
        self.file_name: list = self.config.requ['path']['log_errors_path']

        self.script_file_name: str = file_name

    def logger(self, place: str = None, message_string: str = None) -> None:
        date_ = datetime.date.today()
        now_ = datetime.datetime.now()
        time_ = now_.strftime("%H:%M:%S")
        try:
            with open(self.file_name[0]+self.file_name[1], 'a') as fileIO:
                fileIO.write(f'{date_} {time_} {self.script_file_name}.{place} {message_string}\n')
        except FileNotFoundError:
            os.mkdir(self.file_name[0])
            with open(self.file_name[0]+self.file_name[1], 'w') as fp:
                pass
            with open(self.file_name[0] + self.file_name[1], 'a') as fileIO:
                fileIO.write(f'{date_} {time_} {self.script_file_name}.{place} {message_string}\n')
