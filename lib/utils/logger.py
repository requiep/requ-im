import datetime


class Logger(object):
    def __init__(self, file_name: str = None) -> None:
        self.file_name: str = 'logs/errors.log'

        self.script_file_name: str = file_name

    def logger(self, place: str = None, message_string: str = None) -> None:
        date_ = datetime.date.today()
        now_ = datetime.datetime.now()
        time_ = now_.strftime("%H:%M:%S")
        with open(self.file_name, 'a') as fileIO:
            fileIO.write(f'{date_} {time_} {self.script_file_name}.{place} {message_string}\n')