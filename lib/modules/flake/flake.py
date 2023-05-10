import subprocess


class FlakeRead(object):
    def __init__(self) -> None:
        pass

    @staticmethod
    def normalize_to_list(list_: str = None) -> list:
        try:
            item_string = list_.split('\n')
            list_of_items: list = []
            for line in item_string:
                new_line = line.split(':')
                list_of_items.append(new_line[1])
            return list_of_items
        except Exception:
            pass

    def run_flake8(self, file_name: str = None) -> (list | str):
        process = subprocess.Popen(['flake8', file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        output = stdout.decode().strip()
        if output:
            numbers_list = self.normalize_to_list(output)
            string = ', '.join(numbers_list[:4])
            new_string = string[:-1] + '...'
            return new_string
        else:
            return []
