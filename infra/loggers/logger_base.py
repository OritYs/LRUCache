from abc import ABC


class LoggerBase(ABC):

    def __init__(self):
        super().__init__()
        self._logger = None

    def send_log_message(self, log_level, message):
        self._logger.log(msg=message, level=log_level)
