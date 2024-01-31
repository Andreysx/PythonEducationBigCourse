from logging import Filter


class InfoFilter(Filter):
    def __init__(self, level):
        super().__init__()
        self.__level = level

    def filter(self, log_record):
        return log_record.levelno == self.__level